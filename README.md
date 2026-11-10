# IHLT-MAI-2026-27-Local

Ran's own workspace for the UPC MAI course *Introduction to Human Language Technologies* (2026-27).

| Folder | What |
|---|---|
| `labs/` | My lab notebooks, `Lab01`–`Lab09`, plus the study and experimental versions (`Lab02-two-libs`, `Lab03-two-libs`, `Lab06-full`, `Lab07-sections`) |
| `project/` | My STS project notebook (SemEval 2012 Task 6) |
| `common/` | Shared code and caches: TextServer client, UKB and TextServer answers, `credentials.json` (ignored) |
| `overview/` | Notes, plans and the history of this workspace (`HISTORY.md`) |
| `team/` | Team repository `cocoac-ai/IHLT-MAI-2026-27` (separate git repo, ignored here) |

Data folders in the root are not tracked: `train/`, `trial/`, `test_gold/`, `task6-submissions/`, `nltk_data/`, `hf_cache/`, `slides/`. `team/` keeps its own copy of the data it needs.

Notebooks use the folder above them as root (`ROOT = Path.cwd().parent`), so they run from `labs/` or `project/`; on Colab the root is `Colab Notebooks/ihlt` in Google Drive.

One shared environment for my notebooks and the team ones: `pyproject.toml` + `uv.lock` → `.venv` (uv).

```bash
uv sync
```
