# To do

State on 2026-11-15. What is left, by topic. Items marked *decided* are not to be done; they are listed so they are not reopened by mistake.

## General

- [ ] After the course: decide whether to delete the local clone `team/` and keep only this repository (the team repository stays on GitHub with the `labNN-submitted` tags).
- *Decided:* no more TextServer queries (daily quota, see [labs/textserver.md](labs/textserver.md)). The code stays in the notebooks, switched off.

## Labs

All nine notebooks in `labs/` are complete and fully executed (every code cell has run).

| Lab | Local state | Left to do |
|---|---|---|
| Lab01 | Done | — |
| Lab02 | Done: NLTK and spaCy; TextServer tokenizer off | — (*decided:* the TextServer outputs and text are not updated) |
| Lab03 | Done: NLTK and spaCy; TextServer `morpho` off | — (*decided:* same as Lab02) |
| Lab04 | Done: HMM, TnT, perceptron, CRF, learning curves | — |
| Lab05 | Done | — |
| Lab06 | Done: complete study version (3 pipelines, Lesk / MFS / UKB, satellite fix) | — (the two fixes of 2026-10-29 are applied here; the submitted version stays unfixed) |
| Lab07 | Done: NLTK, spaCy, FreeLing; ex1, ex2 | — (*decided:* `entities` service off, FreeLing NEs from the Lab 6 cache) |
| Lab08 | Done: three chart parsers | [ ] Not submitted yet: `team/lab08/` is empty |
| Lab09 | Done: fastcoref on *Alice* | [ ] Not submitted yet: `team/lab09/` is empty |

## Project (STS, SemEval 2012 Task 6)

The notebook `project/sts-project.ipynb` is complete and executed (ALL 0.8217, 2nd of 89; Mean 0.6937, 1st). A 12-slide draft exists in `slides/projects/STS Project Presentation.pptx` (not tracked, last changed 2026-10-18).

- [ ] Decide the authors: alone, or split with a teammate following [project/two-student-plan.md](project/two-student-plan.md).
- [ ] Fill in the student names (first cell of the notebook, title slide).
- [ ] Check that every number on the slides still matches the notebook output (the slides are older than the last notebook run).
- [ ] Restart & Run All, then rename to `sts-[Student1]-[Student2].ipynb`.
- [ ] Export the slides as `sts-[Student1]-[Student2].pdf`.
- [ ] Rehearse the talk in 10 minutes.
- [ ] Upload the notebook and the PDF to raco before the oral presentation.
- [ ] Optional extensions (from the conclusions): normalize numbers, dates and times; align multiword expressions with WordNet; tune the hyperparameters with cross-validation. Each one needs a re-run and updated text and slides.
- [ ] If the two-student plan is used: its section 3 (repository and workflow) still shows the old layout (data at the root, `project/PLAN.md`, `project-sts-team` branch); update it to the layout of the repository where the work is done.
