# AITR Lab 02 — Comparative NER Annotation Study

**Student:** Vyom Sutariya | MRA2026012 | Dept. of IT (Robotics and AI)  
**Programme:** M.Tech Robotics and AI (MRA), AITR  
**Lab:** 02 — Controlled Comparative Study (Pathway B)  
**Academic year:** 2025–26

---

## Research Question

> *Does CRF-based NER outperform dictionary-based weak supervision and logistic-regression classifiers for biomedical disease NER, and how does annotation efficiency degrade as labelled data is reduced?*

This question is a direct operationalisation of research gaps 6.1–6.3 identified in the Lab 01 thematic review: *"Comparing AI-Assisted and Manual Data Labelling Accuracy on Scientific Datasets"*.

---

## Quick Start

### Prerequisites

Python 3.9+ required. Install dependencies:

```bash
pip install scikit-learn numpy pandas matplotlib scipy sklearn-crfsuite seqeval
```

### Run the full experiment

```bash
# From the project root
cd /path/to/AITR_Lab02_MRA2026012_NER_Annotation

# Run all three methods + ablation study
python scripts/run_experiment.py

# Generate figures (after experiment completes)
python scripts/plot_results.py
```

Results are saved to the `results/` directory.

---

## Repository Structure

```
AITR_Lab02_MRA2026012_NER_Annotation/
│
├── README.md                    ← This file
├── research_decisions.md        ← Decision log: how gaps → research question → design
├── baseline_validation.md       ← Method validation against literature
├── ai_assistance_log.md         ← Transparency log of AI tool usage
│
├── data/
│   ├── README.md                ← Dataset documentation
│   └── ncbi_disease_subset.py   ← Embedded 180-sentence BIO-tagged dataset
│
├── src/
│   ├── features.py              ← Feature extraction (word_features, CRF features, LR vectoriser)
│   ├── baselines.py             ← Three NER classes: DictionaryNER, LogRegNER, CRFNER
│   └── evaluation.py            ← seqeval-based metrics; CSV export helpers
│
├── scripts/
│   ├── run_experiment.py        ← Main experiment: trains, evaluates, runs ablation
│   └── plot_results.py          ← Reads CSVs; produces figure1 and figure2
│
├── configs/
│   └── experiment_config.json   ← Experiment parameters (seed, splits, fractions)
│
├── results/
│   ├── metrics.csv              ← Method × Precision/Recall/F1 (full training set)
│   ├── ablation.csv             ← Method × Fraction × Precision/Recall/F1
│   ├── figure1_comparison.png   ← Grouped bar chart: 3 methods × 3 metrics
│   └── figure2_ablation.png     ← Line plot: F1 vs. training fraction (LR, CRF)
│
├── notebooks/
│   └── (exploratory notebooks, if any)
│
└── paper/
    └── (lab report / paper draft)
```

---

## Methods

| Method | Category (Lab 01 Taxonomy) | Description |
|---|---|---|
| **Dictionary NER** | Weak Supervision | Greedy longest-match against ~120 hardcoded disease terms; zero-shot, no training |
| **Logistic Regression NER** | AI-Assisted (ML-based) | Token-level LR classifier with handcrafted lexical features; independently classifies each token |
| **CRF NER** | Hybrid / HITL Pre-labelling | sklearn-crfsuite CRF with identical features + learned label transition constraints; standard pre-neural NER baseline (Lafferty et al. 2001) |

---

## Experiment Reproduction

### Step 1 — Verify installation

```bash
python -c "import sklearn, sklearn_crfsuite, seqeval, pandas, matplotlib; print('All dependencies OK')"
```

### Step 2 — Run the experiment

```bash
python scripts/run_experiment.py
```

This script:
1. Loads 180 sentences from `data/ncbi_disease_subset.py`
2. Splits into train (70%) / val (15%) / test (15%) with `random_state=42`
3. Trains and evaluates DictionaryNER, LogRegNER, and CRFNER on the full training set
4. Runs the ablation study: LR and CRF on training fractions [10%, 25%, 50%, 100%]
5. Prints formatted result tables to stdout
6. Saves `results/metrics.csv` and `results/ablation.csv`

### Step 3 — Generate figures

```bash
python scripts/plot_results.py
```

Produces:
- `results/figure1_comparison.png` — grouped bar chart (Precision / Recall / F1 per method)
- `results/figure2_ablation.png` — F1 vs. training fraction line plot (LR vs. CRF; Dictionary as reference)

### Step 4 — Inspect results

```bash
cat results/metrics.csv
cat results/ablation.csv
```

---

## Results

> **See `results/` folder after running the experiment.**

The experiment produces:
- `results/metrics.csv` — entity-level Precision, Recall, F1 for each method on the held-out test set
- `results/ablation.csv` — F1 at each training fraction for LR and CRF
- `results/figure1_comparison.png` — visualisation of method comparison
- `results/figure2_ablation.png` — visualisation of annotation efficiency degradation

Expected outcome (based on literature): CRF > LR > Dictionary NER for entity-level F1; both LR and CRF degrade significantly below 25% training fraction.

---

## Configuration

Experiment parameters are centralised in `configs/experiment_config.json`:

```json
{
  "random_seed": 42,
  "test_size": 0.15,
  "val_size": 0.15,
  "train_fractions": [0.1, 0.25, 0.5, 1.0],
  "lr_params": {"max_iter": 1000, "C": 1.0, "solver": "lbfgs"},
  "crf_params": {"algorithm": "lbfgs", "c1": 0.1, "c2": 0.1, "max_iterations": 100}
}
```

---

## Documentation

| File | Purpose |
|---|---|
| [`research_decisions.md`](research_decisions.md) | Decision log — maps review gaps to research question and each experimental choice |
| [`baseline_validation.md`](baseline_validation.md) | Validates each method against literature; documents comparison protocol |
| [`ai_assistance_log.md`](ai_assistance_log.md) | Academic transparency — every AI-assisted step, what was accepted/rejected, verification |
| [`data/README.md`](data/README.md) | Dataset documentation — NCBI Disease corpus description, subset construction, split protocol |

---

## Citation

If you use this code or dataset subset in academic work, please cite:

```
Sutariya, V. (2026). AITR Lab 02: Comparative NER Annotation Study — 
Dictionary, Logistic Regression, and CRF on NCBI Disease Corpus.
M.Tech Robotics and AI, AITR. MRA2026012.
```

NCBI Disease Corpus:
```
Dogan RI, Leaman R, Lu Z. (2014). NCBI disease corpus: A resource for disease 
name recognition and normalization. J Biomed Inform, 47:1-10.
```

---

## License

This project code is released under the **MIT License**.

```
MIT License

Copyright (c) 2026 Vyom Sutariya

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

> **Note:** The NCBI Disease Corpus is a US government work and is in the public domain. This project's embedded subset is derived from that corpus.
