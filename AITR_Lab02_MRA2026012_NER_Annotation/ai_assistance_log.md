# AI Assistance Log — AITR Lab 02

**Student:** Vyom Sutariya | MRA2026012 | Dept. of IT (Robotics and AI)  
**Lab:** AITR Lab 02 — Comparative NER Annotation Study  
**Tool used throughout:** Antigravity (powered by Google DeepMind Gemini)  
**Date:** November 2026

---

> **Purpose of this log:** Academic transparency record of every AI-assisted step in this project, documenting what the AI proposed, what the researcher accepted/modified/rejected, and how each output was verified before use.

---

## Entry 1: Dataset Construction

| Field | Detail |
|---|---|
| **Task** | Create a representative biomedical NER dataset embedded in Python |
| **Tool** | Antigravity (Gemini) |
| **Prompt summary** | "Generate 180 BIO-tagged sentences with disease entity annotations using NCBI Disease corpus vocabulary. Include varied clinical and epidemiological contexts. Target ~30% entity tokens." |
| **AI proposal** | Generated 180 sentence templates with BIO-tagged disease entities; proposed disease name list drawn from NCBI Disease vocabulary (Huntington disease, breast cancer, Alzheimer disease, cystic fibrosis, etc.); included varied contexts (clinical description, gene association, treatment mention, epidemiology) |
| **Human decision** | Reviewed all generated sentences; cross-checked disease names against NCBI Disease corpus documentation and OMIM; removed two fictitious disease names inserted by AI ("Ventriculopathy syndrome", "Neuronal dysplasia type IV"); added 8 additional multi-token entities (e.g., "amyotrophic lateral sclerosis", "systemic lupus erythematosus") that the AI had abbreviated or omitted; corrected 4 BIO-tagging errors where the AI had tagged I-Disease at sentence start without a preceding B-Disease |
| **Verification** | Manual review of 20% random sample (36 sentences); confirmed BIO consistency (no I-Disease without prior B-Disease or I-Disease; no crossing spans); spot-checked 10 disease names against NCBI Disease corpus |
| **Outcome** | Dataset with 180 sentences, verified disease names, correct BIO annotation, ~30% entity tokens; saved as `data/ncbi_disease_subset.py` |
| **AI contribution** | High — generated the bulk of sentences and initial disease term list |
| **Researcher contribution** | Verification, correction of BIO errors, removal of fictitious terms, addition of complex multi-token entities |

---

## Entry 2: CRF Feature Engineering

| Field | Detail |
|---|---|
| **Task** | Design token feature functions for CRF and LR NER models |
| **Tool** | Antigravity (Gemini) |
| **Prompt summary** | "Suggest feature functions for a CRF NER model following standard NLP practice. Features should be suitable for biomedical text." |
| **AI proposal** | Suggested: word identity, lowercased word, suffix (last 3, 2, 1 chars), prefix (first 3 chars), `isupper`, `istitle`, `isdigit`, context window ±2 (previous and next words) |
| **Human decision** | Accepted the core feature set; additionally added: (a) `word_shape` feature (maps characters to their type, e.g., "Huntington" → "Aa+") — not in AI proposal but known to improve NER on biomedical proper nouns; (b) explicit BOS/EOS (beginning/end-of-sentence) indicators — standard in CRF implementations but omitted by AI; verified the full set against Lafferty et al. 2001 and sklearn-crfsuite documentation examples |
| **Verification** | Compared final feature set with the sklearn-crfsuite tutorial (Choi 2016) example feature template; confirmed all standard features are present; ran a sanity check confirming that feature dicts are non-empty for all tokens in a test sentence |
| **Outcome** | Feature extraction module `src/features.py` implementing `word_features()`, `sentence_to_crf_features()`, and `get_X_y_for_lr()`; feature set matching NLP community standard |
| **AI contribution** | Medium — provided the standard starting set |
| **Researcher contribution** | Added word_shape and BOS/EOS; verified against literature |

---

## Entry 3: Evaluation Code

| Field | Detail |
|---|---|
| **Task** | Implement evaluation metrics for sequence labelling (NER) |
| **Tool** | Antigravity (Gemini) |
| **Prompt summary** | "Write evaluation code for a NER system. Compute precision, recall, and F1 for biomedical NER output." |
| **AI proposal** | Initial code used `sklearn.metrics.accuracy_score` and `sklearn.metrics.f1_score` with `average='macro'` on flattened token-level predictions — which is incorrect for NER evaluation (inflated by O-class majority, does not account for entity span boundaries) |
| **Human decision** | Rejected the AI proposal entirely; replaced with `seqeval.metrics.precision_score`, `seqeval.metrics.recall_score`, and `seqeval.metrics.f1_score` — which operate at the entity span level, requiring correct B-/I- boundary detection for a true positive. This directly addresses Review Gap 6.1 (standardised evaluation). The `save_metrics_csv` and `save_ablation_csv` helper functions were also authored by the researcher without AI assistance. |
| **Verification** | Manually constructed a known example: 2 sentences with 1 entity each; computed expected entity-level precision=1.0, recall=1.0, F1=1.0 for a perfect predictor; confirmed seqeval output matched; tested a deliberately wrong prediction to confirm F1 drops correctly |
| **Outcome** | `src/evaluation.py` with correct entity-level evaluation pipeline using seqeval |
| **AI contribution** | Low — the AI proposal was incorrect and was rejected |
| **Researcher contribution** | Complete rewrite using seqeval; design of verification test case |

---

## Entry 4: Ablation Study Design

| Field | Detail |
|---|---|
| **Task** | Design a training data ablation protocol to study annotation efficiency |
| **Tool** | Antigravity (Gemini) |
| **Prompt summary** | "Design an ablation study on training data size for comparing NER methods. We want to understand how performance degrades as labelled data is reduced." |
| **AI proposal** | Suggested random subsampling of the training set at fractions [0.1, 0.25, 0.5, 1.0]; no mention of seed control or reproducibility mechanism |
| **Human decision** | Accepted the fraction choices (they span two orders of magnitude and align with Review Gap 6.3); added explicit seed control: `numpy.random.default_rng(42).choice(...)` with a fixed seed per fraction — ensuring the same sentences are selected across two independent runs; excluded Dictionary NER from the ablation (zero-shot, constant across fractions) but retained it as a horizontal reference line in the visualisation |
| **Verification** | Ran the subsampling function twice with seed=42 on a test sentence list; confirmed identical sentence sets selected on both runs for all four fractions |
| **Outcome** | Reproducible ablation protocol embedded in `scripts/run_experiment.py`; results saved to `results/ablation.csv` |
| **AI contribution** | Medium — fraction choices and overall design |
| **Researcher contribution** | Seed control mechanism, exclusion logic for Dictionary NER, verification of reproducibility |

---

## Entry 5: Visualisation

| Field | Detail |
|---|---|
| **Task** | Create publication-quality result figures from experiment output CSVs |
| **Tool** | Antigravity (Gemini) |
| **Prompt summary** | "Write matplotlib code to produce: (1) a grouped bar chart comparing Precision/Recall/F1 across 3 NER methods; (2) a line plot showing F1 vs. training fraction for LR and CRF." |
| **AI proposal** | Generated basic matplotlib code: `plt.bar()` for grouped bars with default colours; `plt.plot()` for line plot; no error bars; default axis labels; no style customisation |
| **Human decision** | Used the AI code as a scaffold; made the following modifications: (a) switched to a colourblind-friendly palette (blue/orange/green per method, consistent across both figures); (b) added `plt.tight_layout()` and adjusted figure size to 8×5 inches for publication aspect ratio; (c) improved axis labels ("F1 Score (entity-level, seqeval)", "Training Fraction"); (d) added a horizontal dashed reference line for Dictionary NER F1 in Figure 2; (e) added grid lines (`alpha=0.3`) for readability; (f) set `dpi=150` for high-resolution export |
| **Verification** | Visual inspection: confirmed axis scales are correct (y from 0.0 to 1.0); confirmed legend correctly maps colours to methods; confirmed figure 2 x-axis ticks match fraction values [0.10, 0.25, 0.50, 1.00] |
| **Outcome** | `results/figure1_comparison.png` and `results/figure2_ablation.png`; publication-quality at 150 dpi |
| **AI contribution** | Medium — provided the structural scaffolding code |
| **Researcher contribution** | Style, accessibility (colourblind palette), axis labelling, reference line, verification |

---

## Summary Table

| Entry | Task | AI Role | Researcher Role | AI Contribution Level |
|---|---|---|---|---|
| 1 | Dataset Construction | Generated sentences & term list | Reviewed, corrected BIO errors, removed fictitious terms | High |
| 2 | CRF Feature Engineering | Provided standard feature set | Added word_shape & BOS/EOS; verified against literature | Medium |
| 3 | Evaluation Code | Proposed (incorrect) token-level metrics | Rejected; rewrote with seqeval entity-level metrics | Low |
| 4 | Ablation Study Design | Suggested fraction choices | Added seed control; verified reproducibility | Medium |
| 5 | Visualisation | Provided matplotlib scaffold | Styling, accessibility, axis labels, verification | Medium |

> **Academic integrity note:** All AI-generated content in this project was reviewed, verified, and in several cases corrected or rejected by the researcher before use. The AI served as a productivity tool, not an autonomous research agent. The research question, experimental design, methodology decisions, and all verification steps were performed by the researcher.
