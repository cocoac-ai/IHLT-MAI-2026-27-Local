# STS Project: two-student plan

Updated: 2026-11-16

This is the team version of the IHLT STS project (SemEval 2012 Task 6). The notebook `project/sts-project.ipynb` is the full system (76 cells); it is split into one notebook per student, and built again from the two parts. This document says who owns what, what the two parts share, and how to work and present.

What the project asks: [project-outline.md](project-outline.md). Method, results and findings: [report.md](report.md).

Deliverables (to raco, before the oral presentation):

- `sts-[Student1]-[Student2].ipynb`: the notebook (rename `sts-project.ipynb`).
- `sts-[Student1]-[Student2].pdf`: the slides, exported as PDF (10 minutes).

## 1. Division of the work

The split follows the statement of the project: one student owns the **lexical dimension**, the data and the evaluation; the other owns the **syntactic dimension** and the **models**. Each student owns complete cells, from the code to the analysis text below it.

| Section of the notebook | Student 1: lexical dimension and evaluation | Student 2: syntactic dimension and models |
|---|---|---|
| 1. Setup and data | Loading, description of the five test sets | |
| 2. Evaluation | Official measures (ALL, ALLnrm, Mean), ranking of the 89 official runs | |
| 3. Preprocessing | NLTK: tokens, POS tags, lemmas, stopwords; the note on the lemmatizer | spaCy: dependency parse |
| 4. Features | 4.1: 24 lexical features (overlap, n-grams, TF-IDF, WordNet alignment, numbers, length) | 4.2: 21 syntactic features (POS, chunks, dependencies); 4.3: 14 lexico-syntactic features; the feature table `X` |
| 5. From measures to models | 5.1: each measure alone, plain averages | 5.2: cross-validation of the 24 configurations and selection; 5.3: noise of the cross-validation, hyperparameters; 5.4: leave one dataset out |
| 6. Test set | | Test results, ranking, bootstrap intervals, random seeds |
| 7. Analysis | 7.1: from a single measure to a learned model; 7.2: results by dataset; 7.5: error analysis | 7.3: single model or one per dataset, model for the surprise sets; 7.4: ablation, importance, syntax with and without dependencies |
| 8. Comparison with the participants | Methods of the papers | |
| Title and conclusions (9) | Shared | Shared |

Cells: 39 for student 1, 35 for student 2, 2 shared. Student 1 has more feature code and the reading of the results; student 2 has the modelling and most of the quantitative checks.

## 2. Interfaces

The two parts only meet through these objects. Do not change their form without telling the other student.

| Object | Owner | Contract |
|---|---|---|
| `data[(split, name)]` | Student 1 | `(pairs, gold)`: list of `[s1, s2]` and a numpy array; `split` in `{"train", "test"}`, `name` in `TRAIN_SETS` / `TEST_SETS` |
| `processed[(split, name)]` | Student 1 | list of `(tokens1, tokens2)`; each token is a dict with `word`, `lower`, `tag`, `pos`, `lemma`, `stop`, `punct` |
| `evaluate(predictions)` | Student 1 | `{test set: array}` → dict with `ALL`, `ALLnrm`, `Mean` and the Pearson of each test set |
| `official`, `baseline`, `read_submission` | Student 1 | DataFrame of the 89 official runs (rank as index); the baseline row; the predictions of one run |
| `jaccard`, `cosine`, `ngrams`, `content`, `word_similarity`, `idf` | Student 1 | helpers of 4.1, reused by the syntactic and lexico-syntactic features |
| `lexical_features(t1, t2)` | Student 1 | dict `{name: float}`; names get the prefix `lex:` |
| `single`, `scores`, `train_gold`, `UNSUPERVISED` | Student 1 | section 5.1: Pearson of each feature alone; ALL, ALLnrm and Mean for the training sets; the measures without learning |
| `parsed[(split, name)]` | Student 2 | list of `(doc1, doc2)`, the spaCy documents of each pair |
| `chunk`, `syntactic_features`, `dependency_features` | Student 2 | features with the prefix `syn:` |
| `lexico_syntactic_features`, `lexical_dependency_features` | Student 2 | features with the prefix `lexsyn:` |
| `X`, `y`, `FEATURE_GROUPS`, `ALL_FEATURES`, `DEPENDENCY_FEATURES` | Student 2 | feature DataFrames per dataset; groups `lexical`, `syntactic`, `combined` selected by prefix |
| `MODELS`, `cross_validate`, `cv_results`, `best_cv`, `SELECTED` | Student 2 | the models, the cross-validation and the selected configuration |
| `train_and_predict`, `test_results`, `test_predictions`, `SYSTEM`, `summary`, `official_rank` | Student 2 | test predictions of the 24 configurations and of the selected system; used by sections 7.1, 7.2 and 7.5 of student 1 |

Rules for both:

- **The test set is only used in section 6 and later.** Every choice (features, model, strategy, hyperparameters) is made with cross-validation on the training data.
- **No pre-trained embeddings, no data other than the task data.** NLTK for the lexical processing, the spaCy parser for the dependencies (to be confirmed with the lecturer, see `0-general/todo.md`).
- **Every number in the text is printed by a cell.** When the code changes, re-run the notebook and update the text and the slides.

## 3. Files and workflow

```
project/
  sts-project.ipynb               the final notebook: built from the two parts, do not edit it by hand
  sts-student1.ipynb              the cells of student 1 and the shared ones (title, conclusions)
  sts-student2.ipynb              the cells of student 2
  sts_parts.py                    split, merge, list, run_before
  STS Project Presentation.pptx   slides (not tracked in git)
```

Every cell carries its position and its owner in its metadata, so the two parts can always be put back in the right order.

| Command (run in `project/`) | What it does |
|---|---|
| `python sts_parts.py list` | Position, owner and first line of every cell |
| `python sts_parts.py merge` | Builds `sts-project.ipynb` from the two parts (cells keep the outputs they have) |
| `python sts_parts.py merge --run` | The same, then runs the whole notebook (about 5 minutes) and copies the new outputs back to the two parts |
| `python sts_parts.py split` | Writes the two parts again from `sts-project.ipynb` (only needed if the final notebook was edited directly) |

How to work:

1. **Each student edits only their own notebook.** A new cell needs nothing special: at merge time it is placed right after the cell above it.
2. **The cells of the two parts are interleaved**, so a part does not run from top to bottom by itself. To work on a cell, run the helper cell at the top of the part with the position of that cell, e.g. `run_before(30)`: it runs the code cells of both parts that come before it. The helper cells are not copied to the final notebook.
3. **To integrate**: pull the other student's part, run `python sts_parts.py merge --run`, read the result, commit the three notebooks together.
4. **Do not edit the same part at the same time in two places**: notebooks merge badly in git. With one part per student this only happens for the two shared cells (title and conclusions), which are in the part of student 1: student 2 sends the changes to student 1.
5. Before each integration, check that the interfaces of section 2 still hold (same names, same prefixes).

## 4. Schedule

The system is complete, so what is left is to make it the work of two people. The dates depend on the presentation day.

| Phase | Student 1 | Student 2 | Done when |
|---|---|---|---|
| 1. Take over | Reads their part and the report, runs it with `run_before` | The same | Each can explain every cell of their part |
| 2. Review | Reviews the part of student 2 (code and text) | Reviews the part of student 1 | Comments discussed; changes made by the owner |
| 3. Open points | Normalization of times and dates, if there is time (section 7.5) | Answer of the lecturer about the spaCy parser; if it is not allowed, remove the 10 dependency features and re-run | `merge --run` gives the final notebook |
| 4. Delivery | Slides of their part, names, rename | Slides of their part, export the PDF | Notebook re-run, PDF exported, talk rehearsed in 10 minutes |

## 5. Presentation (10 minutes, 12 slides)

| # | Slide | Speaker | Time |
|---|---|---|---|
| 1 | Title | Student 1 | 0:20 |
| 2 | The task and the evaluation | Student 1 | 0:50 |
| 3 | The data: five very different test sets | Student 1 | 0:50 |
| 4 | The system: from a sentence pair to a score | Student 2 | 0:50 |
| 5 | Three dimensions, 59 measures | Student 1 (lexical), Student 2 (syntactic and lexico-syntactic) | 1:00 |
| 6 | From a measure to a model, step by step | Student 1 | 1:00 |
| 7 | Model selection by cross-validation | Student 2 | 0:50 |
| 8 | Test results: at the level of the best official system | Student 2 | 1:00 |
| 9 | Results by test set | Student 1 | 0:50 |
| 10 | Analysis: what each dimension contributes | Student 2 | 1:00 |
| 11 | Error analysis | Student 1 | 0:50 |
| 12 | Conclusions | Both | 0:40 |

Each student speaks about 5 minutes. Every slide has speaker notes. Questions: each answers on their own part; the questions about the overall design are answered by both.

Questions to prepare:

- Why is the spaCy parser allowed if embeddings are not? (Student 2: the model has no word vectors; without it the result is 0.0038 lower and the conclusions are the same.)
- Is one model per dataset realistic? (Student 2: it mostly fixes the score level; ALLnrm and Mean hardly change. Section 7.3.)
- Are you better than the first system? (Both: no, the difference is not significant. Section 6.)
