# STS 项目：要做什么

更新：2026-11-16

对照的材料：题目 `slides/projects/Project-Semantic-Textual Similarity.pdf`（8 页，2026-11-16 的版本）和 `slides/projects/papers/` 里的论文。本地的实现在 `project/sts-project.ipynb`。

## 1. 一句话

SemEval 2012 Task 6（Semantic Textual Similarity）：给两个句子，预测它们的意思有多接近，0（话题不同）到 5（完全等价）。用 Pearson 相关系数和 gold standard 比。

## 2. 交什么

口头报告之前传到 raco（IHLT STS Project）：

| 文件 | 内容 |
|---|---|
| `sts-[Student1]-[Student2].ipynb` | notebook |
| `sts-[Student1]-[Student2].pdf` | 幻灯片 |

## 3. 题目要求（第 5 页）

| # | 要求 | 必做 |
|---|---|---|
| 1 | 用 SemEval 2012 STS 的数据和任务描述 | 是 |
| 2 | 用句子相似度的度量实现几种检测 paraphrase 的方法 | 是 |
| 2a | 探索**词汇**的几个维度（lexical dimensions） | 是 |
| 2b | **单独**探索句法维度（syntactic dimension alone） | 是 |
| 2c | 探索两者的**组合** | 是 |
| 3 | 自选的新组件 | 可选 |
| 4 | 比较并评论这些方法的结果：方法之间比，和官方结果比 | 是 |

限制：

- **不能用现成的词向量或句向量模型**（例如 BERT）。
- **不能用别的数据**：只有 trial、train、test 和参赛系统的提交（第 4 页）。

## 4. Strategies（第 8 页，这次新加的一页）

这一页给的是做法的方向，不是新的必做项，但它说明了老师希望看到哪些东西：

| 方向 | 例子 |
|---|---|
| 不同的句子表示 | 词汇、句法、语义特征的**集合**；在不同特征集上算出的**距离向量**；两者的组合 |
| 不同的相似度度量 | 单个集合度量（Jaccard、Dice……） |
| | 度量的混合（平均、加权平均……） |
| | 学出来的模型：用 ML 学加权平均的**权重**；用 ML 从特征**直接预测**分数；用 ML 从**距离向量**预测分数 |

对 notebook 的含义：不能只给一个最终模型，要有一个从简单到复杂的对比（单个度量 → 平均 → 学出来的线性权重 → 非线性模型），说清楚每一步多了多少。

## 5. 评分（第 6 页）

| 权重 | 项目 | 对我们意味着什么 |
|---|---|---|
| 0.40 | Analysis and Representation of Results | 最重的一项：表、图、每个结论有数字支持、误差分析 |
| 0.20 | Results | Pearson（ALL）高于第 10 名（0.7562）得 10 分，低于 baseline（0.311）得 0 分，中间按比例 |
| 0.20 | Oral Presentation | 幻灯片和讲解 |
| 0.10 | Code Effectiveness | 代码能跑、结果对 |
| 0.05 | Code Readability and Efficiency | 代码清楚、不慢 |
| 0.05 | Use of NLP Libraries and Resources | 用课上的库和资源（NLTK、spaCy、WordNet） |

Results 这一项只要超过 0.7562 就满分，再高也不加分。所以超过以后，精力应该放在分析上（0.40）。lab 的成绩也是同一个教训：答案对，丢的是分析（见 `0-general/todo.md`）。

## 6. 数据

| 部分 | 内容 |
|---|---|
| trial | 分数的定义、5 对例句、输入输出格式；用不上，只是方便试 |
| train | MSRpar（750 对）、MSRvid（750）、SMTeuroparl（734） |
| test | MSRpar（750）、MSRvid（750）、SMTeuroparl（459）、OnWN（750）、SMTnews（399）；后两个是 surprise，没有训练数据 |
| submissions | 89 个官方 run 的输出，用来重算官方排名 |

官方的三个指标：ALL（五个测试集拼起来算 Pearson，评分用这个）、ALLnrm（每个测试集先做最小二乘归一化）、Mean（各测试集 Pearson 的加权平均）。

## 7. 论文（第 7 页）

`slides/projects/papers/` 里是任务综述 `task6.pdf` 和 Pearson 高于 0.65 的 17 个参赛系统。前几名的做法（方法、结果、发现的总结见 [report.md](report.md)）：

| 系统 | ALL | 做法 | 用了任务之外的什么 |
|---|---|---|---|
| UKP（第 1） | 0.8239 | 300 多个度量里选约 20 个，log-linear 回归，每个数据集一个模型 | Wikipedia、Wiktionary（ESA）、分布式词库、机器翻译回译 |
| TakeLab（第 2、3） | 0.8138 / 0.8133 | n-gram 重叠、WordNet 加权重叠、依存句法；SVR | NYT 和 Wikipedia 上的 LSA 词向量 |
| ETS（第 6、7） | 0.7834 | 机器翻译评测指标 TERp 改成判别式的编辑模型 | paraphrase 表 |
| SRIUBC（第 10） | 0.7562 | 语义相似度、词汇匹配、POS、skip-bigram；SVR | 语义相似度资源 |
| Soft Cardinality | 0.7109 | 只用表层信息（字符 q-gram 的软基数），不用任何资源 | 无 |

综述里给了置信区间：第 1 名 0.8239 的 95% 区间是 [0.8123, 0.8349]。所以前几名之间的差别在统计上不显著，说"第几名"时要带上这一点。

每篇的白话说明见 [papers.md](papers.md)。注意：`5-unt.pdf` 和 `25-buap.pdf` 下载错了，是这两个队在别的任务（Task 1、Task 2）的论文，不是 STS 的。

## 8. notebook 里要有的东西

按题目和评分倒推出来的清单，"现状"是 2026-11-16 改完以后的 `project/sts-project.ipynb`（76 格，全部执行过，整本约 5 分钟）。

| # | 内容 | 对应的要求 | 现状 |
|---|---|---|---|
| 1 | 数据的读取和描述：五个测试集有多不一样 | 3.1 | 有（第 1 节） |
| 2 | 三个官方指标，用 89 个提交验证（baseline 0.3110，第 10 名 0.7562） | 3.4、评分 | 有（第 2 节），89 个 run 都重算了 |
| 3 | 预处理：分词、POS、lemma、停用词；句法分析 | 库的使用 | 有（第 3 节）：NLTK，加上 spaCy 的依存分析（模型没有词向量） |
| 4 | 词汇特征：词和 lemma 的重叠、n-gram、TF-IDF、WordNet、数字、长度 | 3.2a | 有（4.1）：24 个 |
| 5 | **只有**句法的特征：POS、chunk、依存关系，不看词 | 3.2b | 有（4.2）：21 个，其中 5 个来自依存树 |
| 6 | 词汇和句法结合的特征：同类词比较、带词的依存三元组、主语宾语谓词 | 3.2c | 有（4.3）：14 个，其中 5 个来自依存树 |
| 7 | 从简单到复杂：单个度量 → 平均 → 学出来的线性权重 → 非线性模型 | Strategies | 有（5.1、5.2 在训练集上，7.1 在测试集上） |
| 8 | 所有选择都用训练集上的交叉验证做；测试集只在最后用一次 | 方法上要站得住 | 有（第 5 节）：24 个配置的交叉验证，另外量了折的噪声、超参数的敏感度、留一个数据集 |
| 9 | 测试集结果，和官方排名比；带置信区间 | 3.4 | 有（第 6 节）：bootstrap 区间，和 UKP、TakeLab 的成对比较，随机种子 |
| 10 | 分析：按数据集、训练策略、哪些特征有用（消融）、对没见过的数据集的泛化 | 评分 0.40 | 有（7.2–7.4） |
| 11 | 误差分析：错得最多的句对，归类，能修的修 | 评分 0.40 | 有（7.5）；数字相近的问题修了一半，时间格式没修 |
| 12 | 和论文里的系统比方法，不只比数字 | 3.4 | 有（第 8 节） |
| 13 | 结论和局限 | | 有（第 9 节） |

## 9. 现在的结果（2026-11-16）

选出来的系统：59 个特征，random forest，每个数据集一个模型（由训练集上的交叉验证选出）。

| | ALL | ALLnrm | Mean |
|---|---|---|---|
| 我们 | 0.8263 | 0.8654 | 0.6946 |
| 官方最好 | 0.8239（UKP） | 0.8635（TakeLab） | 0.6773（UKP） |

- 和 UKP 的差别**不显著**（差的 95% 区间 [-0.0077, 0.0122]），只能说"和最好的系统同一水平"，不能说"第一"。
- 远高于第 10 名（0.7562），Results 这一项满分。
- 只用词汇特征 0.8199；只用句法 0.5384；不用 spaCy（只用 NLTK）ALL 低 0.0038。

## 10. 幻灯片

12 页，16:9，10 分钟左右，每页有讲稿（备注）。结构：任务 → 数据 → 系统 → 三个维度 → 从单个度量到模型 → 怎么选模型 → 结果 → 按数据集 → 分析 → 误差 → 结论。文件是 `project/STS Project Presentation.pptx`，不进 git（`.gitignore`）；旧版已删。

## 11. 交之前还要做的

- 填学生的名字（notebook 第一格、幻灯片第 1 页），文件改名成 `sts-[Student1]-[Student2]`。
- 幻灯片导出 PDF。
- 向老师确认 spaCy 的 `en_core_web_sm` 可以用（它没有词向量，Lab 8 也用它；但内部有一层学出来的 token 表示）。如果不行，去掉依存特征就是只用 NLTK 的系统，结论不变（notebook 7.4）。
- 排练一遍，10 分钟。

## 12. 两个人的分工

notebook 已经拆成两本：`project/sts-student1.ipynb`（词汇维度、数据、评测）和 `project/sts-student2.ipynb`（句法维度、模型），用 `project/sts_parts.py` 合并成 `sts-project.ipynb`。分工、接口和用法见 [two-student-plan.md](two-student-plan.md)。
