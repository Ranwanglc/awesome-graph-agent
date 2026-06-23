# Idea Report — LLM Agent Long/Short-Term Memory

**Lens**: aris idea-discovery / idea-creator (cross-paper gap alignment)
**Date**: 2026-06-23
**Input**: 19 curated top-venue papers (`papers.json`), abstract-level
**Constraints**: no GPU, no paid API budget → ideas judged on *paper feasibility only*; no pilots run. Cross-model reviewer unavailable → devil's-advocate done in-house.
**Hard exclusions honored**: (1) cache-aware skill router, (2) staleness-gate eviction axis. See *Eliminated / too-close*.

---

## 1. Landscape Summary

The 19 papers cluster into five regions, and the structural gaps live *between* the clusters, not inside them.

- **Conversational long-term memory** is the most crowded cluster: LoCoMo (Maharana 2024) defines the very-long dialogue eval; RMM ("In Prospect and Retrospect", ACL 2025) does reflective prospective/retrospective summarization + RL-refined retrieval; Mem-PAL (AAAI) adds hierarchical+heterogeneous memory for personalization; MemGuide (AAAI) reranks memory by *task-intent/slot-completion* rather than similarity; MemoryART (AAAI) imports Adaptive Resonance Theory for healthcare; "My agent understands me better" (CHI 2024) adds human-like recall cues + a consolidation equation; "Towards Usable, Privacy Respecting…" (CHI 2026) is the lone HCI/privacy-controls entry.
- **Memory architectures/management**: H-MEM (EACL) builds a multi-level index with pointer-based routing to avoid exhaustive similarity search; PromptX (WWW) uses engram activation-diffusion graphs; ARTEM/STEM (AAAI ×2) add a self-organizing spatial-temporal episodic net for chronological recall; Value-Driven MAG (AAAI) adds utility-based consolidation + a value-governance check.
- **Multi-agent & tool memory**: the LLM-MAS memory survey (PAKDD) explicitly names *synchronization, access control, scalability, alignment, safety* as open; MemTool (ECIR) manages *short-term* tool/MCP context across 100-turn conversations; GraphCogent (WWW) decomposes working memory into sense/buffer/execute across collaborating agents.
- **Memory security/poisoning**: AgentPoison (NeurIPS 2024) is constrained-optimization backdoor trigger injection into RAG/long-term memory; DrunkAgent (WWW 2026) corrupts memory *updates* in recommender agents via transferable triggers.
- **Embodied/multimodal memory**: JARVIS-1 (TPAMI) multimodal memory for Minecraft; HELPER (EMNLP 2023) retrieval of language-program pairs that grows at deployment; AgentCF++ (SIGIR) dual-layer + group-shared memory for cross-domain recommendation.

**Where the structural gaps are.** (i) *Almost every method is write/retrieve-optimistic*: it studies what to store and how to retrieve, but assumes the stored content is true — yet two papers (AgentPoison, DrunkAgent) prove the memory channel is an attack surface, and **no architecture paper here defends its own write path**. (ii) *Evaluation is split*: retrieval accuracy (LoCoMo/LongMemEval) is measured, but **whether a memory operation should have happened at all** (write-worthiness, contradiction with existing memory) is never scored. (iii) *Personalization vs. privacy is bifurcated*: Mem-PAL/MemGuide maximize personalization; the CHI privacy paper wants user control — **nobody measures the personalization cost of honoring a forget/withhold request**. (iv) *Multi-agent memory is surveyed but its named open problems (access control, cross-agent contradiction) have no method paper here*. (v) *Consolidation is treated as compression* (RMM, Value-MAG) but **contradiction-aware consolidation** (new fact conflicts with stored fact) is absent across all clusters.

---

## 2. Ranked Candidate Ideas

Ranking criterion: novelty × cross-cluster leverage × paper-feasibility-without-GPU. All experiments are designed for API-judge + public benchmarks (LongMemEval, LoCoMo) and lightweight local indices (FAISS/BM25), no training required unless noted.

---

### 🏆 Idea 1 — Write-Gate / Memory Admission Control: deciding *whether* to write, not what to evict

- **Thesis**: Agents over-write memory; a lightweight *admission controller* that scores each candidate write for (write-worthiness × non-redundancy × contradiction-with-existing) before it enters the store improves downstream QA *and* shrinks the store, and is the natural defense against poisoning.
- **Gap + which papers**: Sits between the *management* cluster (RMM, Value-MAG, H-MEM — all optimize **post-write** organization/retrieval) and the *security* cluster (AgentPoison, DrunkAgent — both attack the **write** path). No paper here gates the write itself. RMM's prospective reflection *summarizes everything*; Value-MAG consolidates by utility *after* storage. This is the missing pre-store filter.
- **Novelty vs. those papers**: It is **not eviction** (orthogonal to the excluded staleness-gate: that decides what to *remove*; this decides what to *admit*). It unifies a utility signal (Value-MAG) with a contradiction/poison signal (AgentPoison threat model) at write time — a combination none of the 19 attempt.
- **Minimal experiment (no GPU)**: On LongMemEval + LoCoMo, run a standard mem0/RAG agent with and without an admission controller (the controller is an API-judge prompt scoring each candidate write on 3 axes; threshold tuned on a dev split). Metrics: QA accuracy, store size, and — inject AgentPoison-style / DrunkAgent-style trigger writes — attack success rate (ASR). Hypothesis: ≥ baseline QA at much smaller store + large ASR drop. Pure inference + API judge.
- **Feasibility/risk**: High feasibility. Risk: an API-judge admission gate may reject genuinely useful-but-surprising facts (false negatives) — but that *trade-off curve* is itself the publishable finding.
- **Devil's advocate**: "Isn't this just RAG filtering / dedup?" — dedup is similarity-only; the contradiction + poison axes are new and the security framing is the differentiator. Risk it overlaps a concurrent "memory write policy" preprint — needs a Phase-3 novelty check (not possible here). Also: contradiction detection at write time is hard when the conflicting memory isn't retrieved — must retrieve-then-check, adding latency.

---

### Idea 2 — Contradiction-Aware Memory Consolidation (belief revision for agent memory)

- **Thesis**: When a new memory contradicts a stored one (user changed jobs, preference flipped), current agents keep both and retrieve whichever is more similar; an explicit *belief-revision* consolidation step (detect conflict → resolve by recency/source-trust/explicit-confirmation → supersede) raises temporal-reasoning accuracy.
- **Gap + which papers**: Builds on ARTEM/STEM (chronological recall) and "My agent understands me better" (consolidation equation) but both treat consolidation as strengthening/decay, never as *conflict resolution*. LoCoMo explicitly reports LLMs fail at "long-range temporal and causal dynamics" — exactly the symptom of un-revised contradictory memory.
- **Novelty**: Belief revision / truth maintenance applied to agent memory stores. None of the 19 model "this fact supersedes that fact."
- **Minimal experiment**: Curate a contradiction subset from LoCoMo/LongMemEval (or synthesize preference-flip dialogues via API), compare (a) append-only memory, (b) recency-only, (c) belief-revision consolidator (API-judge resolves conflicts and writes a `supersedes` edge). Metric: accuracy on "what is the user's *current* X" questions. No GPU.
- **Feasibility/risk**: High. Risk: building a clean contradiction benchmark is the real work; existing benches under-represent flips.
- **Devil's advocate**: Could be seen as a special case of Idea 1's contradiction axis → keep them distinct (admission vs. revision) or merge into one stronger paper. Synthetic flips may not transfer to real dialogues.

---

### Idea 3 — The Personalization↔Privacy Pareto: cost of forgetting/withholding

- **Thesis**: Honoring a user "forget this" / "don't use this" request degrades personalization measurably; we quantify the Pareto frontier and propose *selective scoping* (per-fact usage policy) that recovers most utility at a given privacy level.
- **Gap + which papers**: Directly bridges the two halves nobody connects: Mem-PAL + MemGuide (maximize personalization) vs. "Towards Usable, Privacy Respecting LTM" (CHI — wants user controls but no utility measurement). The CHI paper is a thesis proposal with *no metric* for the personalization cost.
- **Novelty**: First quantitative privacy-utility trade-off for agent long-term memory with an actionable mechanism (scoped memory tags), not just an interface study.
- **Minimal experiment**: On a personalization benchmark (PAL-style or LongMemEval personalization split), apply graduated forget/withhold policies to stored facts and measure personalized-response quality (API-judge) vs. fraction withheld. Compare naive deletion vs. usage-scoping (fact retained for safety/consistency but blocked from generation). No GPU.
- **Feasibility/risk**: Medium-high. Risk: defining "personalization quality" cleanly; needs a defensible API-judge rubric.
- **Devil's advocate**: Reviewers may call it "obvious that deleting data hurts personalization" — the contribution must be the *mechanism* (scoping > deletion) and the shape of the curve, not the existence of a trade-off. PAL-Set is Chinese-only; English transfer untested.

---

### Idea 4 — Cross-Agent Memory Contradiction & Trust in Multi-Agent Systems

- **Thesis**: When agents share memory, one agent's wrong/poisoned write propagates; a *provenance + cross-agent consistency check* (each shared memory carries source-agent + confidence; consumers down-weight low-trust or contradicted entries) limits error propagation without killing collaboration gains.
- **Gap + which papers**: The LLM-MAS memory survey names *access control, alignment, safety* as open with **no method**; AgentPoison/DrunkAgent show single-agent poisoning; GraphCogent/AgentCF++ use shared/group memory but assume it's trustworthy. The intersection (poisoning *in shared* memory) is empty.
- **Novelty**: First study of poison/error *propagation through shared agent memory* + a provenance-trust defense.
- **Minimal experiment**: Small simulated MAS (3–5 API agents) with a shared store on a collaborative QA task; inject a poisoned/wrong write from one agent; measure team accuracy with vs. without provenance-trust weighting, and propagation depth. No GPU (API agents only).
- **Feasibility/risk**: Medium. Risk: building a credible MAS testbed from scratch is effort-heavy; results sensitive to orchestration choices.
- **Devil's advocate**: Could read as "federated trust 101 applied to LLMs." Differentiation = the empirical propagation dynamics + that contradicted-but-confident writes are the worst case. Reproducibility of MAS results is a known reviewer worry.

---

### Idea 5 — Audit: Does intent/structure-aware retrieval survive distractor & adversarial memory?

- **Thesis**: MemGuide (intent-driven) and H-MEM (index routing) beat similarity retrieval on clean stores — but their advantage may collapse when the store contains distractor or adversarial entries; a stress-test audit reveals which retrieval paradigm is robust.
- **Gap + which papers**: Pure cross-paper diagnostic over MemGuide, H-MEM, RMM (RL retrieval) and the security cluster. Each method is evaluated on clean stores only; robustness ranking is unknown.
- **Novelty**: A *contribution-type = diagnostic* paper; negative or surprising result is equally publishable. Nobody has stress-tested these 2025–26 retrievers head-to-head under contamination.
- **Minimal experiment**: Reimplement/approximate similarity-RAG, intent-rerank (MemGuide-style API reranker), and index-route (H-MEM-style) over LongMemEval; progressively inject distractors + AgentPoison-style triggers; plot accuracy vs. contamination ratio. No GPU.
- **Feasibility/risk**: High feasibility (all inference). Risk: faithful reimplementation of H-MEM's routing from abstract alone is approximate — must caveat.
- **Devil's advocate**: Audits can be seen as low-novelty if the answer is "more structure = more robust." Mitigate by including the *failure modes* and a cheap fix. Approximate reimplementations invite "not the real method" critiques.

---

### Idea 6 — Write-worthiness as a first-class benchmark axis (eval, not method)

- **Thesis**: Every benchmark here (LoCoMo, LongMemEval, PAL-Bench, MS-TOD, MediLongChat) scores *retrieval/QA* but never scores *whether the agent wrote the right things*. We define precision/recall-of-writes and show retrieval scores can be gamed by write-everything policies.
- **Gap + which papers**: Meta-level over the entire conversational + management clusters. RMM "summarizes everything," MemoryART builds episodic stores — none report write-precision; the field optimizes a downstream metric blind to store quality.
- **Novelty**: New evaluation dimension + the demonstration that current leaderboards reward hoarding.
- **Minimal experiment**: Annotate (API-judge + spot human check) gold "should-store" units on a LoCoMo/LongMemEval slice; compute write-precision/recall for several memory agents; correlate with store size and QA. Show a hoarding baseline tops QA while having terrible write-precision and huge cost. No GPU.
- **Feasibility/risk**: High. Risk: gold "should-store" labels are subjective — need inter-annotator agreement on a small set.
- **Devil's advocate**: Reviewers may want a method, not just a metric; pair it with Idea 1 (admission control) as the method that the metric rewards → a stronger combined paper. Subjectivity of gold writes is the main attack.

---

### Idea 7 — Memory-cost-aware serving: token/latency budget as a constraint on memory ops

- **Thesis**: Memory papers report accuracy and sometimes token savings (MemoryART, GraphCogent) but never frame memory management as *accuracy under a hard token/latency budget*; a budget-constrained controller chooses how much to retrieve/consolidate per turn.
- **Gap + which papers**: Builds on MemTool (short-term tool-context efficiency) and MemoryART/GraphCogent (token reduction as a side effect) — none treat the per-turn memory budget as the optimization target.
- **Novelty**: Reframes memory as a constrained resource-allocation problem at inference.
- **Minimal experiment**: On LongMemEval, sweep retrieval/consolidation depth; plot accuracy vs. token budget for fixed agents; add a simple budget-aware policy and show Pareto improvement. No GPU.
- **Feasibility/risk**: Medium. Risk: overlaps general RAG-efficiency literature *outside* this set — high concurrent-work risk; needs the Phase-3 novelty check that's unavailable here. ⚠️ Also adjacent in spirit to the excluded cache-aware router (constraint-driven), though different object (memory ops, not skill DAG/KV-cache). Flagged, kept low.
- **Devil's advocate**: Most likely to already exist in the broader efficient-RAG world. Lowest novelty confidence of the set.

---

## 3. Eliminated / Too-Close

| Idea considered | Verdict | Reason |
|---|---|---|
| Add a third/fourth eviction-scoring axis (e.g., "surprise", "emotional salience") to long-term memory | **KILLED** | Directly the excluded *staleness-gate* family — "yet another what-to-evict axis." Not orthogonal. |
| Cache/prefix-aware memory retrieval planner to maximize KV-cache hit-rate across memory reads | **KILLED** | Near-duplicate of excluded *cache-aware skill router* (KV-cache-constrained planning). |
| "Apply ART / engram graphs to a new domain (legal/finance)" | **KILLED** | Pure "apply X to Y" — MemoryART/PromptX already establish the mechanism; new domain alone isn't a contribution. |
| Better embedding model for memory retrieval on LoCoMo | **KILLED** | Incremental; reviewers won't care; orthogonal to the architectural gaps. |
| Yet another hierarchical memory layout vs. H-MEM/Mem-PAL | **KILLED** | Crowded; marginal delta over two 2026 papers; no clear new axis. |
| New very-long-dialogue benchmark like LoCoMo-but-longer | **DEPRIORITIZED** | LoCoMo/LongMemEval/MediLongChat already saturate the "longer dialogue" framing; a new *axis* (Idea 6 write-quality) is stronger than a new length record. |
| Pure interface/privacy-controls user study | **FOLDED** | Subsumed into Idea 3 with a quantitative metric, which is the publishable upgrade over the CHI proposal. |

---

## 4. Top Recommendation

**Idea 1 (Write-Gate / Memory Admission Control)** — it is the single point where three clusters intersect (management, security, evaluation), it is provably absent across all 19 papers, it is fully runnable with API-judge + LongMemEval/LoCoMo and no GPU, and it produces a publishable result either way (a clean QA-vs-store-size-vs-ASR trade-off). Strongest move: pair it with **Idea 6** (write-worthiness metric) so the paper ships both the metric that exposes hoarding *and* the mechanism that fixes it, and with **Idea 2**'s contradiction axis as the security-relevant write check.

**Caveat**: novelty here is confirmed only at the abstract level of these 19 papers. A real `/novelty-check` against the broader 2025–26 preprint stream (not possible in this no-API-budget run) is required before committing — Idea 7 and the write-policy framing of Idea 1 carry the highest concurrent-work risk.
