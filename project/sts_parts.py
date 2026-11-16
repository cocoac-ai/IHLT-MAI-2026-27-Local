"""Split the STS project notebook into one notebook per student, and merge them back.

    python sts_parts.py split          sts-project.ipynb -> sts-student1.ipynb, sts-student2.ipynb
    python sts_parts.py merge          the two parts -> sts-project.ipynb (cells keep their outputs)
    python sts_parts.py merge --run    the same, then run the whole notebook and copy the outputs back to the parts
    python sts_parts.py list           position, owner and first line of every cell

Every cell carries its position and its owner in its metadata: {"sts": {"order": 12, "owner": "1"}}.
The owner is "1", "2" or "both" (shared cells are kept in the notebook of student 1).
A new cell needs nothing: at merge time it is placed right after the cell above it and gets the owner
of the notebook where it was written.

Inside a part notebook, run_before(order) runs the code cells of both parts that come before a cell,
so that a student can work on one of their cells without running the other part by hand.
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FULL = HERE / "sts-project.ipynb"
PARTS = {"1": HERE / "sts-student1.ipynb", "2": HERE / "sts-student2.ipynb"}
HELPER = """\
**Part of student {n}.** This notebook holds only the cells of student {n}{shared}; the other cells are in `{other}`. \
The final notebook `sts-project.ipynb` is built from the two parts with `python sts_parts.py merge --run`.

- Edit only this notebook, not the final one. New cells are placed after the cell above them.
- The cells of the two parts are interleaved, so this notebook does not run from top to bottom by itself. \
To work on one cell, run the cell below with the position of that cell (`python sts_parts.py list` shows the positions): \
it runs everything that comes before it, from both parts.
"""
HELPER_CODE = """\
# Helper, not part of the final notebook: run the code cells of both parts that come before a position.
from sts_parts import run_before
# run_before(30)   # e.g. before working on the cell at position 30
"""


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write(path, notebook):
    Path(path).write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


def info(cell):
    return cell.get("metadata", {}).get("sts", {})


def first_line(cell):
    text = "".join(cell["source"]).strip()
    return text.split("\n")[0][:80] if text else "(empty)"


def helper_cells(n):
    shared = " and the shared ones (title and conclusions)" if n == "1" else ""
    other = PARTS["2" if n == "1" else "1"].name
    make = lambda kind, text: {"cell_type": kind, "id": f"helper-{kind}-{n}", "metadata": {"sts": {"helper": True}},
                               "source": text.splitlines(keepends=True),
                               **({"execution_count": None, "outputs": []} if kind == "code" else {})}
    return [make("markdown", HELPER.format(n=n, shared=shared, other=other)), make("code", HELPER_CODE)]


def split():
    """Write the two part notebooks from the final notebook (every cell must have an owner)."""
    full = read(FULL)
    missing = [first_line(c) for c in full["cells"] if "owner" not in info(c)]
    if missing:
        sys.exit("Cells without an owner in sts-project.ipynb (edit the parts, not the final notebook):\n  " + "\n  ".join(missing))
    for n, path in PARTS.items():
        cells = [c for c in full["cells"] if info(c)["owner"] == n or (n == "1" and info(c)["owner"] == "both")]
        write(path, {**full, "cells": helper_cells(n) + cells})
        print(f"{path.name}: {len(cells)} cells")


def collect():
    """All the cells of the two parts in the order of the final notebook."""
    cells = []
    for n, path in PARTS.items():
        order = 0.0
        for cell in read(path)["cells"]:
            meta = cell.setdefault("metadata", {}).setdefault("sts", {})
            if meta.get("helper"):
                continue
            if "order" not in meta:  # new cell: right after the cell above it
                order += 0.001 + 0.0001 * int(n)  # different steps: the two students never get the same position
                meta.update(order=round(order, 6), owner=n)
                print(f"new cell of student {n} at position {meta['order']}: {first_line(cell)}")
            order = meta["order"]
            cells.append(cell)
    orders = [info(c)["order"] for c in cells]
    duplicated = sorted({o for o in orders if orders.count(o) > 1})
    if duplicated:
        sys.exit(f"Two cells have the same position: {duplicated}")
    return sorted(cells, key=lambda c: info(c)["order"])


def merge(run=False):
    """Build the final notebook from the two parts; with run=True, execute it and copy the outputs back."""
    template = read(PARTS["1"])
    cells = collect()
    for position, cell in enumerate(cells):  # whole numbers again, so that new cells always fit in between
        info(cell)["order"] = position
    write(FULL, {**template, "cells": cells})
    print(f"{FULL.name}: {len(cells)} cells")
    if run:
        subprocess.run([sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace",
                        "--ExecutePreprocessor.timeout=1800", FULL.name], cwd=HERE, check=True)
    split()


def show():
    for cell in collect():
        print(f"{info(cell)['order']:>7}  {info(cell)['owner']:<4}  {cell['cell_type'][:4]}  {first_line(cell)}")


def run_before(order):
    """Run, in the current notebook, the code cells of both parts that come before the given position."""
    from IPython import get_ipython
    from IPython.utils.capture import capture_output
    shell = get_ipython()
    cells = [c for c in collect() if c["cell_type"] == "code" and info(c)["order"] < order]
    for cell in cells:
        with capture_output():
            result = shell.run_cell("".join(cell["source"]), store_history=False)
        if not result.success:
            print(f"Error in the cell at position {info(cell)['order']} (student {info(cell)['owner']}): {first_line(cell)}")
            result.raise_error()
    print(f"Ran {len(cells)} code cells before position {order}.")


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else ""
    if command == "split":
        split()
    elif command == "merge":
        merge(run="--run" in sys.argv)
    elif command == "list":
        show()
    else:
        sys.exit(__doc__)
