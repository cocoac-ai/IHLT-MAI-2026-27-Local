# Local vs. team: differences

- Team repo: `IHLT-MAI-2026-27-Labs`, cloned in `team/` (labs and project, so this file is in `0-general/`)
- Local: this repository (`IHLT-MAI-2026-27-Local`)
- Compared versions: team `labNN-submitted` tags, local `main`, 2026-11-15

This repository (`IHLT-MAI-2026-27-Local`) is my own study version; the team repository (`IHLT-MAI-2026-27-Labs`, cloned in `team/`) holds what was submitted. The local labs compare the tools (NLTK, spaCy, FreeLing/TextServer) instead of using only the one of the submission. State on 2026-11-15; the submitted versions are the `labNN-submitted` tags of the team repository.

## 1. General

| | Local (this repository) | Team (`team/`) |
|---|---|---|
| Layout | `labs/LabNN.ipynb`, `project/`, `common/`, `overview/` | one folder per lab, `labNN/LabNN.ipynb`, plus `common/`, `project/` |
| Data | `data/` (`train/`, `trial/`, `test_gold/`, `task6-submissions/`) | `test_gold/` only, at the root |
| Models | `models/nltk_data/`, `models/hf_cache/` | `nltk_data/` at the root, no Hugging Face cache |
| Setup cell | local only: `ROOT = Path.cwd().parent`, paths under `data/` and `models/` | Colab block (`%pip install`, Drive `Colab Notebooks/ihlt` or `/content`) and local fallback, flat paths |
| Environment | `pyproject.toml` also has `datasets`, `fastcoref`, `transformers`, `matplotlib`, `python-crfsuite`, `scikit-learn` (needed by Lab04, Lab09 and the project) | smaller `pyproject.toml` without them |
| TextServer | `common/textserver.py`, caches in `common/` (`ukb_senses.json`, `textserver_tokenizer.json`) | `common/textserver.py`; the UKB cache is in `lab06/` |
| Git | branch `main`, commit directly | branch `main`, changes only through pull requests; `labNN-submitted` tags |

## 2. Labs

| Lab | Local | Team (submitted) |
|---|---|---|
| Lab01 | same notebook | same; only the setup cell differs |
| Lab02 | NLTK **and** spaCy tokenizers, kept as separate pipelines; sections (Jaccard, Pearson, score distribution, examples, tokenizer comparison); TextServer tokenizer code, off | NLTK only, 8 cells |
| Lab03 | separate NLTK and spaCy pipelines (words and lemmas always from the same library); sections on pairs with the largest changes, POS tags and lemmas, lemmas and meaning; TextServer `morpho` code, off | NLTK and spaCy lemmatizers, no sections, 14 cells; spaCy lemmas 0.4784 vs words 0.4507 |
| Lab04 | rewritten: 24 models (4 taggers × 6 training sizes), fixed perceptron seed, timings, learning curves, written answer with section headings | the teammate's version: same experiment, short code, answer: perceptron on 3000 sentences (~95.9 %) |
| Lab05 | same notebook | same; only the setup cell differs |
| Lab06 | complete study version: NLTK, spaCy and FreeLing pipelines; Lesk, MFS and UKB; satellite adjectives included in Lesk (`synsets=wn.synsets(word, pos)`); Lesk senses 0.4406; "Notes" section with the design decisions | spaCy only, Lesk and UKB, without the satellite fix: Lesk senses 0.4467 |
| Lab07 | NEs from NLTK (`ne_chunk`), spaCy and FreeLing (NP tags of the Lab 6 cache); ex1 and ex2; `entities` service code, off | spaCy only, ex1 and ex2 |
| Lab08 | done | not submitted (`lab08/` empty) |
| Lab09 | done (fastcoref) | not submitted (`lab09/` empty) |

## 3. Project

| | Local | Team |
|---|---|---|
| Notebook | `project/sts-project.ipynb`, complete and executed, one author (student names blank) | `project/` empty |
| Split between two students | plan in [project/two-student-plan.md](../2-project/two-student-plan.md) (not applied to the notebook) | — |
| Slides | draft `slides/projects/STS Project Presentation.pptx` (not tracked) | — |
| Running it | needs `data/train/`, `data/test_gold/`, `data/task6-submissions/` and `scikit-learn` | would need the training data, the official submissions and the extra packages first |

## To take from the team / to port

- From team → local:
- From local → team:
