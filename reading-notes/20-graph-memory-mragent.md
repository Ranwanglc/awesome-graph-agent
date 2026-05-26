# 精读报告：Memory is Reconstructed, Not Retrieved: Graph Memory for LLM Agents

**Paper #20 | Published at ICLR 2026 (Conference Paper)**
**Authors:** Shuo Ji, Yibo Li, Bryan Hooi (National University of Singapore)
**Code:** https://github.com/Ji-shuo/MRAgent
**OpenReview:** https://openreview.net/forum?id=YPoHy6lgKP
**Also presented at:** ICML 2026 Poster, ICLR 2026 Workshop MemAgents

---

## 0. 一句话总结

MRAgent 将 Agent 记忆访问从"一次性检索"升级为"迭代联想重构"——用 Cue-Tag-Content 异构图建模记忆，LLM 在图上多步推理式遍历，边推理边剪枝，理论证明严格强于被动检索，实验提升 23%+且降低 token 开销。

---

## 1. 研究动机

### 1.1 核心问题
LLM Agent 需要处理长期交互历史，但受限于上下文窗口。现有 memory-augmented agent 采用**"retrieve-then-reason"**静态范式——先一次性检索，再推理。这导致：

1. **无法中间调整：** 检索一旦完成，无法根据推理中发现的新线索重新搜索
2. **噪声累积：** 固定 top-k 或 N-hop 扩展引入大量无关内容
3. **间接证据不可达：** 无法通过推理链发现非直接关联的记忆

### 1.2 认知科学视角
- 人类记忆回忆是**序列性重构过程**（非一次性读取）
- 上下文线索 → 激活 engram → 偏置后续回忆 → 逐步重构
- MRAgent 的 Cue-Tag-Content 对应人类记忆的 "线索→印记→内容"

---

## 2. 形式化定义

### 2.1 记忆访问框架

外部记忆 $M$ 含 $N$ 个记忆单元 $V = \{v_1, ..., v_N\}$

**被动检索（Passive Retrieval）：**
$$\{v^{(1)}, ..., v^{(T)}\} = \pi_p(x)$$
一次性、无状态，仅基于查询 $x$。

**主动重构（Active Reconstruction）：**
$$v^{(t)} = \pi_a^{(t)}(x, S^{(t-1)}), \quad S^{(t)} = S^{(t-1)} \cup \{v^{(t)}\}$$
逐步、有状态，每步根据已积累证据决定下一步。

### 2.2 现有方法的被动范式

| 方法 | 检索策略 | 缺陷 |
|------|---------|------|
| RAG | $\pi(x) = \text{TopK}(\text{sim}(x,v), k)$ | 仅表面相似，无多跳能力 |
| A-Mem | seed + N-hop 邻居扩展 | 要求显式图链接，固定扩展引入噪声 |
| MemoryOS | 三层级 STM/MTM/LPM | 检索仍是静态的 top-k |
| LangMem | 对话摘要 + 向量检索 | 压缩丢失细节 |
| Mem0 | LLM-driven CRUD + 相似度检索 | 检索不适应中间证据 |

---

## 3. 方法论：MRAgent

### 3.1 联想记忆系统（Associative Memory System）

**异构图结构：** $M = (C, V, R)$

- **Cues $C$：** 细粒度关键词（实体、属性等）
- **Contents $V$：** 记忆内容节点（情景 + 语义）
- **Relations $R \subseteq C \times G \times V$：** 带类型关系，其中 $G$ 为 Tag 集合

**核心设计——Associative Tags：**
Tags 不是简单索引，而是**语义桥梁**，总结了 Cue 与 Content 之间的关联模式。

**两个映射算子：**
$$\phi_{c \to g}(c) \triangleq \{g | (c, g, \cdot) \in R\}$$
$$\phi_{(c,g) \to v}(c, g) \triangleq \{v | (c, g, v) \in R\}$$

第一步从 Cue 激活候选 Tags，第二步从 (Cue, Tag) 对检索 Content。将联想推理与内容检索**解耦**。

### 3.2 多粒度记忆层

| 层 | 结构 | 内容 | 功能 |
|----|------|------|------|
| 情景层 | Cue-Tag-Episode | 具体事件 + 时间线 | 事件级细粒度检索 |
| 语义层 | Cue-Tag-Semantic | 人物属性、偏好、事实 | 稳定知识直接访问 |
| 话题层 | Topic-Episode | 跨情景的主题聚合 | 高层级推理 |

### 3.3 记忆构建流程

从原始对话 $T$ 构建记忆图：

**情景记忆构建：**
1. $\{e_i\} \leftarrow R_{LLM}(T)$ — 代词消解 + 时间归一化 + 情景分段
2. $g_i \leftarrow T_{LLM}(e_i)$ — LLM 生成关联标签（短语）
3. $C_i \leftarrow K_{LLM}(e_i)$ — LLM 提取关键 Cues

**语义记忆构建：**
$$\{(c_i^s, g_i^s, s_i)\} \leftarrow S_{LLM}(T)$$
提取稳定事实/属性，形成 (实体 Cue, 方面 Tag, 语义内容)

**话题记忆构建：**
$$\{\tau_j\} \leftarrow A_{LLM}(\{e_i\})$$
从情景集合中抽象出反复出现的主题模式

### 3.4 主动记忆重构算法（Algorithm 1）

```
Input: 查询 x, 记忆图 G, 遍历动作集 A, 最大步数 T
Output: 答案 ŷ

1. C ← EXTRACT_CUES(x)          // 从查询提取初始 Cues
2. Z⁰ ← ACTIVE_SET_INIT(C, G)   // 初始化活跃集
3. H⁰ ← ∅                        // 初始化重构上下文
4. for t = 0 to T-1:
5.   A⁽ᵗ⁾ ← C_LLM(x, H⁽ᵗ⁾, Z⁽ᵗ⁾)     // LLM 选择遍历动作
6.   Z̃⁽ᵗ⁺¹⁾ ← ∪{Πₐ(Z⁽ᵗ⁾)} for a ∈ A⁽ᵗ⁾  // 执行图遍历
7.   Z⁽ᵗ⁺¹⁾ ← R_LLM(x, H⁽ᵗ⁾, Z̃⁽ᵗ⁺¹⁾)   // LLM 路由 + 剪枝
8.   H⁽ᵗ⁺¹⁾ ← H⁽ᵗ⁾ ∪ Z⁽ᵗ⁺¹⁾             // 更新证据
9.   if STOP(x, H⁽ᵗ⁺¹⁾): break           // 判断是否足够
10. ŷ ← ANSWER_LLM(x, H⁽ᵗ⁺¹⁾)           // 生成答案
```

**三类遍历动作：**
- **前向：** Cue→Tag（激活标签）、(Cue,Tag)→Content（检索内容）
- **反向：** Content→(Cue,Tag)（从内容发现新线索）

**两种执行模式：**
- Navigate 模式：调用工具探索记忆图
- Answer 模式：证据充分后生成回答

### 3.5 记忆工具包（Memory Toolkit）

| 工具 | 映射函数 | 功能 |
|------|---------|------|
| query_tag_events | $\phi_{(c,g) \to e}$ | 检索 cue-tag 对关联的情景事件 |
| query_conversation_time | $\phi_{e \to t}$ | 获取事件时间戳 |
| query_event_keywords | $\phi_{e \to (c,g)}$ | 从事件提取关联 cues 和 tags |
| query_event_context | $\phi_{e \to ctx}$ | 获取事件上下文文本 |
| query_personal_information | $\phi_{c^s \to g^s}$ | 获取人物关联的语义方面 |
| query_personal_aspect | $\phi_{(c^s,g^s) \to v^s}$ | 检索 (人物, 方面) 的语义内容 |
| query_topic_events | $\phi_{\tau \to e}$ | 获取话题关联的事件 |

---

## 4. 理论分析

**定理（Active > Passive 的严格表达力优势）：**

对于任意检索预算 $T \geq 2$：
$$H_{passive}^{LM}(T) \subsetneq H_{active}^{LM}(T)$$

即：被动检索能实现的所有映射，主动重构都能实现；但存在主动重构能实现而被动检索不能实现的映射。

**直觉：** 主动策略可以根据第一步的结果调整第二步的方向——这种条件依赖是被动策略做不到的。

---

## 5. 实验结果

### 5.1 主实验（LoCoMo Benchmark）

| 方法 | Multi-hop J | Temporal J | Overall J |
|------|------------|-----------|-----------|
| RAG | 58.16 | 49.22 | 61.30 |
| A-Mem | 53.54 | 49.53 | 55.97 |
| MemoryOS | 63.82 | 47.04 | 63.35 |
| Mem0 | 68.79 | 61.68 | 68.31 |
| **MRAgent** | **75.17** | **80.37** | **84.21** |

*Gemini backbone; Claude backbone 结果类似，Overall J 达 88.32*

**关键发现：**
- **Overall 提升 23.3%**（Gemini）/ 12.4%（Claude）vs 最强 baseline
- 在 Temporal 和 Multi-hop 类型上提升最显著（这正是需要多步推理的类型）

### 5.2 LongMemEval Benchmark

| 方法 | Multi-session | Temporal | Overall |
|------|--------------|----------|---------|
| RAG | 54.89 | 42.86 | 54.65 |
| Mem0 | 50.38 | 45.11 | 53.01 |
| **MRAgent** | **68.42** | **68.42** | **72.95** |
| MRAgent* (Claude retrieval) | **86.46** | **85.71** | **86.76** |

相比最强 baseline 提升 **32%**。

### 5.3 效率分析（Token + Runtime）

| 方法 | Token 消耗 | Runtime(s) |
|------|-----------|-----------|
| A-Mem | 632k | 1,122 |
| MemoryOS | 273k | 3,136 |
| LangMem | 3,268k | 1,210 |
| Mem0 | 245k | 533 |
| **MRAgent** | **118k** | 586 |

**MRAgent token 使用最少**（118k vs 次低 245k），因为：
- 轻量级记忆构建（复杂关系建模推迟到检索阶段）
- Tag 引导的选择性检索避免了读取无关内容
- "按需"访问 vs "全量"加载

### 5.4 消融实验

| 结构变体 | 无推理 | 有推理 |
|---------|--------|--------|
| CE (Cue→Episode) | 低 | 中 |
| CTE (Cue-Tag-Episode) | 中 | 高 |
| CTC (Cue-Tag-Content, 完整) | 中+ | **最高** |

**结论：**
1. **多步推理是关键因素：** 所有结构配合推理后都大幅提升
2. **Tag 提供有效的语义引导：** CTE > CE（无推理设置下）
3. **语义记忆不可缺少：** 移除语义层后性能明显下降

### 5.5 多轮推理分析

- Single-hop / Temporal 查询：~3 轮即达近完美 Recall
- Multi-hop 查询：迭代探索带来 **30%+ 的 Recall 提升**
- 证明了多步重构对复杂查询的必要性

---

## 6. 局限性与讨论

**作者指出的设计选择：**
- 将复杂关系建模推迟到检索阶段（构建阶段相对简单）
- 当前未引入记忆更新/遗忘机制
- 更适合"重查询"场景（构建轻量，检索智能）

**潜在局限（推断）：**
- 每次查询需要多轮 LLM 调用（虽然总 token 减少，但延迟可能增加）
- 记忆图的质量依赖于构建阶段 LLM 的提取能力
- 对于简单 single-hop 查询可能过度设计

---

## 7. 与 Octo 平台的关联思考

### 7.1 直接可借鉴的设计

| MRAgent 设计 | Octo 应用场景 |
|-------------|-------------|
| Cue-Tag-Content 图结构 | Lobster Agent 的长期交互历史存储 |
| 多粒度记忆层（情景+语义+话题） | 用户画像 + 对话历史 + 群组话题 |
| LLM 驱动的记忆构建 | Octo Smart Summary 可复用相同 pipeline |
| Memory Toolkit（工具化记忆访问） | Agent 通过 tool-call 访问记忆图 |

### 7.2 对 OpenClaw 的启发

| 当前做法 | 可优化方向 |
|---------|-----------|
| `memory_search` 一次语义匹配 | 支持多轮迭代检索（Navigate 模式） |
| MEMORY.md 扁平存储 | 可引入 Tag 层做关联索引 |
| Self-improving corrections 线性日志 | 用 CTC 图连接相关经验 |

### 7.3 与本次整理其他论文的交叉

- **#4 Graph-R1：** 可用 RL 端到端优化 MRAgent 的遍历策略
- **#1 NaviAgent：** 图驱动工具编排 → MRAgent 思路可推广到"记忆驱动的工具选择"
- **#13 GraphFlow：** MRAgent 的多步检索可作为 Agent Serving 的一种工作流模式

---

## 8. 关键 Takeaways

1. **范式转移：** 记忆是重构出来的，不是检索出来的
2. **Tag 是关键创新：** 不是简单索引，而是让 LLM 在访问内容前就能评估路径
3. **效率悖论：** 更多推理步骤 ≠ 更多消耗（精准访问反而减少了总 token）
4. **理论支撑：** 主动策略严格强于被动策略（不是经验性的而是可证明的）
5. **实用性：** 代码开源，使用 Gemini-2.5-Flash / Claude-Sonnet-4.5，可直接复现

---

*Created: 2026-05-26 | Author: Danni 🦊*
*Status: ✅ 全文精读完成（23页）*
