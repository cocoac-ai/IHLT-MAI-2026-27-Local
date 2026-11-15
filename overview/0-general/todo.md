# 待办和现状

更新：2026-11-15

## 现在做什么

1. **决定 STS 项目的作者**：一个人，还是按 [two-student-plan.md](../2-project/two-student-plan.md) 和队友分。定了以后填名字（notebook 第一格、标题页）。
2. **核对幻灯片**：幻灯片比 notebook 最后一次运行要早，逐个数字对一遍；然后 Restart & Run All，按 `sts-[Student1]-[Student2]` 改名，导出 PDF。
3. **Lab08、Lab09**：本地已完成，团队仓库 `team/lab08/`、`team/lab09/` 还是空的，没交。

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
