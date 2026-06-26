# Shared Memory & Shared Files — Recent Top-Venue Papers

> Recent papers on **shared / collective memory and shared files / artifacts / workspaces across multiple LLM agents** from top venues (ICML, NeurIPS, AAAI, ACL, WWW, AAMAS, PAKDD, plus selected journals & landmark preprints), discovered via the [DBLP](https://dblp.org) API.
> Curated by Aris 🔬 · 2026-06-26

**18 papers** · **17/18 with abstracts** · 12 open-access PDFs mirrored in the private `awesome-graph-agent-pdfs` repo (`shared-memory-files/`). Paywalled papers keep the abstract here so you can still see what each one does.

Focus: **shared / collective** memory and shared files / artifacts across agents — *not* single-agent personal memory.

## Quick Index

| # | Year | Venue | Title | Link | PDF |
|---|------|-------|-------|------|-----|
| 1 | 2026 | Discov. Artif. Intell. | A memory fabric for conversational AI agents enabling shared and persistent memory | [doi](https://doi.org/10.1007/s44163-026-00992-z) | 🔒 |
| 2 | 2026 | WWW | GraphCogent: Mitigating LLMs' Working Memory Constraints via Multi-Agent Collaboration in Complex Graph Understanding | [doi](https://doi.org/10.1145/3774904.3792314) | ✅ `GraphCogent_Mitigating_LLMs_Working_Memory_Constraints_via.pdf` |
| 3 | 2026 | PAKDD | Memory in LLM-Based Multi-agent Systems: Mechanisms, Challenges, and Collective Intelligence | [doi](https://doi.org/10.1007/978-981-92-1468-6_10) | 🔒 |
| 4 | 2025 | ICML | Agent Reviewers: Domain-specific Multimodal Agents with Shared Memory for Paper Review | [PMLR](https://proceedings.mlr.press/v267/lu25p.html) | ✅ `Agent_Reviewers_Domain_specific_Multimodal_Agents_with_Sha.pdf` |
| 5 | 2025 | CoRR | MIRIX: Multi-Agent Memory System for LLM-Based Agents | [arXiv](https://arxiv.org/abs/2507.07957) | ✅ `MIRIX_Multi_Agent_Memory_System_for_LLM_Based_Agents.pdf` |
| 6 | 2025 | CoRR | SRMT: Shared Memory for Multi-agent Lifelong Pathfinding | [arXiv](https://arxiv.org/abs/2501.13200) | ✅ `SRMT_Shared_Memory_for_Multi_agent_Lifelong_Pathfinding.pdf` |
| 7 | 2025 | CoRR | Exploring Advanced LLM Multi-Agent Systems Based on Blackboard Architecture | [arXiv](https://arxiv.org/abs/2507.01701) | ✅ `Exploring_Advanced_LLM_Multi_Agent_Systems_Based_on_Blackb.pdf` |
| 8 | 2025 | CoRR | LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science | [arXiv](https://arxiv.org/abs/2510.01285) | ✅ `LLM_based_Multi_Agent_Blackboard_System_for_Information_Di.pdf` |
| 9 | 2023 | CIC | Enabling Synergistic Knowledge Sharing and Reasoning in Large Language Models with Collaborative Multi-Agents | [doi](https://doi.org/10.1109/CIC58953.2023.00021) | 🔒 |
| 10 | 2026 | J. Ind. Inf. Integr. | Harnessing collective intelligence of multi-agent LLM systems for sensor fault diagnosis | [doi](https://doi.org/10.1016/j.jii.2025.101012) | 🔒 |
| 11 | 2025 | NeurIPS | Centralized Reward Agent for Knowledge Sharing and Transfer in Multi-Task Reinforcement Learning | [NeurIPS](http://papers.nips.cc/paper_files/paper/2025/hash/eeb273b238606e9186452bed7190a8ab-Abstract-Conference.html) | ✅ `Centralized_Reward_Agent_for_Knowledge_Sharing_and_Transfe.pdf` |
| 12 | 2025 | AAMAS | Context Adaptive Memory-Efficient LLM Inference for Edge Multi-Agent Systems | [ACM](https://dl.acm.org/doi/10.5555/3709347.3743976) | 🔒 |
| 13 | 2025 | ACL | TReMu: Towards Neuro-Symbolic Temporal Reasoning for LLM-Agents with Memory in Multi-Session Dialogue | [doi](https://doi.org/10.18653/v1/2025.findings-acl.972) | ✅ `TReMu_Towards_Neuro_Symbolic_Temporal_Reasoning_for_LLM_Ag.pdf` |
| 14 | 2024 | AAAI | Cautiously-Optimistic Knowledge Sharing for Cooperative Multi-Agent Reinforcement Learning | [doi](https://doi.org/10.1609/aaai.v38i16.29677) | ✅ `Cautiously_Optimistic_Knowledge_Sharing_for_Cooperative_Mu.pdf` |
| 15 | 2023 | Auton. Agents Multi Agent Syst. | Full communication memory networks for team-level cooperation learning | [doi](https://doi.org/10.1007/s10458-023-09617-6) | 🔒 |
| 16 | 2024 | NeurIPS | AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases | [NeurIPS](http://papers.nips.cc/paper_files/paper/2024/hash/eb113910e9c3f6242541c1652e30dfd6-Abstract-Conference.html) | ✅ `AgentPoison_Red_teaming_LLM_Agents_via_Poisoning_Memory_or.pdf` |
| 17 | 2025 | CoRR | Collaborative Memory: Multi-User Memory Sharing in LLM Agents with Dynamic Access Control | [arXiv](https://arxiv.org/abs/2505.18279) | ✅ `Collaborative_Memory_Multi_User_Memory_Sharing_in_LLM_Agen.pdf` |
| 18 | 2025 | CoRR | Terrarium: Revisiting the Blackboard for Multi-Agent Safety, Privacy, and Security Studies | [arXiv](https://arxiv.org/abs/2510.14312) | ✅ `Terrarium_Revisiting_the_Blackboard_for_Multi_Agent_Safety.pdf` |

---

## Papers with Abstracts

### Shared / Collective Memory Architectures

#### 1. A memory fabric for conversational AI agents enabling shared and persistent memory
**Discov. Artif. Intell. 2026** · [link](https://doi.org/10.1007/s44163-026-00992-z) · DOI: `10.1007/s44163-026-00992-z` · PDF: 🔒 paywall

> Conversational artificial intelligence is now the most widely adopted platform for interfacing with large language models. Alongside large language models these artificial intelligence systems rely on contexts derived from past conversations and preferences to provide accurate and the most relevant responses to users. The knowledge base and past experiences contribute to long-term memory, while processing ongoing conversations generates short-term memory. Both long-term and short-term memories together provide a comprehensive and coherent context to the user. While most architectures focus on a single user context, there is an emerging need in conversational artificial intelligence to provide a system to generate context from multiple individuals and/or agents. Building on this foundation, we introduce memory fabric, a framework that allows conversational artificial intelligence to …

<sub>abstract source: openalex-doi</sub>

#### 2. GraphCogent: Mitigating LLMs' Working Memory Constraints via Multi-Agent Collaboration in Complex Graph Understanding
**WWW 2026** · [link](https://doi.org/10.1145/3774904.3792314) · DOI: `10.1145/3774904.3792314` · PDF: ✅ `GraphCogent_Mitigating_LLMs_Working_Memory_Constraints_via.pdf`

> Large language models (LLMs) show promising performance on small-scale graph reasoning tasks but fail when handling real-world graphs with complex queries. This phenomenon arises from LLMs' working memory constraints, which result in their inability to retain long-range graph topology over extended contexts while sustaining coherent multi-step reasoning. However, real-world graphs are often structurally complex, such as Web, Transportation, Social, and Citation networks. To address these limitations, we propose GraphCogent, a collaborative agent framework inspired by human Working Memory Model that decomposes graph reasoning into specialized cognitive processes: sense, buffer, and execute. The framework consists of three modules: Sensory Module standardizes diverse graph text representations via subgraph sampling, Buffer Module integrates and indexes graph data across multiple formats, …

<sub>abstract source: arxiv</sub>

#### 3. Memory in LLM-Based Multi-agent Systems: Mechanisms, Challenges, and Collective Intelligence
**PAKDD 2026** · [link](https://doi.org/10.1007/978-981-92-1468-6_10) · DOI: `10.1007/978-981-92-1468-6_10` · PDF: 🔒 paywall

> Memory plays a central role in transforming Large Language Model (LLM)-based agents from reactive predictors into consistent, context-aware collaborators. While LLM-based single-agent memory has been extensively studied, memory in LLM-based Multi-Agent Systems (LLM-MAS) lacks a systematic taxonomy and review. In multi-agent contexts, memory becomes a shared cognitive infrastructure enabling collective intelligence, long-term coordination, and team evolvement. This survey provides the first comprehensive review of memory in LLM-MAS, synthesizing research across memory architectures, management and operations, evaluation, and application, while formalizing key definitions and introducing the design space. Our survey reveals that memory in LLM-MAS is not a trivial extension of single-agent memory but a distinct research frontier-with new challenges in synchronization, access control, …

<sub>abstract source: openalex-doi</sub>

#### 4. Agent Reviewers: Domain-specific Multimodal Agents with Shared Memory for Paper Review
**ICML 2025** · [link](https://proceedings.mlr.press/v267/lu25p.html) · PDF: ✅ `Agent_Reviewers_Domain_specific_Multimodal_Agents_with_Sha.pdf`

> Feedback from peer review is essential to improve the quality of scientific articles. However, at present, many manuscripts do not receive sufficient external feedback for refinement before or during submission. Therefore, a system capable of providing detailed and professional feedback is crucial for enhancing research efficiency. In this paper, we have compiled the largest dataset of paper reviews to date by collecting historical open-access papers and their corresponding review comments and standardizing them using LLM. We then developed a multi-agent system that mimics real human review processes, based on LLMs. This system, named Agent Reviewers, includes the innovative introduction of multimodal reviewers to provide feedback on the visual elements of papers. Additionally, a shared memory pool that stores historical papers’ metadata is preserved, which supplies reviewer agents with …

<sub>abstract source: mlr-proceedings</sub>

#### 5. MIRIX: Multi-Agent Memory System for LLM-Based Agents
**CoRR 2025** · [link](https://arxiv.org/abs/2507.07957) · DOI: `10.48550/arXiv.2507.07957` · PDF: ✅ `MIRIX_Multi_Agent_Memory_System_for_LLM_Based_Agents.pdf`

> Although memory capabilities of AI agents are gaining increasing attention, existing solutions remain fundamentally limited. Most rely on flat, narrowly scoped memory components, constraining their ability to personalize, abstract, and reliably recall user-specific information over time. To this end, we introduce MIRIX, a modular, multi-agent memory system that redefines the future of AI memory by solving the field's most critical challenge: enabling language models to truly remember. Unlike prior approaches, MIRIX transcends text to embrace rich visual and multimodal experiences, making memory genuinely useful in real-world scenarios. MIRIX consists of six distinct, carefully structured memory types: Core, Episodic, Semantic, Procedural, Resource Memory, and Knowledge Vault, coupled with a multi-agent framework that dynamically controls and coordinates updates and retrieval. This …

<sub>abstract source: arxiv</sub>

#### 6. SRMT: Shared Memory for Multi-agent Lifelong Pathfinding
**CoRR 2025** · [link](https://arxiv.org/abs/2501.13200) · DOI: `10.48550/arXiv.2501.13200` · PDF: ✅ `SRMT_Shared_Memory_for_Multi_agent_Lifelong_Pathfinding.pdf`

> Multi-agent reinforcement learning (MARL) demonstrates significant progress in solving cooperative and competitive multi-agent problems in various environments. One of the principal challenges in MARL is the need for explicit prediction of the agents' behavior to achieve cooperation. To resolve this issue, we propose the Shared Recurrent Memory Transformer (SRMT) which extends memory transformers to multi-agent settings by pooling and globally broadcasting individual working memories, enabling agents to exchange information implicitly and coordinate their actions. We evaluate SRMT on the Partially Observable Multi-Agent Pathfinding problem in a toy Bottleneck navigation task that requires agents to pass through a narrow corridor and on a POGEMA benchmark set of tasks. In the Bottleneck task, SRMT consistently outperforms a variety of reinforcement learning baselines, especially under …

<sub>abstract source: arxiv</sub>

### Blackboard & Shared Workspace

#### 7. Exploring Advanced LLM Multi-Agent Systems Based on Blackboard Architecture
**CoRR 2025** · [link](https://arxiv.org/abs/2507.01701) · DOI: `10.48550/arXiv.2507.01701` · PDF: ✅ `Exploring_Advanced_LLM_Multi_Agent_Systems_Based_on_Blackb.pdf`

> In this paper, we propose to incorporate the blackboard architecture into LLM multi-agent systems (MASs) so that (1) agents with various roles can share all the information and others' messages during the whole problem-solving process, (2) agents that will take actions are selected based on the current content of the blackboard, and (3) the selection and execution round is repeated until a consensus is reached on the blackboard. We develop the first implementation of this proposal and conduct experiments on commonsense knowledge, reasoning and mathematical datasets. The results show that our system can be competitive with the SOTA static and dynamic MASs by achieving the best average performance, and at the same time manage to spend less tokens. Our proposal has the potential to enable complex and dynamic problem-solving where well-defined structures or workflows are unavailable.

<sub>abstract source: arxiv</sub>

#### 8. LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science
**CoRR 2025** · [link](https://arxiv.org/abs/2510.01285) · DOI: `10.48550/arXiv.2510.01285` · PDF: ✅ `LLM_based_Multi_Agent_Blackboard_System_for_Information_Di.pdf`

> Advances in large language models (LLMs) have created new opportunities in data science, but their deployment is often limited by the challenge of finding relevant data in large data lakes. Existing methods struggle with this: both single- and multi-agent systems are quickly overwhelmed by large, heterogeneous files, and master-slave multi-agent systems rely on a rigid central controller that requires precise knowledge of each sub-agent's capabilities, which is not possible in large-scale settings where the main agent lacks full observability over sub-agents' knowledge and competencies. We propose a novel multi-agent paradigm inspired by the blackboard architecture for traditional AI models. In our framework, a central agent posts requests to a shared blackboard, and autonomous subordinate agents - either responsible for a partition of the data lake or retrieval from the web - volunteer …

<sub>abstract source: arxiv</sub>

### Shared File / Artifact Coordination

#### 9. Enabling Synergistic Knowledge Sharing and Reasoning in Large Language Models with Collaborative Multi-Agents
**CIC 2023** · [link](https://doi.org/10.1109/CIC58953.2023.00021) · DOI: `10.1109/CIC58953.2023.00021` · PDF: 🔒 paywall

> Despite the significant advancements in the field of Natural Language Processing (NLP), Large Language Models (LLMs) have shown limitations in performing complex tasks that require arithmetic, commonsense, and symbolic reasoning. Reasoning frameworks like ReAct, Chain-of-thought (CoT), Tree-of-thoughts (ToT), etc. have shown success but with limitations in solving long-form complex tasks. To address this, we pro-pose a knowledge-sharing and collaborative multi-agent assisted framework on LLMs that leverages the capabilities of existing reasoning frameworks and the collaborative skills of multi-agent systems (MASs). The objectives of the proposed framework are to overcome the limitations of LLMs, enhance their reasoning capabilities, and improve their performance in complex tasks. It involves generating natural language rationales and in-context few-shot learning via prompting, and …

<sub>abstract source: semanticscholar</sub>

### Communication & Coordination Memory

#### 10. Harnessing collective intelligence of multi-agent LLM systems for sensor fault diagnosis
**J. Ind. Inf. Integr. 2026** · [link](https://doi.org/10.1016/j.jii.2025.101012) · DOI: `10.1016/j.jii.2025.101012` · PDF: 🔒 paywall

> *(No open abstract available from Crossref / arXiv / Semantic Scholar / OpenAlex — paywalled venue, abstract not retrievable.)*

#### 11. Centralized Reward Agent for Knowledge Sharing and Transfer in Multi-Task Reinforcement Learning
**NeurIPS 2025** · [link](http://papers.nips.cc/paper_files/paper/2025/hash/eeb273b238606e9186452bed7190a8ab-Abstract-Conference.html) · PDF: ✅ `Centralized_Reward_Agent_for_Knowledge_Sharing_and_Transfe.pdf`

> Reward shaping is effective in addressing the sparse-reward challenge in reinforcement learning (RL) by providing immediate feedback through auxiliary, informative rewards. Based on the reward shaping strategy, we propose a novel multi-task reinforcement learning framework that integrates a centralized reward agent (CRA) and multiple distributed policy agents. The CRA functions as a knowledge pool, aimed at distilling knowledge from various tasks and distributing it to individual policy agents to improve learning efficiency. Specifically, the shaped rewards serve as a straightforward metric for encoding knowledge. This framework not only enhances knowledge sharing across established tasks but also adapts to new tasks by transferring meaningful reward signals. We validate the proposed method on both discrete and continuous domains, including the representative Meta-World benchmark, …

<sub>abstract source: arxiv</sub>

#### 12. Context Adaptive Memory-Efficient LLM Inference for Edge Multi-Agent Systems
**AAMAS 2025** · [link](https://dl.acm.org/doi/10.5555/3709347.3743976) · DOI: `10.5555/3709347.3743976` · PDF: 🔒 paywall

> Large Language Models (LLMs) excel at multi-document QA, summarization, code generation, and other language-intensive tasks, yet they demand substantial memory resources for storing key-value (KV) caches and processing attention in long-context scenarios. These requirements often prohibit on-device or edge deployments in multi-agent systems (MAS), where multiple agents share or update contextual information and need efficient inference pipelines. We present CASK (Context-Adaptive Sparse Key-value), an inference-time strategy that reduces memory usage while preserving strong performance on extended contexts. CASK addresses this challenge with two complementary mechanisms: a dynamic sparse attention module-a lightweight, meta-learned component-that identifies the most relevant context tokens, and an adaptive KV-cache compression technique that dynamically quantizes and prunes less …

<sub>abstract source: semanticscholar</sub>

#### 13. TReMu: Towards Neuro-Symbolic Temporal Reasoning for LLM-Agents with Memory in Multi-Session Dialogue
**ACL 2025** · [link](https://doi.org/10.18653/v1/2025.findings-acl.972) · DOI: `10.18653/v1/2025.findings-acl.972` · PDF: ✅ `TReMu_Towards_Neuro_Symbolic_Temporal_Reasoning_for_LLM_Ag.pdf`

> Temporal reasoning in multi-session dialogues presents a significant challenge which has been under-studied in previous temporal reasoning benchmarks. To bridge this gap, we propose a new evaluation task for temporal reasoning in multi-session dialogues and introduce an approach to construct a new benchmark by augmenting dialogues from LoCoMo and creating multi-choice QAs. Furthermore, we present TReMu, a new framework aimed at enhancing the temporal reasoning capabilities of LLM-agents in this context. Specifically, the framework employs time-aware memorization through timeline summarization, generating retrievable memory by summarizing events in each dialogue session with their inferred dates. Additionally, we integrate neuro-symbolic temporal reasoning, where LLMs generate Python code to perform temporal calculations and select answers. Experimental evaluations on popular LLMs …

<sub>abstract source: arxiv</sub>

#### 14. Cautiously-Optimistic Knowledge Sharing for Cooperative Multi-Agent Reinforcement Learning
**AAAI 2024** · [link](https://doi.org/10.1609/aaai.v38i16.29677) · DOI: `10.1609/aaai.v38i16.29677` · PDF: ✅ `Cautiously_Optimistic_Knowledge_Sharing_for_Cooperative_Mu.pdf`

> While decentralized training is attractive in multi-agent reinforcement learning (MARL) for its excellent scalability and robustness, its inherent coordination challenges in collaborative tasks result in numerous interactions for agents to learn good policies. To alleviate this problem, action advising methods make experienced agents share their knowledge about what to do, while less experienced agents strictly follow the received advice. However, this method of sharing and utilizing knowledge may hinder the team's exploration of better states, as agents can be unduly influenced by suboptimal or even adverse advice, especially in the early stages of learning. Inspired by the fact that humans can learn not only from the success but also from the failure of others, this paper proposes a novel knowledge sharing framework called Cautiously-Optimistic kNowledge Sharing (CONS). CONS enables …

<sub>abstract source: crossref</sub>

#### 15. Full communication memory networks for team-level cooperation learning
**Auton. Agents Multi Agent Syst. 2023** · [link](https://doi.org/10.1007/s10458-023-09617-6) · DOI: `10.1007/s10458-023-09617-6` · PDF: 🔒 paywall

> Communication in multi-agent systems is a key driver of team-level cooperation, for instance allowing individual agents to augment their knowledge about the world in partially-observable environments. In this paper, we propose two reinforcement learning-based multi-agent models, namely FCMNet and FCMTran. The two models both allow agents to simultaneously learn a differentiable communication mechanism that connects all agents as well as a common, cooperative policy conditioned upon received information. FCMNet utilizes multiple directional Long Short-Term Memory chains to sequentially transmit and encode the current observation-based messages sent by every other agent at each timestep. FCMTran further relies on the encoder of a modified transformer to simultaneously aggregate multiple self-generated messages sent by all agents at the previous timestep into a single message that is used …

<sub>abstract source: semanticscholar</sub>

### Security & Access Control of Shared Memory

#### 16. AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases
**NeurIPS 2024** · [link](http://papers.nips.cc/paper_files/paper/2024/hash/eb113910e9c3f6242541c1652e30dfd6-Abstract-Conference.html) · PDF: ✅ `AgentPoison_Red_teaming_LLM_Agents_via_Poisoning_Memory_or.pdf`

> LLM agents have demonstrated remarkable performance across various applications, primarily due to their advanced capabilities in reasoning, utilizing external knowledge and tools, calling APIs, and executing actions to interact with environments. Current agents typically utilize a memory module or a retrieval-augmented generation (RAG) mechanism, retrieving past knowledge and instances with similar embeddings from knowledge bases to inform task planning and execution. However, the reliance on unverified knowledge bases raises significant concerns about their safety and trustworthiness. To uncover such vulnerabilities, we propose a novel red teaming approach AgentPoison, the first backdoor attack targeting generic and RAG-based LLM agents by poisoning their long-term memory or RAG knowledge base. In particular, we form the trigger generation process as a constrained optimization to …

<sub>abstract source: arxiv</sub>

#### 17. Collaborative Memory: Multi-User Memory Sharing in LLM Agents with Dynamic Access Control
**CoRR 2025** · [link](https://arxiv.org/abs/2505.18279) · DOI: `10.48550/arXiv.2505.18279` · PDF: ✅ `Collaborative_Memory_Multi_User_Memory_Sharing_in_LLM_Agen.pdf`

> Complex tasks are increasingly delegated to ensembles of specialized LLM-based agents that reason, communicate, and coordinate actions-both among themselves and through interactions with external tools, APIs, and databases. While persistent memory has been shown to enhance single-agent performance, most approaches assume a monolithic, single-user context-overlooking the benefits and challenges of knowledge transfer across users under dynamic, asymmetric permissions. We introduce Collaborative Memory, a framework for multi-user, multi-agent environments with asymmetric, time-evolving access controls encoded as bipartite graphs linking users, agents, and resources. Our system maintains two memory tiers: (1) private memory-private fragments visible only to their originating user; and (2) shared memory-selectively shared fragments. Each fragment carries immutable provenance attributes …

<sub>abstract source: arxiv</sub>

#### 18. Terrarium: Revisiting the Blackboard for Multi-Agent Safety, Privacy, and Security Studies
**CoRR 2025** · [link](https://arxiv.org/abs/2510.14312) · DOI: `10.48550/arXiv.2510.14312` · PDF: ✅ `Terrarium_Revisiting_the_Blackboard_for_Multi_Agent_Safety.pdf`

> A multi-agent system (MAS) powered by large language models (LLMs) can automate tedious user tasks such as meeting scheduling that requires inter-agent collaboration. LLMs enable nuanced protocols that account for unstructured private data, user constraints, and preferences. However, this design introduces new risks, including misalignment and attacks by malicious parties that compromise agents or steal user data. In this paper, we propose the Terrarium framework for fine-grained study on safety, privacy, and security in LLM-based MAS. We repurpose the blackboard design, an early approach in multi-agent systems, to create a modular, configurable testbed for multi-agent collaboration. We identify key attack vectors such as misalignment, malicious agents, compromised communication, and data poisoning. We implement three collaborative MAS scenarios with four representative attacks to …

<sub>abstract source: arxiv</sub>

---

## Notes
- Source: DBLP `search/publ/api` (via `dblp.uni-trier.de` mirror; main host returned HTTP 500 during this run), filtered to 2023+ and shared/collective-memory relevance; de-duplicated by DBLP key/title.
- Abstracts pulled from Crossref / arXiv / Semantic Scholar / OpenAlex / PMLR proceedings (source noted under each).
- PDFs: only openly available copies mirrored (arXiv, PMLR proceedings). Paywalled (ACM/Springer/IEEE/Elsevier) marked 🔒 — abstract still included where retrievable.
- Landmark preprints (CoRR) on blackboard / shared memory are included where directly on-topic and no published version exists.
