# History of this workspace

Until 2026-11-10 all IHLT work lived in one repository, the team one (`cocoac-ai/IHLT-MAI-2026-27-Labs`), with my own work on local branches that were never pushed. On 2026-11-10 it was split in two:

- this repository (`cocoac-ai/IHLT-MAI-2026-27-Local`), only mine, started without history;
- the team repository, cloned in `team/`, unchanged.

The same day the team repository switched from `teamwork` to `main`: `main` was fast-forwarded to `teamwork` (`f651a1e`), made the default branch, and `teamwork` was deleted. Changes reach `main` only through pull requests (no approval needed); deleting `main` and force pushes are blocked.

The history of the old local branches was not kept: their content is in the files listed below, and the backup bundle was deleted on 2026-11-10. The team branches and the `labNN-submitted` tags are still in the team repository.

## Old branches

| Branch | Last commit | What it was | Where it is now |
|---|---|---|---|
| `main` | `14ff19b` 2026-10-19 | Team branch, frozen until the end of the course | fast-forwarded to `teamwork`, now the team branch in `team/` |
| `teamwork` | `f651a1e` 2026-11-06 | Shared team branch, one lab folder released at a time | merged into `main`, deleted |
| `local/main` | `995d25b` 2026-11-04 | All my own work: Lab01–Lab09, STS project, `common/` | `labs/Lab01.ipynb`–`Lab09.ipynb`, `project/sts-project.ipynb`, `common/`, `pyproject.toml`, `uv.lock` |
| `local/lab02-03-two-libs` | `3c2d137` 2026-11-01 | Lab02 and Lab03 with separate NLTK and spaCy pipelines, plus TextServer (tokenizer, morpho); last commit was WIP | `labs/Lab02-two-libs.ipynb`, `labs/Lab03-two-libs.ipynb`, `common/textserver_tokenizer.json` |
| `local/lab06-nltk-mfs` | `a274175` 2026-11-04 | Lab06 full study version: NLTK, spaCy and FreeLing pipelines, Lesk, MFS and UKB | `labs/Lab06-full.ipynb` |
| `local/lab07-sections` | `1c24253` 2026-11-05 | Lab07 experiments: NE types, feature combinations, FreeLing entities service (off) | `labs/Lab07-sections.ipynb` |
| `local/main-project-team` | `dfe6042` 2026-10-20 | STS project split between two students | `overview/project-two-student-plan.md`; its notebook only added the student owners to the section headings, so the single-student notebook of `local/main` was kept |

Changes made while moving the notebooks to `labs/`:

- the setup comment now says `labs/` instead of `labXX/`;
- `Lab02-two-libs` and `Lab03-two-libs` import `textserver` from `common/` and keep their credentials and TextServer caches there (before: the root and the lab folder);
- `Lab06-full` refers to the team repository `team/` instead of the `teamwork` branch.

Not carried over: the older copies of other labs inside the side branches (each side branch only changed its own lab), and `.gitkeep` files.

## Submitted versions

The submitted labs are tags in the team repository (`team/`):

| Tag | Commit |
|---|---|
| `lab01-submitted` | `637d30c` |
| `lab02-submitted` | `0036138` |
| `lab03-submitted` | `c580e9b` |
| `lab04-submitted` | `14ff19b` |
| `lab05-submitted` | `fa5a28d` |
| `lab06-submitted` | `5e8f0c1` |
| `lab07-submitted` | `1f23b8c` |

Known differences with the submitted versions: `labs/Lab06.ipynb` includes satellite adjectives in Lesk, which the submitted Lab06 does not.
