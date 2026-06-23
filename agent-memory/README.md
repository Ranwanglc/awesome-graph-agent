# Agent Memory — Recent Top-Venue Papers

> Recent papers on **LLM agent long/short-term memory** from top venues (NeurIPS, ACL, EMNLP, AAAI, WWW, SIGIR, EACL, ECIR, TPAMI, PAKDD, CHI ...), discovered via the [DBLP](https://dblp.org) API.
> Curated by Sunnie 🔬 · 2026-06-23

**19 papers** · **19/19 with abstracts** · 8 open-access PDFs mirrored in the private `awesome-graph-agent-pdfs` repo (`agent-memory/`). Paywalled papers keep the abstract here so you can still see what each one does.

## Quick Index

| # | Year | Venue | Title | Link | PDF |
|---|------|-------|-------|------|-----|
| 1 | 2026 | WWW | PromptX: A Cognitive Agent Platform with Long-term Memory | [doi](https://doi.org/10.1145/3774905.3793108) | 🔒 |
| 2 | 2026 | WWW | GraphCogent: Mitigating LLMs' Working Memory Constraints via Multi-Agent Collaboration in Complex Graph Understanding | [doi](https://doi.org/10.1145/3774904.3792314) | ✅ `GraphCogent_Mitigating_LLMs_Working_Memory_Constraints_via_M.pdf` |
| 3 | 2026 | WWW | DrunkAgent: Stealthy Memory Corruption in LLM-Powered Recommender Agents | [doi](https://doi.org/10.1145/3774904.3792688) | ✅ `DrunkAgent_Stealthy_Memory_Corruption_in_LLM_Powered_Recomme.pdf` |
| 4 | 2026 | PAKDD | Memory in LLM-Based Multi-agent Systems: Mechanisms, Challenges, and Collective Intelligence | [doi](https://doi.org/10.1007/978-981-92-1468-6_10) | 🔒 |
| 5 | 2026 | ECIR | MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Retrieval and Invocation in LLM Agent Multi-turn Conversations | [doi](https://doi.org/10.1007/978-3-032-21300-6_15) | 🔒 |
| 6 | 2026 | EACL | H-MEM: Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents | [doi](https://doi.org/10.18653/v1/2026.eacl-long.15) | ✅ `H_MEM_Hierarchical_Memory_for_High_Efficiency_Long_Term_Reas.pdf` |
| 7 | 2026 | CHI Extended Abstracts | Towards Usable, Privacy Respecting Long-Term Memory for LLM-based Conversational Agents | [doi](https://doi.org/10.1145/3772363.3799198) | 🔒 |
| 8 | 2026 | AAAI | Mem-PAL: Towards Memory-based Personalized Dialogue Assistants for Long-term User-Agent Interaction | [doi](https://doi.org/10.1609/aaai.v40i37.40385) | ✅ `Mem_PAL_Towards_Memory_based_Personalized_Dialogue_Assistant.pdf` |
| 9 | 2026 | AAAI | MemoryART: Enhancing LLMs via Multi-Memory Models with Adaptive Resonance Theory for Healthcare Agents | [doi](https://doi.org/10.1609/aaai.v40i25.39205) | 🔒 |
| 10 | 2026 | AAAI | MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents | [doi](https://doi.org/10.1609/aaai.v40i36.40313) | 🔒 |
| 11 | 2026 | AAAI | Value-Driven Memory-Augmented Generation for Agentic LLMs: Towards Structured and Adaptive Knowledge Utilization | [doi](https://doi.org/10.1609/aaai.v40i48.42170) | 🔒 |
| 12 | 2026 | AAAI | ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory | [doi](https://doi.org/10.1609/aaai.v40i30.39773) | 🔒 |
| 13 | 2025 | SIGIR | AgentCF++: Memory-enhanced LLM-based Agents for Popularity-aware Cross-domain Recommendations | [doi](https://doi.org/10.1145/3726302.3730161) | 🔒 |
| 14 | 2025 | IEEE Trans. Pattern Anal. Mach. Intell. | JARVIS-1: Open-World Multi-Task Agents With Memory-Augmented Multimodal Language Models | [doi](https://doi.org/10.1109/TPAMI.2024.3511593) | 🔒 |
| 15 | 2025 | ACL | In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents | [doi](https://doi.org/10.18653/v1/2025.acl-long.413) | ✅ `In_Prospect_and_Retrospect_Reflective_Memory_Management_for.pdf` |
| 16 | 2024 | NeurIPS | AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases | [doi](http://papers.nips.cc/paper_files/paper/2024/hash/eb113910e9c3f6242541c1652e30dfd6-Abstract-Conference.html) | ✅ `AgentPoison_Red_teaming_LLM_Agents_via_Poisoning_Memory_or_K.pdf` |
| 17 | 2024 | CHI Extended Abstracts | "My agent understands me better": Integrating Dynamic Human-like Memory Recall and Consolidation in LLM-Based Agents | [doi](https://doi.org/10.1145/3613905.3650839) | 🔒 |
| 18 | 2024 | ACL | Evaluating Very Long-Term Conversational Memory of LLM Agents | [doi](https://doi.org/10.18653/v1/2024.acl-long.747) | ✅ `Evaluating_Very_Long_Term_Conversational_Memory_of_LLM_Agent.pdf` |
| 19 | 2023 | EMNLP | Open-Ended Instructable Embodied Agents with Memory-Augmented Large Language Models | [doi](https://doi.org/10.18653/v1/2023.findings-emnlp.226) | ✅ `Open_Ended_Instructable_Embodied_Agents_with_Memory_Augmente.pdf` |

---

## Papers with Abstracts

### 1. PromptX: A Cognitive Agent Platform with Long-term Memory
**WWW 2026** · [link](https://doi.org/10.1145/3774905.3793108) · DOI: `10.1145/3774905.3793108` · PDF: 🔒 paywall

> While large language models (LLMs) demonstrate impressive contextual understanding, their limitations in long-term memory and personalized reasoning constrain their practical impact in industrial settings. To address these gaps, we introduce PromptX, a cognitive platform that enables AI agents to construct structured memory and develop their reasoning over time. PromptX integrates three core technologies: (1) A new prompt markup language to define agent personas and memory organization; (2) Engram-based activation-diffusion memory networks that unify raw experiences with conceptual sequences, enabling associative retrieval through graph network propagation; (3) a protocol-driven orchestration layer enabling dynamic tool discovery and coordination, inspired by HATEOAS principles from web-engineering. During five months of real-world deployment across a range of 15+ enterprises in 6 …

<sub>abstract source: openalex-doi</sub>

### 2. GraphCogent: Mitigating LLMs' Working Memory Constraints via Multi-Agent Collaboration in Complex Graph Understanding
**WWW 2026** · [link](https://doi.org/10.1145/3774904.3792314) · DOI: `10.1145/3774904.3792314` · PDF: ✅ `GraphCogent_Mitigating_LLMs_Working_Memory_Constraints_via_M.pdf`

> Large language models (LLMs) show promising performance on small-scale graph reasoning tasks but fail when handling real-world graphs with complex queries. This phenomenon arises from LLMs' working memory constraints, which result in their inability to retain long-range graph topology over extended contexts while sustaining coherent multi-step reasoning. However, real-world graphs are often structurally complex, such as Web, Transportation, Social, and Citation networks. To address these limitations, we propose GraphCogent, a collaborative agent framework inspired by human Working Memory Model that decomposes graph reasoning into specialized cognitive processes: sense, buffer, and execute. The framework consists of three modules: Sensory Module standardizes diverse graph text representations via subgraph sampling, Buffer Module integrates and indexes graph data across multiple formats, …

<sub>abstract source: arxiv</sub>

### 3. DrunkAgent: Stealthy Memory Corruption in LLM-Powered Recommender Agents
**WWW 2026** · [link](https://doi.org/10.1145/3774904.3792688) · DOI: `10.1145/3774904.3792688` · PDF: ✅ `DrunkAgent_Stealthy_Memory_Corruption_in_LLM_Powered_Recomme.pdf`

> Large language model (LLM)-powered agents are increasingly used in recommender systems (RSs) to achieve personalized behavior modeling, where the memory mechanism plays a pivotal role in enabling the agents to autonomously explore, learn and self-evolve from real-world interactions. However, this very mechanism, serving as a contextual repository, inherently exposes an attack surface for potential adversarial manipulations. Despite its central role, the robustness of agentic RSs in the face of such threats remains largely underexplored. Previous works suffer from semantic mismatches or rely on static embeddings or pre-defined prompts, all of which are not designed for dynamic systems, especially for dynamic memory states of LLM agents. This challenge is exacerbated by the black-box nature of commercial recommenders. To tackle the above problems, in this paper, we present the first …

<sub>abstract source: arxiv</sub>

### 4. Memory in LLM-Based Multi-agent Systems: Mechanisms, Challenges, and Collective Intelligence
**PAKDD 2026** · [link](https://doi.org/10.1007/978-981-92-1468-6_10) · DOI: `10.1007/978-981-92-1468-6_10` · PDF: 🔒 paywall

> Memory plays a central role in transforming Large Language Model (LLM)-based agents from reactive predictors into consistent, context-aware collaborators. While LLM-based single-agent memory has been extensively studied, memory in LLM-based Multi-Agent Systems (LLM-MAS) lacks a systematic taxonomy and review. In multi-agent contexts, memory becomes a shared cognitive infrastructure enabling collective intelligence, long-term coordination, and team evolvement. This survey provides the first comprehensive review of memory in LLM-MAS, synthesizing research across memory architectures, management and operations, evaluation, and application, while formalizing key definitions and introducing the design space. Our survey reveals that memory in LLM-MAS is not a trivial extension of single-agent memory but a distinct research frontier-with new challenges in synchronization, access control, …

<sub>abstract source: openalex-doi</sub>

### 5. MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Retrieval and Invocation in LLM Agent Multi-turn Conversations
**ECIR 2026** · [link](https://doi.org/10.1007/978-3-032-21300-6_15) · DOI: `10.1007/978-3-032-21300-6_15` · PDF: 🔒 paywall

> Large Language Model (LLM) agents have shown significant autonomous capabilities in dynamically searching and incorporating relevant tools or Model Context Protocol (MCP) servers for individual queries. However, fixed context windows limit effectiveness in multi-turn interactions requiring repeated, independent tool usage. We introduce MemTool, a short-term memory framework enabling LLM agents to dynamically manage tools or MCP server contexts across multi-turn conversations. MemTool offers three agentic architectures: 1) Autonomous Agent Mode, granting full tool management autonomy, 2) Workflow Mode, providing deterministic control without autonomy, and 3) Hybrid Mode, combining autonomous and deterministic control. Evaluating each MemTool mode across 13+ LLMs on the ScaleMCP benchmark, we conducted experiments over 100 consecutive user interactions, measuring tool removal ratios …

<sub>abstract source: arxiv</sub>

### 6. H-MEM: Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents
**EACL 2026** · [link](https://doi.org/10.18653/v1/2026.eacl-long.15) · DOI: `10.18653/V1/2026.EACL-LONG.15` · PDF: ✅ `H_MEM_Hierarchical_Memory_for_High_Efficiency_Long_Term_Reas.pdf`

> Long-term memory is one of the key factors influencing the reasoning capabilities of Large Language Model Agents (LLM Agents).Incorporating a memory mechanism that effectively integrates past interactions can significantly enhance decision-making and contextual coherence of LLM Agents.While recent works have made progress in memory storage and retrieval, such as encoding memory into dense vectors for similarity-based search or organizing knowledge in the form of graph, these approaches often fall short in structured memory organization and efficient retrieval.To address these limitations, we propose a Hierarchical Memory (H-MEM) architecture for LLM Agents that organizes and updates memory in a multi-level fashion based on the degree of semantic abstraction.Each memory vector is embedded with a positional index encoding pointing to its semantically related submemories in the next …

<sub>abstract source: openalex-doi</sub>

### 7. Towards Usable, Privacy Respecting Long-Term Memory for LLM-based Conversational Agents
**CHI Extended Abstracts 2026** · [link](https://doi.org/10.1145/3772363.3799198) · DOI: `10.1145/3772363.3799198` · PDF: 🔒 paywall

> In recent years, Large Language Models (LLMs) have evolved from stateless text generators into conversational agents (CAs) that use long-term memory to facilitate personalised and compelling interactions. While these emerging capabilities improve user experience, they also introduce ethical and privacy concerns. Although prior work has examined LLM privacy from a technical perspective, few studies have designed features or interaction techniques for supporting users with privacy management. The aim of my thesis is to address this gap by co-designing usable, privacy-respecting memory mechanisms for LLM-based CAs. I present a mixed-methods survey of LLM-based CA users’ privacy attitudes and strategies, and an ongoing design taxonomy of conversational privacy controls. I then present a plan for two further studies focused on co-designing and prototyping interface controls with users. I aim …

<sub>abstract source: s2</sub>

### 8. Mem-PAL: Towards Memory-based Personalized Dialogue Assistants for Long-term User-Agent Interaction
**AAAI 2026** · [link](https://doi.org/10.1609/aaai.v40i37.40385) · DOI: `10.1609/AAAI.V40I37.40385` · PDF: ✅ `Mem_PAL_Towards_Memory_based_Personalized_Dialogue_Assistant.pdf`

> With the rise of smart personal devices, service-oriented human-agent interactions have become increasingly prevalent. This trend highlights the need for personalized dialogue assistants that can understand user-specific traits to accurately interpret requirements and tailor responses to individual preferences. However, existing approaches often overlook the complexities of long-term interactions and fail to capture users' subjective characteristics. To address these gaps, we present PAL-Bench, a new benchmark designed to evaluate the personalization capabilities of service-oriented assistants in long-term user-agent interactions. In the absence of available real-world data, we develop a multi-step LLM-based synthesis pipeline, which is further verified and refined by human annotators. This process yields PAL-Set, the first Chinese dataset comprising multi-session user logs and dialogue …

<sub>abstract source: arxiv</sub>

### 9. MemoryART: Enhancing LLMs via Multi-Memory Models with Adaptive Resonance Theory for Healthcare Agents
**AAAI 2026** · [link](https://doi.org/10.1609/aaai.v40i25.39205) · DOI: `10.1609/AAAI.V40I25.39205` · PDF: 🔒 paywall

> Though promising in healthcare consultation applications, large language models (LLMs) face critical limitations in retaining and utilizing long-term memory across multi-turn interactions. In particular, existing memory enhancing paradigms are constrained by limited context windows and embedding-based retrieval, often failing to maintain task relevance and still suffering from memory prototype collapse in multi-turn healthcare consultation. To address these challenges, we propose a cognitively-inspired memory framework named MemoryART, which is grounded in Adaptive Resonance Theory (ART)—a cognitive and learning theory of how humans and animals adapt to dynamic environments. MemoryART employs three memory modules—working memory, episodic memory, and semantic memory to support task-aware memory organization and dynamic retrieval. Specifically, episodic memory provides the storage of …

<sub>abstract source: openalex-doi</sub>

### 10. MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents
**AAAI 2026** · [link](https://doi.org/10.1609/aaai.v40i36.40313) · DOI: `10.1609/AAAI.V40I36.40313` · PDF: 🔒 paywall

> Modern task-oriented dialogue (TOD) systems increasingly rely on large language model (LLM) agents, leveraging Retrieval-Augmented Generation (RAG) and long-context capabilities for long-term memory utilization. However, these methods prioritise semantic similarity over task intent, degrading multi-session coherence. We propose MemGuide, a two-stage intent-driven memory selection framework: (1) Intent‑Aligned Retrieval retrieves goal-consistent QA‑formatted memory units; (2) Missing‑Slot Guided Filtering reranks units by slot-completion gain via a chain‑of‑thought reasoner and fine‑tuned LLaMA‑8B filter. We also introduce the MS-TOD, the first multi-session TOD benchmark with 132 diverse personas, 956 task goals, and annotated intent-aligned memory targets. Evaluations on MS-TOD show that MemGuide boosts task success rate by 11% (88%→99%) and reduces dialogue length by 2.84 turns, and …

<sub>abstract source: crossref</sub>

### 11. Value-Driven Memory-Augmented Generation for Agentic LLMs: Towards Structured and Adaptive Knowledge Utilization
**AAAI 2026** · [link](https://doi.org/10.1609/aaai.v40i48.42170) · DOI: `10.1609/AAAI.V40I48.42170` · PDF: 🔒 paywall

> Large Language Models (LLMs) have demonstrated remarkable capabilities in reasoning, yet their efficacy is constrained by a fundamental memory limitation: a static context window that resets with each interaction. This prevents them from accumulating experience and adapting to dynamic, long-term tasks. To address the limitations of long-term memory in agentic LLMs, this work introduces a neuro-inspired framework with two key contributions. First, we propose \textbf{ARTEM} (Agentic Retrieval with Temporal-Episodic Memory), a system that organizes experiences into structured events and manages utility-based memory consolidation. Second, we extend this framework with a distinct governance component, \textbf{Value-driven ARTEM}, that validates candidate outputs against core principles before finalization. Together, these components equip LLM agents with continual learning, adaptive …

<sub>abstract source: openalex-doi</sub>

### 12. ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory
**AAAI 2026** · [link](https://doi.org/10.1609/aaai.v40i30.39773) · DOI: `10.1609/AAAI.V40I30.39773` · PDF: 🔒 paywall

> Current large language models (LLMs) exhibit significant deficiencies in episodic memory tasks including encoding, storing, and retrieving specific information from temporally dependent events over a long period of time. Recent approaches to handle memory tasks in LLMs, such as in-context learning, retrieval-augmented generation (RAG), and fine-tuning, may resolve the long-term retention issues, but are still inadequate to handle tasks requiring chronological awareness of the stored information. We introduce Agentic Retrieval with Temporal-Episodic Memory (ARTEM), a hybrid LLM-based agent architecture integrating LLMs with a self-organizing neural network named Spatial-Temporal Episodic Memory (STEM), designed to handle episodic memory tasks. Our approach employs LLMs for event extraction from the inputs to represent temporal, spatial, entitative, and semantic information that may …

<sub>abstract source: openalex-doi</sub>

### 13. AgentCF++: Memory-enhanced LLM-based Agents for Popularity-aware Cross-domain Recommendations
**SIGIR 2025** · [link](https://doi.org/10.1145/3726302.3730161) · DOI: `10.1145/3726302.3730161` · PDF: 🔒 paywall

> LLM-based user agents, which simulate user interaction behavior, are emerging as a promising approach to enhancing recommender systems. In real-world scenarios, users' interactions often exhibit cross-domain characteristics and are influenced by others. However, the memory design in current methods causes user agents to introduce significant irrelevant information during decision-making in cross-domain scenarios and makes them unable to recognize the influence of other users' interactions, such as popularity factors. To tackle this issue, we propose a dual-layer memory architecture combined with a two-step fusion mechanism. This design avoids irrelevant information during decision-making while ensuring effective integration of cross-domain preferences. We also introduce the concepts of interest groups and group-shared memory to better capture the influence of popularity factors on users …

<sub>abstract source: openalex-doi</sub>

### 14. JARVIS-1: Open-World Multi-Task Agents With Memory-Augmented Multimodal Language Models
**IEEE Trans. Pattern Anal. Mach. Intell. 2025** · [link](https://doi.org/10.1109/TPAMI.2024.3511593) · DOI: `10.1109/TPAMI.2024.3511593` · PDF: 🔒 paywall

> Achieving human-like planning and control with multimodal observations in an open world is a key milestone for more functional generalist agents. Existing approaches can handle certain long-horizon tasks in an open world. However, they still struggle when the number of open-world tasks could potentially be infinite and lack the capability to progressively enhance task completion as game time progresses. We introduce JARVIS-1, an open-world agent that can perceive multimodal input (visual observations and human instructions), generate sophisticated plans, and perform embodied control, all within the popular yet challenging open-world Minecraft universe. Specifically, we develop JARVIS-1 on top of pre-trained multimodal language models, which map visual observations and textual instructions to plans. The plans will be ultimately dispatched to the goal-conditioned controllers. We outfit …

<sub>abstract source: arxiv</sub>

### 15. In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents
**ACL 2025** · [link](https://doi.org/10.18653/v1/2025.acl-long.413) · DOI: `10.18653/V1/2025.ACL-LONG.413` · PDF: ✅ `In_Prospect_and_Retrospect_Reflective_Memory_Management_for.pdf`

> Large Language Models (LLMs) have made significant progress in open-ended dialogue, yet their inability to retain and retrieve relevant information from long-term interactions limits their effectiveness in applications requiring sustained personalization. External memory mechanisms have been proposed to address this limitation, enabling LLMs to maintain conversational continuity. However, existing approaches struggle with two key challenges. First, rigid memory granularity fails to capture the natural semantic structure of conversations, leading to fragmented and incomplete representations. Second, fixed retrieval mechanisms cannot adapt to diverse dialogue contexts and user interaction patterns. In this work, we propose Reflective Memory Management (RMM), a novel mechanism for long-term dialogue agents, integrating forward- and backward-looking reflections: (1) Prospective Reflection, …

<sub>abstract source: arxiv</sub>

### 16. AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases
**NeurIPS 2024** · [link](http://papers.nips.cc/paper_files/paper/2024/hash/eb113910e9c3f6242541c1652e30dfd6-Abstract-Conference.html) · PDF: ✅ `AgentPoison_Red_teaming_LLM_Agents_via_Poisoning_Memory_or_K.pdf`

> LLM agents have demonstrated remarkable performance across various applications, primarily due to their advanced capabilities in reasoning, utilizing external knowledge and tools, calling APIs, and executing actions to interact with environments. Current agents typically utilize a memory module or a retrieval-augmented generation (RAG) mechanism, retrieving past knowledge and instances with similar embeddings from knowledge bases to inform task planning and execution. However, the reliance on unverified knowledge bases raises significant concerns about their safety and trustworthiness. To uncover such vulnerabilities, we propose a novel red teaming approach AgentPoison, the first backdoor attack targeting generic and RAG-based LLM agents by poisoning their long-term memory or RAG knowledge base. In particular, we form the trigger generation process as a constrained optimization to …

<sub>abstract source: arxiv</sub>

### 17. "My agent understands me better": Integrating Dynamic Human-like Memory Recall and Consolidation in LLM-Based Agents
**CHI Extended Abstracts 2024** · [link](https://doi.org/10.1145/3613905.3650839) · DOI: `10.1145/3613905.3650839` · PDF: 🔒 paywall

> In this study, we propose a novel human-like memory architecture designed for enhancing the cognitive abilities of large language model based dialogue agents. Our proposed architecture enables agents to autonomously recall memories necessary for response generation, effectively addressing a limitation in the temporal cognition of LLMs. We adopt the human memory cue recall as a trigger for accurate and efficient memory recall. Moreover, we developed a mathematical model that dynamically quantifies memory consolidation, considering factors such as contextual relevance, elapsed time, and recall frequency. The agent stores memories retrieved from the user's interaction history in a database that encapsulates each memory's content and temporal context. Thus, this strategic storage allows agents to recall specific memories and understand their significance to the user in a temporal context, …

<sub>abstract source: arxiv</sub>

### 18. Evaluating Very Long-Term Conversational Memory of LLM Agents
**ACL 2024** · [link](https://doi.org/10.18653/v1/2024.acl-long.747) · DOI: `10.18653/V1/2024.ACL-LONG.747` · PDF: ✅ `Evaluating_Very_Long_Term_Conversational_Memory_of_LLM_Agent.pdf`

> Existing works on long-term open-domain dialogues focus on evaluating model responses within contexts spanning no more than five chat sessions. Despite advancements in long-context large language models (LLMs) and retrieval augmented generation (RAG) techniques, their efficacy in very long-term dialogues remains unexplored. To address this research gap, we introduce a machine-human pipeline to generate high-quality, very long-term dialogues by leveraging LLM-based agent architectures and grounding their dialogues on personas and temporal event graphs. Moreover, we equip each agent with the capability of sharing and reacting to images. The generated conversations are verified and edited by human annotators for long-range consistency and grounding to the event graphs. Using this pipeline, we collect LoCoMo, a dataset of very long-term conversations, each encompassing 300 turns and 9K …

<sub>abstract source: arxiv</sub>

### 19. Open-Ended Instructable Embodied Agents with Memory-Augmented Large Language Models
**EMNLP 2023** · [link](https://doi.org/10.18653/v1/2023.findings-emnlp.226) · DOI: `10.18653/V1/2023.FINDINGS-EMNLP.226` · PDF: ✅ `Open_Ended_Instructable_Embodied_Agents_with_Memory_Augmente.pdf`

> Pre-trained and frozen large language models (LLMs) can effectively map simple scene rearrangement instructions to programs over a robot's visuomotor functions through appropriate few-shot example prompting. To parse open-domain natural language and adapt to a user's idiosyncratic procedures, not known during prompt engineering time, fixed prompts fall short. In this paper, we introduce HELPER, an embodied agent equipped with an external memory of language-program pairs that parses free-form human-robot dialogue into action programs through retrieval-augmented LLM prompting: relevant memories are retrieved based on the current dialogue, instruction, correction, or VLM description, and used as in-context prompt examples for LLM querying. The memory is expanded during deployment to include pairs of user's language and action plans, to assist future inferences and personalize them to the …

<sub>abstract source: arxiv</sub>

---

## By Theme

### Conversational / Long-Term Dialogue Memory
- **MemTool: Optimizing Short-Term Memory Management for Dynamic Tool Retrieval and Invocation in LLM Agent Multi-turn Conversations** (ECIR 2026) — 🔒
- **Towards Usable, Privacy Respecting Long-Term Memory for LLM-based Conversational Agents** (CHI Extended Abstracts 2026) — 🔒
- **Mem-PAL: Towards Memory-based Personalized Dialogue Assistants for Long-term User-Agent Interaction** (AAAI 2026) — PDF ✅
- **In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents** (ACL 2025) — PDF ✅
- **Evaluating Very Long-Term Conversational Memory of LLM Agents** (ACL 2024) — PDF ✅

### Memory Architectures & Management
- **PromptX: A Cognitive Agent Platform with Long-term Memory** (WWW 2026) — 🔒
- **GraphCogent: Mitigating LLMs' Working Memory Constraints via Multi-Agent Collaboration in Complex Graph Understanding** (WWW 2026) — PDF ✅
- **H-MEM: Hierarchical Memory for High-Efficiency Long-Term Reasoning in LLM Agents** (EACL 2026) — PDF ✅
- **MemoryART: Enhancing LLMs via Multi-Memory Models with Adaptive Resonance Theory for Healthcare Agents** (AAAI 2026) — 🔒
- **MemGuide: Intent-Driven Memory Selection for Goal-Oriented Multi-Session LLM Agents** (AAAI 2026) — 🔒
- **Value-Driven Memory-Augmented Generation for Agentic LLMs: Towards Structured and Adaptive Knowledge Utilization** (AAAI 2026) — 🔒

### Multi-Agent & Tool Memory
- **Memory in LLM-Based Multi-agent Systems: Mechanisms, Challenges, and Collective Intelligence** (PAKDD 2026) — 🔒
- **AgentCF++: Memory-enhanced LLM-based Agents for Popularity-aware Cross-domain Recommendations** (SIGIR 2025) — 🔒

### Memory Security / Poisoning
- **DrunkAgent: Stealthy Memory Corruption in LLM-Powered Recommender Agents** (WWW 2026) — PDF ✅
- **AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases** (NeurIPS 2024) — PDF ✅

### Embodied / Multimodal Agent Memory
- **ARTEM: Enhancing Large Language Model Agents with Spatial-Temporal Episodic Memory** (AAAI 2026) — 🔒
- **JARVIS-1: Open-World Multi-Task Agents With Memory-Augmented Multimodal Language Models** (IEEE Trans. Pattern Anal. Mach. Intell. 2025) — 🔒
- **Open-Ended Instructable Embodied Agents with Memory-Augmented Large Language Models** (EMNLP 2023) — PDF ✅

### Other
- **"My agent understands me better": Integrating Dynamic Human-like Memory Recall and Consolidation in LLM-Based Agents** (CHI Extended Abstracts 2024) — 🔒

## Notes
- Source: DBLP `search/publ/api`, filtered to 2023+ and top venues; de-duplicated by title.
- Abstracts pulled from Crossref / arXiv / Semantic Scholar / OpenAlex (source noted under each).
- PDFs: only openly available copies mirrored (ACL Anthology, NeurIPS proceedings, arXiv). Paywalled (ACM/Springer/IEEE/AAAI) marked 🔒 — abstract still included.
