# Baseline Validation Report — AITR Lab 02

**Student:** Vyom Sutariya | MRA2026012 | Dept. of IT (Robotics and AI)  
**Lab:** AITR Lab 02 — Comparative NER Annotation Study  
**Date:** November 2026

---

## Overview

This document validates the three NER baselines implemented in `src/baselines.py` against:
1. Their theoretical description in the literature
2. Their mapping to the Lab 01 review taxonomy
3. The comparison protocol ensuring a fair evaluation

---

## Method 1: Dictionary NER

### Description
Greedy longest-match dictionary lookup against a hardcoded list of ~120 disease terms. For each sentence, the algorithm scans left-to-right; at each position it checks for the longest matching term in the dictionary, assigns B-Disease to the first token and I-Disease to subsequent tokens, then advances past the matched span. All remaining tokens receive label O.

### Implementation Details
- **Dictionary size:** ~120 terms (single-token and multi-token)
- **Terms sourced from:** NCBI Disease corpus vocabulary; standard biomedical disease nomenclature (OMIM, MeSH headings)
- **Match type:** Case-insensitive exact string match
- **Multi-word handling:** Greedy longest-match (e.g., "breast cancer" matched before "cancer")
- **Training required:** None (zero-shot)

### Validation Checks
| Check | Result |
|---|---|
| Disease terms cross-checked against NCBI Disease corpus vocabulary | ✅ Pass |
| Multi-token terms produce correct B-/I- sequence | ✅ Pass |
| No entity begins with I-Disease (BIO consistency) | ✅ Pass |
| Output labels are a subset of {B-Disease, I-Disease, O} | ✅ Pass |

### Limitations
- **No context modelling:** Cannot disambiguate "cancer" (disease) from "Cancer Research" (journal)
- **Exact match only:** Misses morphological variants (e.g., "diabetic" vs. "diabetes"), abbreviations, and misspellings
- **Recall ceiling:** Performance bounded by dictionary coverage; novel disease mentions are always missed
- **Precision ceiling:** Any disease term appearing in a non-clinical context is a false positive

### Review Taxonomy Mapping
- **Category:** Weak Supervision (Lab 01 review, Section 2)
- **Equivalent to:** Snorkel-style labelling function (Ratner et al. 2017); rule-based pre-annotation in HITL pipelines (Budd et al. 2021 [1], Section 3.1)
- **Expected F1 range:** 0.40–0.65 (review reports 0.70–0.82 for autonomous AI; dictionary methods typically underperform full ML)

### Status
✅ **VERIFIED** as a weak supervision baseline; correctly implements greedy longest-match BIO tagging with no learned parameters.

---

## Method 2: Logistic Regression NER

### Description
Token-level multi-class logistic regression classifier. Each token is independently classified into {B-Disease, I-Disease, O} based on a handcrafted feature vector. No sequence context is modelled; each token's prediction is conditionally independent of its neighbours' labels.

### Implementation Details
- **Classifier:** `sklearn.linear_model.LogisticRegression(max_iter=1000, C=1.0, random_state=42, solver='lbfgs', multi_class='auto')`
- **Feature vectoriser:** `sklearn.feature_extraction.DictVectorizer` (sparse output)
- **Training:** Supervised; requires labelled (token, label) pairs

### Feature Set

| Feature | Description |
|---|---|
| `word` | Raw word string |
| `word.lower()` | Lowercased word |
| `word[-3:]` | Last 3 characters (suffix) |
| `word[-2:]` | Last 2 characters |
| `word[-1:]` | Last 1 character |
| `word[:3]` | First 3 characters (prefix) |
| `word.isupper()` | All uppercase flag |
| `word.istitle()` | Title case flag |
| `word.isdigit()` | Digit flag |
| `word_shape` | Character shape (e.g., "Xxxxxxx" → "Aa+") |
| `bias` | Constant bias term |
| `BOS` | Beginning-of-sentence indicator |
| `EOS` | End-of-sentence indicator |
| `prev1_word`, `prev2_word` | Context window: words at positions i-1, i-2 |
| `next1_word`, `next2_word` | Context window: words at positions i+1, i+2 |

### Validation
- Feature set is comparable to the pre-neural NER literature (Settles 2004; Chieu & Ng 2002)
- Context window ±2 is standard for token-level NER feature engineering
- Case features (isupper, istitle) are known to be predictive for named entity recognition

### Limitation
- **No sequence modelling:** Each token's label is predicted independently; the model cannot learn transition constraints (e.g., I-Disease cannot follow O)
- **Sparse representation:** High-dimensional one-hot feature space; may underfit on small training sets
- **Independent predictions:** Can produce invalid BIO sequences (e.g., I-Disease at sentence start)

### Review Taxonomy Mapping
- **Category:** AI-Assisted Annotation (ML-based) — Lab 01 review, Section 2
- **Expected F1 range:** Intermediate between dictionary and CRF; typically 0.55–0.75 for biomedical NER

### Status
✅ **VERIFIED** as an ML-assisted baseline; standard logistic regression NER with handcrafted features matching pre-neural NLP practice.

---

## Method 3: CRF NER

### Description
Linear-chain Conditional Random Field (CRF) with the same feature set as the LR model, plus learned label transition features. CRF models the joint probability of the full label sequence given the input, enabling it to learn constraints such as "I-Disease must follow B-Disease or I-Disease".

### Implementation Details
- **Library:** `sklearn_crfsuite.CRF`
- **Algorithm:** `lbfgs` (L-BFGS, a quasi-Newton optimiser)
- **Regularisation:** L1 coefficient c1=0.1; L2 coefficient c2=0.1
- **Max iterations:** 100
- **all_possible_transitions:** True (learns transitions for all label pairs, including unseen ones)
- **Feature set:** Identical to LR (see table above) + automatically learned transition features

### Validation
| Check | Result |
|---|---|
| CRF is the standard pre-neural NER method (Lafferty et al. 2001) | ✅ Confirmed |
| `sklearn_crfsuite` follows the original CRF formulation | ✅ Confirmed |
| L-BFGS optimiser is the standard for CRF training | ✅ Confirmed |
| c1/c2 regularisation values match sklearn-crfsuite documentation defaults | ✅ Confirmed |
| `all_possible_transitions=True` ensures full transition matrix | ✅ Confirmed |

### Deviations from Canonical CRF Literature
| Aspect | Lafferty et al. 2001 / Standard | This Implementation |
|---|---|---|
| Optimiser name | "L-BFGS-B" (bounded) | `lbfgs` in sklearn_crfsuite (equivalent unbounded; constraints enforced by regularisation) |
| Regularisation | Various | c1=0.1 (L1), c2=0.1 (L2) — standard sklearn-crfsuite defaults |
| Feature template | Manual template specification | Dict-based features (computationally equivalent) |

These deviations are minor and do not affect the validity of the method as a CRF NER baseline.

### Review Taxonomy Mapping
- **Category:** Hybrid / HITL Pre-labelling — Lab 01 review, Section 2, Figure 1
- **Justification:** In HITL pipelines, CRF is widely used for pre-annotation before human correction (Budd et al. 2021 [1], Section 3.2); CRF's sequence modelling capability approximates the "pre-labelling" step in human-in-the-loop systems
- **Expected F1 range:** 0.70–0.85 for biomedical disease NER; review cites HITL systems achieving 0.88–0.95 F1 with full human review

### Status
✅ **VERIFIED** as a HITL pre-labelling proxy; correctly implements sklearn-crfsuite CRF with standard regularisation and feature set.

---

## Comparison Protocol Validation

The following checks ensure a fair, unconfounded comparison across all three methods:

| Protocol Requirement | Implementation | Status |
|---|---|---|
| Same test set for all methods | Single stratified split with seed=42; test set fixed before any training | ✅ |
| Same feature extraction for LR and CRF | Both use `word_features()` from `src/features.py` | ✅ |
| Dictionary NER uses no training data | `DictionaryNER.predict()` requires no `fit()` call | ✅ |
| Seed fixed at 42 for all stochastic steps | `random_state=42` in `LogisticRegression`; `seed=42` in all subsampling | ✅ |
| Metrics computed with seqeval (entity-level, not token-level) | `seqeval.metrics.f1_score` with `average='weighted'` | ✅ |
| Ablation uses same test set across all fractions | Test set isolated before ablation loop begins | ✅ |
| No test-set information leakage into training | No feature normalisation computed on test set; dictionary not tuned on test set | ✅ |

---

## References

- Lafferty, J., McCallum, A., & Pereira, F. (2001). Conditional random fields: Probabilistic models for segmenting and labeling sequence data. *ICML 2001*.
- Dogan RI, Leaman R, Lu Z. (2014). NCBI disease corpus: A resource for disease name recognition and normalization. *J Biomed Inform*, 47:1–10.
- Budd, J. et al. (2021). A survey on active learning and human-in-the-loop deep learning for medical image analysis. *Medical Image Analysis*. [1]
- Hu, Y. et al. (2024). Advancing medical NER with large language models. [3]
- Nakayama, H. (2018). seqeval: A Python framework for sequence labeling evaluation.
