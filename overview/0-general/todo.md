# 待办和现状

更新：2026-11-16

## 现在做什么

1. **决定 STS 项目的作者**：一个人，还是按 [two-student-plan.md](../2-project/two-student-plan.md) 和队友分。定了以后填名字（notebook 第一格、标题页）。
2. **核对幻灯片**：幻灯片比 notebook 最后一次运行要早，逐个数字对一遍；然后 Restart & Run All，按 `sts-[Student1]-[Student2]` 改名，导出 PDF。
3. **Lab08、Lab09**：本地已完成，团队仓库 `team/lab08/`、`team/lab09/` 还是空的，没交。交之前按下面"交之前检查"的五条过一遍（Lab01–07 丢分的共同原因）。

## 截止日期

| 什么 | 哪天 |
|---|---|
| STS 项目口头报告（10 分钟，notebook + PDF 先传到 raco） | 待补 |
| Lab08、Lab09 提交 | 待补 |

## 等别人

| 等谁 | 等什么 | 等到了以后我做什么 |
|---|---|---|
| （暂无） | | |

## 各部分现状（原来的 To do 清单，英文）

State on 2026-11-15. What is left, by topic. Items marked *decided* are not to be done; they are listed so they are not reopened by mistake.

### General

- [ ] After the course: decide whether to delete the local clone `team/` and keep only this repository (the team repository stays on GitHub with the `labNN-submitted` tags).
- *Decided:* no more TextServer queries (daily quota, see [labs/textserver.md](../1-labs/textserver.md)). The code stays in the notebooks, switched off.

### Labs

All nine notebooks in `labs/` are complete and fully executed (every code cell has run). "Left to do" below is only what is needed for the lab itself; the other tools still to add are in the next section.

| Lab | Local state | Left to do |
|---|---|---|
| Lab01 | Done | — |
| Lab02 | Done: NLTK and spaCy; TextServer tokenizer off | — (*decided:* the TextServer outputs and text are not updated) |
| Lab03 | Done: NLTK and spaCy; TextServer `morpho` off | — (*decided:* same as Lab02) |
| Lab04 | Done: HMM, TnT, perceptron, CRF, learning curves | — |
| Lab05 | Done | — |
| Lab06 | Done: complete study version (3 pipelines, Lesk / MFS / UKB, satellite fix) | — (the two fixes of 2026-10-29 are applied here; the submitted version stays unfixed) |
| Lab07 | Done: NLTK, spaCy, FreeLing; ex1, ex2 | Three optional additions, not started (see the Lab07 note below). (*decided:* `entities` service off, FreeLing NEs from the Lab 6 cache). Submitted version graded 9,0: see the notes below the table |
| Lab08 | Done: three chart parsers | [ ] Not submitted yet: `team/lab08/` is empty |
| Lab09 | Done: fastcoref on *Alice* | [ ] Not submitted yet: `team/lab09/` is empty |

#### 每个 lab 的工具：做了哪些，还能加哪些（2026-11-16）

目标：`labs/` 里每个 lab 一个 notebook，把课件（`slides/labs/`）里给的工具都实现一遍并比较。下面是对照课件和本地 notebook 的代码列出来的；"还能加"的都**还没开始**，都不是题目要求的。

| Lab | 课件里的工具 | 本地已有 | 还能加 |
|---|---|---|---|
| Lab01 | NLTK（语料、停用词）；课件提到 spaCy、FreeLing 但这一题只用 NLTK | NLTK | [ ] spaCy 的分词和停用词表，对比前 25 个词（`o'er`、`thee` 会不会不同） |
| Lab02 | 分词：NLTK、spaCy、TextServer；度量：Jaccard、Dice、Overlap、Cosine | NLTK、spaCy；只有 Jaccard；TextServer 关着 | [ ] FreeLing 的词，从缓存取（见下）<br>[ ] Dice、Overlap、Cosine 三个度量 |
| Lab03 | NLTK（`pos_tag` + WordNet lemmatizer）、spaCy、TextServer `morpho` | NLTK、spaCy；TextServer 关着 | [ ] FreeLing 的 lemma 和 POS，从缓存取（见下） |
| Lab04 | HMM（MLE 和 Lidstone 两种）、TnT、perceptron、CRF；列表里还有 Brill | HMM（只有默认的 Lidstone）、TnT、perceptron、CRF，带时间和未登录词 | [ ] HMM 的 MLE 版，对比 smoothing 的作用<br>[ ] Brill（课件只列了名字，没有代码） |
| Lab05 | NLTK WordNet：Path、Leacock-Chodorow、Wu-Palmer、Lin；SentiWordNet（课件有，题目没用） | 四个相似度都有 | [ ] 可选：SentiWordNet 的分数。只有 NLTK 一个工具，没有可比的库 |
| Lab06 | NLTK Lesk、TextServer UKB | Lesk、MFS、UKB（缓存），三条流水线 | —（齐了） |
| Lab07 | NERC：NLTK `ne_chunk`、spaCy、TextServer `entities` | NLTK、spaCy、FreeLing（缓存里的 NP 标签）；`entities` 服务关着 | 工具齐了；剩下的是 Lab07 一节的三条可选 |
| Lab08 | 非概率：BottomUp、BottomUpLeftCorner、LeftCorner、TopDown、Earley；概率：InsideChart、Random、Longest、Viterbi（含从 Treebank 归纳 PCFG）、CoreNLP；依存：spaCy、TextServer | 题目要求的三个：BottomUp、BottomUpLeftCorner、LeftCorner | [ ] TopDown、Earley，同一句话比边数<br>[ ] 概率的：InsideChart、Viterbi<br>[ ] spaCy 的依存分析<br>不做：CoreNLP（要另装 Java 服务）、TextServer 依存（不再请求） |
| Lab09 | spacy-experimental、coreferee、crosslingual-coreference、TextServer `coreferences`；题目只要一个 | fastcoref（课件之外的；notebook 里写了 spacy-experimental 和 coreferee 不支持这里的 spaCy 3.8） | [ ] crosslingual-coreference：先确认能不能装上<br>[ ] spacy-experimental、coreferee：要另建一个旧版 spaCy 的环境才行，值不值得再定<br>不做：TextServer |

**FreeLing 不用再请求 TextServer。** `common/ukb_senses.json`（Lab 6 存下的 `senses` 服务的回答，338 个句子，Lab06、Lab07 用的就是它）每个词是 `[form, lemma, tag, POS, synset]`，所以 Lab02 要的词、Lab03 要的 lemma 和 POS 都在里面。注意：NE 的几个词用 `_` 连成一个（`Van_Orden`），和 NLTK、spaCy 的分词不一样，比较时要说明。`common/textserver_tokenizer.json` 只有 50 个句子，不够用。

建议的先后：先做交之前可能用得上的（Lab08、Lab09 还没交），再做有缓存、不用装东西的（Lab02、Lab03 的 FreeLing，Lab02 的度量），最后才是要装环境的（Lab09 的另外几个）。

#### 成绩（Lab01–07）和没满分的原因（2026-11-16）

成绩单 `grades.pdf` 只有分数，没有评语。下面每个 lab 的原因都是对照题目（`slides/labs/`）和**提交版**的推断，没有核实；要确认只能问老师。

提交版以团队仓库的标签 `labNN-submitted` 为准。**Lab01、Lab02 的提交版和 `team/` 里现在的文件不一样**（提交之后在 `improve-lab01-02` 分支上加了分析），要看提交版用 `git -C team show lab01-submitted:Lab01/Lab01.ipynb`（Lab02 同理，路径 `Lab02/Lab02.ipynb`）。Lab04、Lab07 的标签和现在的文件相同。

| | Lab01 | Lab02 | Lab03 | Lab04 | Lab05 | Lab06 | Lab07 |
|---|---|---|---|---|---|---|---|
| 我们 | 8,1 | 8,2 | 10,0 | 9,0 | 10,0 | 10,0 | 9,0 |
| 全班平均 | 8,14 | 8,92 | 9,34 | 9,44 | 9,16 | 8,93 | 8,74 |
| 全班最高 | 9,2 | 10,0 | 10,0 | 10,0 | 10,0 | 10,0 | 10,0 |
| 最常见的分 | 9,1（14 行） | 9,2（12 行） | 10,0（27 行） | 9,5（26 行） | 10,0（16 行） | 10,0（22 行） | 10,0（14 行） |
| 比我们高 / 同分 / 比我们低（行） | 28 / 4 / 14 | 34 / 4 / 8 | 0 / 27 / 21 | 36 / 10 / 2 | 0 / 16 / 31 | 0 / 22 / 25 | 16 / 8 / 23 |

（成绩单按人一行，同组两人各一行，所以"行"大约是组数的两倍。）

怎么读这张表：

- **相对全班最差的是 Lab04 和 Lab02**，不是 Lab07。Lab04 的 9,0 在 48 行里只高于 2 行；Lab02 的 8,2 只高于 8 行。
- Lab01 没有人拿 10（最高 9,2），所以 8,1 实际上只比常见分低 1 分。
- Lab01、Lab02 我们都**正好比最常见的分低 1,0**（9,1 → 8,1，9,2 → 8,2）。看起来像"标准答案的分减去一项"，但这只是从数字上看出来的，不知道减的是什么。
- Lab06 是 10,0，提交版没有 satellite 的修正，说明那个问题没有被扣分。

四个 lab 丢分的共同点：**答案本身都对，丢的是分析**。由此得到的检查表：

**交之前检查**（Lab08、Lab09 和项目都适用）：

1. 题目的每一步都有对应的格，特别是 "justify"、"discuss" 这类文字要求（Lab02 漏了第 4 步）。
2. 有 markdown：标题、每一步在做什么、结论（Lab01、Lab02 是裸代码）。
3. 输出里不正常的结果要指出并解释，能修就修（Lab01 的 `er`，Lab07 的 `Report` / `report`）。
4. 每句论断都有一个格打印出来的数字支持（Lab04 的 smoothing 和特征；Lab07 的 `types_only`）。
5. 选择或结论不只看一个指标，实验要能回答问题（Lab04 只看准确率；Lab07 的 ex2 没有信息量）。

**本地版的现状**：Lab01、Lab02、Lab04 的丢分点在 `labs/` 里已经补上；Lab07 还有三条可选的（见 Lab07 一节）。除此之外要加的是别的工具，见上面"每个 lab 的工具"一节。

##### Lab01（8,1）

题目：显示 `blake-poems.txt` 里出现最多的 25 个非停用词。

提交版只有 6 个代码格，没有 markdown。这是第一个 lab，当时不知道除了答案还要考虑什么。可能的原因：

1. **没有任何文字。** 没有标题、说明和对结果的讨论，结果是 `most_common(25)` 的原始输出。
2. **结果里有明显的问题，没有处理也没有指出。** `er`（16 次）不是词，是 `o'er` 被 `gutenberg.words()` 切开的碎片；`thee`、`thou`、`thy` 排在第 2、4、5 位，是古英语的代词，NLTK 的停用词表没有。
3. **第 25 名是并列的。** 16 次的词有 8 个，只有 5 个进了前 25，取哪几个是任意的，没有提。

本地版 `labs/Lab01.ipynb` 三条都已补上（古英语形式、`er`、并列，以及扩展停用词表后的前 25）。没有要做的。

##### Lab02（8,2）

题目四步：读 *SMTeuroparl* 的句对；用词和 Jaccard 算相似度；和 gold standard 算 Pearson；**4. Justify the answer**。

提交版只有 4 个代码格，输出只有一行 `Pearson correlation: 0.4507`。和 Lab01 一样是刚开始做的时候交的。可能的原因：

1. **第 4 步完全没做（最可能）。** 没有任何 justification：没有解释 0.45 说明什么，没有例子，没有说为什么词的重叠只能部分反映语义相似度。这是题目明确要求而提交版缺失的。
2. **没有 markdown**，没有展示相似度向量（题目第 2 步说"a vector of similarities"），只算了没显示。
3. 没有讨论预处理（大小写、标点、停用词都原样保留）。这一条题目没有要求，可能性低。

本地版 `labs/Lab02.ipynb` 已补上：Justification、分数分布、不一致的例子、NLTK 和 spaCy 分词器的对比。没有要做的。

##### Lab04（9,0）

题目：在 Treebank 上用前 500–3000 句训练 HMM、TnT、perceptron、CRF，用第 3001 句以后评估这 24 个模型；画四条学习曲线；**选哪个模型，说明理由**。

提交版是队友写的，不是我写的。代码、表和图都对，切分也对（`sentences[3000:]`）。最常见的分是 9,5，我们 9,0，所以大概是论证部分丢了分。可能的原因：

1. **选模型只看准确率（最可能）。** 没有量训练时间和标注时间，没有讨论代价。"选哪个模型"通常要权衡准确率和效率（TnT 训练最快，CRF 最慢）。
2. **有几句论断没有代码支持。**
   - "perceptron 能用后缀、大小写等词级特征"：CRF 也用这些特征，所以这解释不了 perceptron 为什么比 CRF 高；也没有量未登录词上的准确率。
   - "HMM 用了 smoothing 还是最低"：代码里没有设 smoothing，用的是 NLTK 的默认值，文中没有说明。
   - "曲线逐渐变平"：对 HMM 不成立，它到 3000 句还在明显上升（0.8865 → 0.8984）。
3. **只有一段文字，没有分点**；标题是纯文本（`Part of Speech`、`Model Selection and Justification` 没有 `#`），中间有一个空的 markdown 格，输出里有个人路径。排版问题，可能性低。

本地版 `labs/Lab04.ipynb` 已补上第 1、2 条：有训练和标注时间、未登录词上的准确率（HMM 只有 0.3586）、每个模型的评价，以及"只有一次切分，三者差距小"的保留。没有要做的。

##### Lab07（9,0）

对照题目（`slides/labs/07-Word-Sequences.pdf` 第 10 页）和提交版 `team/lab07/Lab07.ipynb`。

队友转述：ex2–ex4 **选一个**做（没有直接向老师核实）。提交版做了 ex2，所以"没做 ex3 / ex4"应该不是扣分原因。我自己的判断：大概率是**分析不够**，和下面第 1、2 条一致。剩下的可能，按可能性排：

1. **ex2 的实验没有产生信息。** `NE:TYPE` 只是给同一个字符串加后缀，Jaccard 下不可能产生新匹配：12 对变化，全部下降，Pearson 只差 0.0013（0.4351 → 0.4364）。报告指出了这一点，但没有再往前一步：`types_only`（用类型替换 NE）只在两个自造句子上演示，没有在 459 对上算 Pearson。
2. **所有带 NE 的表示都没超过基线。** 最好的是纯 lemmas（0.4784）；`lemmas + NEs (added)` 是 0.4765。结论等于"NE 没用"。
3. **自己发现的问题没有修。** pair 393 里 `Report` / `report` 因大小写不匹配，NE 的识别也因此不一致，没有试小写化或去标点。
4. **提交版只用了一个最小的 NER 模型。** `en_core_web_sm` 把 `A5-0323/2000` 标成 DATE、`Maij-Weggen` 标成 ORG；讨论把原因归到识别不稳定，但没有换工具验证。

9 分不是"常规高分"：Lab07 有分的 47 行里，14 行是 10,0，2 行 9,5，8 行 9,0，其余 23 行在 7,1–8,5。所以确实有一个具体的扣分点。

**ex2 和 ex3 / ex4 的区别**（"Jaccard 只比字符串，所以都没收益"只对 ex2 成立）：

| | 做了什么 | Jaccard 下能否产生新匹配 |
|---|---|---|
| ex2 `John:PERSON` | 同一个字符串加后缀 | 不能，只会不变或变低 |
| ex3 `is:WORD, be:LEMMA` | 集合里多了 lemma（词 ∪ lemma） | 能：`is` 和 `was` 通过 `be:LEMMA` 匹配 |
| ex4 `be:0235236-v` | 词换成 synset 编号 | 能：同义词编号相同；但依赖 WSD，消歧错了会变低 |

提交版自己的数字就是证据：lemmas 0.4784 高于 words 0.4606，都是 Jaccard 比字符串，只是字符串换成了归一化后的形式。ex3 / ex4 在 *SMTeuroparl* 上是否真有收益没有跑过。

本地版 `labs/Lab07.ipynb` 的情况：第 4 条已补上（NLTK、spaCy、FreeLing 三个工具）；第 1、3 条没补（`types_only` 仍只是演示，没有小写化），也没有 ex3 / ex4。可选的补充，都不是必须：

- [ ] 可选：`types_only` 在 459 对上算 Pearson。
- [ ] 可选：小写化、去标点后重算 ex1。
- [ ] 可选：ex4，synset 用 Lab 6 的缓存（`common/ukb_senses.json`），不需要再请求 TextServer。

### Project (STS, SemEval 2012 Task 6)

The notebook `project/sts-project.ipynb` is complete and executed (ALL 0.8217, 2nd of 89; Mean 0.6937, 1st). A 12-slide draft exists in `slides/projects/STS Project Presentation.pptx` (not tracked, last changed 2026-10-18).

- [ ] Decide the authors: alone, or split with a teammate following [project/two-student-plan.md](../2-project/two-student-plan.md).
- [ ] Fill in the student names (first cell of the notebook, title slide).
- [ ] Check that every number on the slides still matches the notebook output (the slides are older than the last notebook run).
- [ ] Restart & Run All, then rename to `sts-[Student1]-[Student2].ipynb`.
- [ ] Export the slides as `sts-[Student1]-[Student2].pdf`.
- [ ] Rehearse the talk in 10 minutes.
- [ ] Upload the notebook and the PDF to raco before the oral presentation.
- [ ] Optional extensions (from the conclusions): normalize numbers, dates and times; align multiword expressions with WordNet; tune the hyperparameters with cross-validation. Each one needs a re-run and updated text and slides.
- [ ] If the two-student plan is used: its section 3 (repository and workflow) still shows the old layout (data at the root, `project/PLAN.md`, `project-sts-team` branch); update it to the layout of the repository where the work is done.

## 已决定不做

- 不再请求 TextServer（每天的配额）；代码留在 notebook 里，开关关着。
- Lab02、Lab03 的 TextServer 输出和文字不更新；Lab07 的 `entities` 服务关着，FreeLing 的命名实体用 Lab 6 的缓存。
- 交上去的 Lab06 不改（本地版有两个修正）。
