# STS project (SemEval 2012 Task 6)

The project notebook, split into one part per student. Each student edits their own part; a script puts the two parts together into the notebook that is delivered.

## Files

| File | What |
|---|---|
| `sts-student1.ipynb` | Part of student 1: data, evaluation, NLTK preprocessing, lexical features, measures without learning, results by dataset, error analysis, comparison with the papers. Also holds the two shared cells (title and conclusions) |
| `sts-student2.ipynb` | Part of student 2: spaCy dependency parse, syntactic and lexico-syntactic features, cross-validation and model selection, test results, training strategy, ablation |
| `sts-project.ipynb` | The final notebook, built from the two parts. **Do not edit it by hand**: the next merge overwrites it |
| `sts_parts.py` | The script that merges, splits and lists the cells |
| `STS Project Presentation.pptx` | The slides (12 slides, with speaker notes) |

To deliver: rename `sts-project.ipynb` to `sts-[Student1]-[Student2].ipynb`, and export the slides as `sts-[Student1]-[Student2].pdf`.

## Setup

The notebook expects this layout (the folder that contains `project/` is the root):

```
<root>/
  project/            this folder; run the notebooks and the script from here
  data/               train/, test_gold/, task6-submissions/ (downloaded by the notebook if missing)
  models/nltk_data/   NLTK resources (downloaded by the notebook)
```

Packages: `nltk`, `spacy`, `scikit-learn`, `pandas`, `numpy`, `scipy`, `matplotlib`, `jupyter`. The spaCy model is not downloaded by the notebook:

```
python -m spacy download en_core_web_sm
```

## Who owns what

| Section of the notebook | Student 1 | Student 2 |
|---|---|---|
| 1. Setup and data | all | |
| 2. Evaluation and official results | all | |
| 3. Preprocessing | NLTK; the note on the lemmatizer | spaCy dependency parse |
| 4. Features | 4.1 lexical (24) | 4.2 syntactic (21); 4.3 lexico-syntactic (14); the feature table `X` |
| 5. From measures to models | 5.1 measures without learning | 5.2 cross-validation and selection; 5.3 noise and hyperparameters; 5.4 leave one dataset out |
| 6. Test set | | all |
| 7. Analysis | 7.1 from a measure to a model; 7.2 by dataset; 7.5 errors | 7.3 training strategy; 7.4 which features matter |
| 8. Comparison with the participants | all | |
| Title, 9. Conclusions | shared (kept in the part of student 1) | shared |

39 cells for student 1, 35 for student 2, 2 shared.

## Commands

Run them in `project/`.

| Command | What it does |
|---|---|
| `python sts_parts.py list` | Shows the position, the owner and the first line of every cell |
| `python sts_parts.py merge` | Builds `sts-project.ipynb` from the two parts. Nothing is run: the cells keep the outputs they have |
| `python sts_parts.py merge --run` | Builds it, runs the whole notebook (about 5 minutes), and copies the new outputs back to the two parts |
| `python sts_parts.py split` | Writes the two parts again from `sts-project.ipynb`. Only needed if the final notebook was edited directly |

## How to work

**1. Edit only your own part.** Open `sts-student1.ipynb` or `sts-student2.ipynb`, not the final notebook.

**2. A part does not run from top to bottom by itself.** The cells of the two students are interleaved: for example, the error analysis of student 1 needs the models trained by student 2. To work on one cell:

1. Find its position with `python sts_parts.py list`.
2. In the helper cell at the top of your part, call `run_before` with that position and run it:

   ```python
   from sts_parts import run_before
   run_before(30)   # runs the code cells of both parts that come before position 30
   ```

3. Now run and edit your cell as usual.

`run_before` reads the two parts from disk, so save your notebook first if you changed an earlier cell. The helper cells are not copied to the final notebook.

**3. Adding a cell.** Just add it where it belongs in your part. At merge time it is placed right after the cell above it, and it belongs to the part where it was written. The positions shown by `list` are renumbered after each merge.

**4. Integrating.**

1. Get the latest version of the other student's part (`git pull`).
2. `python sts_parts.py merge --run`
3. Read the final notebook: the text must still match the numbers printed by the cells.
4. Commit the three notebooks together.

**5. Avoiding conflicts.** Notebooks merge badly in git, so never change the other student's part: ask them. The two shared cells (title and conclusions) are in the part of student 1; student 2 sends their changes to student 1.

## Rules of the project

- **The test set is used only in section 6 and later.** Every choice (features, model, strategy, hyperparameters) is made with cross-validation on the training data.
- **No pre-trained word or sentence embeddings, and no data other than the task data.** NLTK and WordNet for the lexical processing; the spaCy parser (`en_core_web_sm`, a model without word vectors) for the dependencies.
- **Every number in the text is printed by a cell.** After changing code, run `merge --run` and update the text and the slides.

## What the two parts share

A change to one of these objects affects the other part: tell the other student first.

| Defined by student 1 | Used by student 2 for |
|---|---|
| `data`, `processed` | all the features |
| `evaluate`, `official`, `baseline`, `read_submission` | test results, ranking, bootstrap |
| `jaccard`, `cosine`, `ngrams`, `content`, `word_similarity`, `idf` | syntactic and lexico-syntactic features |
| `lexical_features` (prefix `lex:`) | the feature table `X` |
| `scores`, `train_gold`, `single` | cross-validation, selection of the measures |

| Defined by student 2 | Used by student 1 for |
|---|---|
| `X`, `y`, `FEATURE_GROUPS` | measures without learning (5.1), error analysis (7.5) |
| `test_results`, `test_predictions`, `SYSTEM`, `summary`, `official_rank` | sections 7.1, 7.2 and 7.5 |

## Current result

Selected by cross-validation: 59 features, random forest, one model per dataset.

| | ALL | ALLnrm | Mean |
|---|---|---|---|
| Ours (test set) | 0.8263 | 0.8654 | 0.6946 |
| Best official run | 0.8239 | 0.8635 | 0.6773 |

The difference with the best official run (UKP) is not significant (95% interval of the difference: [-0.0077, 0.0122]), so the result is "at the level of the best system", not "first".
