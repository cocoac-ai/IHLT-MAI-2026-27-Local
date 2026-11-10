# STS Project: two-student plan

This is the team version of the IHLT STS project (SemEval 2012 Task 6). The notebook `sts-project.ipynb` is the full system; this document splits it between the two students, fixes the interfaces between their parts, and plans the work and the presentation.

Deliverables (to raco, before the oral presentation):

- `sts-[Student1]-[Student2].ipynb`: the notebook (rename `sts-project.ipynb`).
- `sts-[Student1]-[Student2].pdf`: the slides, exported as PDF (10 minutes).

## 1. Division of the work

The split follows the statement of the project: one student owns the **lexical dimension** and the evaluation framework, the other the **syntactic dimension** and the models that combine both. Each student owns complete sections of the notebook, from the code to the analysis text.

| | Student 1: lexical dimension and evaluation | Student 2: syntactic dimension and modelling |
|---|---|---|
| Data and evaluation | Loading of train and test sets; official measures (ALL, ALLnrm, Mean); official ranking from the submissions (sections 1, 2) | |
| Preprocessing | NLTK pipeline: tokens, POS tags, lemmas, stopwords (section 3) | |
| Features | 23 lexical features: overlap, n-grams, TF-IDF, WordNet alignment, numbers, length (4.1) | 16 syntactic features: POS n-grams, chunks (4.2); 9 lexico-syntactic features (4.3) |
| Models | | Cross-validation, SVR / RF / GBR, single vs per-dataset strategy (5); final test run (6) |
| Analysis | Results by dataset vs the best systems (7.1); error analysis (7.4) | Training strategy and calibration (7.2); ablation and feature importance (7.3) |
| Presentation | Slides 1–3, 5 (lexical part), 9, 11 | Slides 4, 5 (syntactic part), 6–8, 10 |
| Together | Conclusions (8), review of the whole notebook, rehearsal | |

The load is balanced: Student 1 has more feature code (WordNet is the largest part), Student 2 has the modelling and most of the quantitative analysis.

## 2. Interfaces

The two parts only meet through these objects. Agree on them first (day 1) and do not change them without telling the other student.

| Object | Owner | Contract |
|---|---|---|
| `data[(split, name)]` | Student 1 | `(pairs, gold)`: list of `[s1, s2]` and a numpy array; `split` in `{"train", "test"}`, `name` in `TRAIN_SETS` / `TEST_SETS` |
| `processed[(split, name)]` | Student 1 | list of `(tokens1, tokens2)`; each token is a dict with `word`, `lower`, `tag`, `pos`, `lemma`, `stop`, `punct` |
| `evaluate(predictions)` | Student 1 | `{test set: array}` → dict with `ALL`, `ALLnrm`, `Mean` and the Pearson of each test set |
| `official` | Student 1 | DataFrame of the 89 official runs (rank as index) |
| `lexical_features(t1, t2)` | Student 1 | dict `{name: float}`; names get the prefix `lex:` |
| `syntactic_features(t1, t2, chunks1, chunks2)` | Student 2 | dict, prefix `syn:` |
| `lexico_syntactic_features(t1, t2, chunks1, chunks2)` | Student 2 | dict, prefix `lexsyn:` |
| `X`, `y`, `FEATURE_GROUPS` | Student 2 | feature DataFrames per dataset; groups `lexical`, `syntactic`, `combined` selected by prefix |

Rules for both:

- **The test set is only used in section 6 and later.** Every choice (features, model, strategy, parameters) is made with cross-validation on the training data.
- **Only NLTK** for the linguistic processing, no pre-trained embeddings, no data other than the task data.
- **Every number in the text is printed by a cell** of the notebook. When the code changes, re-run the notebook and update the text.

## 3. Repository and workflow

```
IHLT/
├── train/ test_gold/ trial/ task6-submissions/   # task data (git-ignored, downloaded by the notebook)
├── nltk_data/                                    # NLTK resources (git-ignored)
└── project/
    ├── PLAN.md                                   # this plan
    ├── sts-project.ipynb                         # final notebook
    └── drafts/                                   # optional: one draft notebook per student
```

Notebooks merge badly in git, so:

1. Each student develops in their own branch (`project-lexical`, `project-syntax`) and, if needed, in their own draft notebook under `project/drafts/`.
2. Only the owner of a section edits it in `sts-project.ipynb`. Changes to another student's section go through them.
3. Integration: merge into `project-sts-team`, then **Restart & Run All** and commit the executed notebook. The whole notebook runs in about 2 minutes.
4. Before each merge, check that the interfaces of section 2 still hold (same keys, same prefixes).

## 4. Schedule

The dates depend on the presentation day; the plan is in four phases.

| Phase | Student 1 | Student 2 | Done when |
|---|---|---|---|
| 1. Base (days 1–2) | Data loading, official measures, check of the baseline (0.3110) and 10th run (0.7562); preprocessing | First syntactic features on the preprocessed data; CV framework with a simple model | Both can compute features on all pairs |
| 2. Features (days 3–6) | Lexical features, WordNet alignment | Syntactic and lexico-syntactic features | `X` has the three groups |
| 3. Models and analysis (days 7–9) | Results by dataset, error analysis | Model selection, test run, strategy, ablation, importance | All sections have their analysis text |
| 4. Delivery (days 10–12) | Slides of their part | Slides of their part | Notebook re-run, PDF exported, talk rehearsed in 10 minutes |

Optional extensions, one per student, if there is time:

- Student 1: normalize numbers, dates and times (e.g. `5.30 p.m.` / `17h30`), and align multiword expressions with WordNet.
- Student 2: tune the hyperparameters with cross-validation, or a deeper syntactic analysis (e.g. dependency-like relations from the chunks).

## 5. Presentation (10 minutes, 12 slides)

| # | Slide | Speaker | Time |
|---|---|---|---|
| 1 | Title | Student 1 | 0:20 |
| 2 | The task and evaluation | Student 1 | 0:50 |
| 3 | The data: five different test sets | Student 1 | 0:50 |
| 4 | The pipeline | Student 2 | 0:50 |
| 5 | Three dimensions, 48 features | Student 1 (lexical), Student 2 (syntactic and lexico-syntactic) | 1:10 |
| 6 | Model selection by cross-validation | Student 2 | 0:50 |
| 7 | Test results: 2nd of 89 | Student 2 | 0:50 |
| 8 | Comparison with the official ranking | Student 2 | 0:40 |
| 9 | Results by test set | Student 1 | 0:50 |
| 10 | Analysis: what each dimension contributes | Student 2 | 1:00 |
| 11 | Error analysis | Student 1 | 0:50 |
| 12 | Conclusions | Both | 0:50 |

Each student speaks about 5 minutes. Questions: each answers on their own part; the questions about the overall design are answered by both.
