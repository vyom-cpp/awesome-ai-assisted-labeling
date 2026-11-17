# Research Decisions Log — AITR Lab 02

**Student:** Vyom Sutariya | MRA2026012 | Dept. of IT (Robotics and AI)  
**Lab:** AITR Lab 02 — Comparative NER Annotation Study  
**Date:** November 2026

---

## 1. From Review to Research Question

### Review Gaps that Motivated This Study

Lab 01 ("Comparing AI-Assisted and Manual Data Labelling Accuracy on Scientific Datasets: A Thematic Review") identified four research gaps. Three of them directly motivate the Lab 02 experimental design:

**Gap 6.1 — Lack of Standardised Evaluation Metrics**
> The reviewed studies used heterogeneous evaluation protocols (token-level accuracy, entity-level F1, agreement-based κ), making cross-method comparison unreliable. No single benchmark NER dataset was consistently used to compare AI-assisted, manual, and hybrid annotation pipelines.

*Implication for Lab 02:* A single, standardised public corpus (NCBI Disease) with a single evaluation library (seqeval entity-level F1) must be used to enable fair cross-method comparison.

**Gap 6.2 — Limited Domain-Specific Validation**
> Most reviewed pipelines were validated on general-domain corpora (CoNLL-2003, OntoNotes). Biomedical NER — where terminology is dense, multi-token, and highly specialised — remained underexplored for the AI-vs-manual comparison axis.

*Implication for Lab 02:* Biomedical disease NER on the NCBI Disease corpus directly fills this gap, extending the review's findings into a clinically relevant domain.

**Gap 6.3 — Limited Understanding of Human-AI Collaboration Efficiency**
> The reviews found no systematic study of how annotation quality degrades as labelled data decreases. The practical question — "how few labels does an AI-assisted method need to match a fully-supervised baseline?" — was unanswered.

*Implication for Lab 02:* An ablation study over training fractions (10%, 25%, 50%, 100%) operationalises this gap into a measurable experiment.

### Transition: Gap → Research Question → Experimental Design

| Review Gap | Research Question Component | Experimental Handle |
|---|---|---|
| 6.1 (standardised evaluation) | Fair cross-method comparison | seqeval F1 on shared test set |
| 6.2 (domain-specific validation) | Biomedical disease NER | NCBI Disease corpus |
| 6.3 (annotation efficiency) | Performance vs. label quantity | Training fraction ablation |

**Research Question (Lab 02):**
> *"Does CRF-based NER outperform dictionary-based weak supervision and logistic-regression classifiers for biomedical disease NER, and how does annotation efficiency degrade as labelled data is reduced?"*

This question is not arbitrary — it is a direct operationalisation of Gaps 6.1–6.3 from the Lab 01 review.

---

## 2. Decision Log

### Decision 1: Dataset Selection — NCBI Disease Corpus

| Field | Detail |
|---|---|
| **Decision** | Use the NCBI Disease corpus as the benchmark dataset |
| **Reasoning** | Standard public benchmark for biomedical disease NER; uses the BIO annotation scheme (B-Disease, I-Disease, O); disease recognition is a well-defined, clinically relevant NER task with clear entity boundaries |
| **Review Linkage** | Hu et al. 2024 [3] uses comparable biomedical NER benchmarks (MedMentions, BC5CDR); adopting NCBI Disease follows the same validation tradition while providing a freely accessible, public-domain corpus |
| **Alternative Considered** | BC5CDR (larger, chemical+disease); rejected because it conflates two entity types, adding complexity that is orthogonal to the annotation-method comparison axis |
| **Status** | ✅ **VERIFIED** — NCBI Disease corpus is publicly available at https://www.ncbi.nlm.nih.gov/CBBresearch/Dogan/DISEASE/; citation: Dogan et al. 2014 |

---

### Decision 2: Method Selection and Review Taxonomy Mapping

| Field | Detail |
|---|---|
| **Decision** | Compare three NER methods: Dictionary NER, Logistic Regression NER, CRF NER |
| **Review Taxonomy** | The Lab 01 review (Section 2, Figure 1) classifies annotation methods as: Fully Manual, Weak Supervision, ML-Assisted, Hybrid/HITL |

**Mapping:**

| Method | Review Taxonomy Category | Justification |
|---|---|---|
| Dictionary NER | Weak Supervision | Rule-based, zero-label, equivalent to a Snorkel-style labelling function (Ratner et al. 2017); no learned parameters; same position as rule-based pre-labelling in the HITL literature (Budd et al. 2021 [1]) |
| Logistic Regression NER | AI-Assisted Annotation (ML-based) | Supervised ML with handcrafted features; directly comparable to the "AI-Assisted" category in the review; requires labelled training data but no sequence modelling |
| CRF NER | Hybrid / HITL Pre-labelling | Sequence model with transition features; standard pre-neural NER baseline (Lafferty et al. 2001); in HITL pipelines, CRF is used for pre-annotation before human review — aligning with Budd et al. 2021 [1] Section 3.2 |

| **Status** | ✅ **VERIFIED** against review taxonomy (Section 2 of Lab 01 report) |

---

### Decision 3: Ablation Study on Training Fraction

| Field | Detail |
|---|---|
| **Decision** | Run each supervised method (LR, CRF) on training fractions: 10%, 25%, 50%, 100% |
| **Motivation** | Review Gap 6.3 — "limited understanding of how annotation quality and efficiency change as labelled data is reduced in human-AI collaborative settings" |
| **Fraction Rationale** | 10% ≈ minimal annotation budget (12–13 sentences); 25% ≈ small-data regime; 50% ≈ moderate budget; 100% = full supervision; four points enable curve-fitting |
| **Dictionary NER excluded** | Dictionary NER is zero-shot (no training labels); its performance is constant across fractions and is plotted as a horizontal reference line |
| **Status** | ✅ **INFERRED** — Gap 6.3 is stated in the review; exact fractions chosen by researcher to span two orders of magnitude |

---

### Decision 4: Evaluation Protocol

| Field | Detail |
|---|---|
| **Decision** | Use seqeval entity-level Precision, Recall, F1 |
| **Reasoning** | Token-level accuracy is misleading for NER (inflated by majority O-class); seqeval computes metrics at the entity span level, requiring correct B-/I- boundary detection |
| **Review Linkage** | Addresses Gap 6.1 (standardised evaluation); Hu et al. 2024 [3] and Sushil et al. 2024 [5] both use entity-level F1 |
| **Status** | ✅ **VERIFIED** — seqeval is the community standard for sequence labelling evaluation (Nakayama 2018); `pip install seqeval` |

---

### Decision 5: Train/Validation/Test Split — 70/15/15, seed=42

| Field | Detail |
|---|---|
| **Decision** | Stratified random split: 70% train, 15% validation, 15% test; random_state=42 |
| **Reasoning** | 70/15/15 is a standard split for small-to-medium NLP datasets; validation set reserved for hyperparameter tuning (not used in final metrics); test set held out and identical for all three methods |
| **Seed Rationale** | seed=42 is a widely used conventional value ensuring reproducibility across runs and environments |
| **Status** | ✅ **INFERRED** — standard split convention; seed chosen explicitly for reproducibility |
