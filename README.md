# IHLT-MAI-2026-27-Local

Ran's own workspace for the UPC MAI course *Introduction to Human Language Technologies* (2026-27).

| Folder | What |
|---|---|
| `labs/` | My lab notebooks, one per lab (`Lab01`–`Lab09`). They compare the tools (NLTK, spaCy, FreeLing/TextServer) instead of using only the one of the submitted version |
| `project/` | My STS project notebook (SemEval 2012 Task 6) |
| `common/` | Shared code and caches: TextServer client, UKB and TextServer answers, `credentials.json` (ignored) |
| `data/` | Datasets (ignored): `train/`, `trial/`, `test_gold/`, `task6-submissions/` |
| `models/` | Downloaded models and resources (ignored): `nltk_data/`, `hf_cache/` |
| `overview/` | Notes, plans and the history of this workspace (`HISTORY.md`) |
| `team/` | Team repository `cocoac-ai/IHLT-MAI-2026-27-Labs` (separate git repo, ignored here) |

`data/`, `models/` and `slides/` are not tracked. `team/` keeps its own copy of the data it needs, in the flat layout of the team repository.

Notebooks use the folder above them as root (`ROOT = Path.cwd().parent`), so they run from `labs/` or `project/`. They run locally only (no Colab setup); when a lab is released to `team/`, its setup cell is adapted to the team layout (flat data folders, Colab).

One shared environment for my notebooks and the team ones: `pyproject.toml` + `uv.lock` → `.venv` (uv).

```bash
uv sync
```
