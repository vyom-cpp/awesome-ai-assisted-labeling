# Dataset Documentation — AITR Lab 02

**Student:** Vyom Sutariya | MRA2026012 | Dept. of IT (Robotics and AI)

---

## NCBI Disease Corpus

| Field | Detail |
|---|---|
| **Full name** | NCBI Disease Corpus |
| **Official source** | https://www.ncbi.nlm.nih.gov/CBBresearch/Dogan/DISEASE/ |
| **Description** | 793 PubMed abstracts manually annotated with disease mentions by NCBI curators |
| **Annotation scheme** | BIO (B-Disease, I-Disease, O) |
| **Entity types** | Disease names and abbreviations (single-token and multi-token spans) |
| **License** | Public domain (US government work — NIH / NCBI) |
| **Language** | English (biomedical) |

**Citation:**
> Dogan RI, Leaman R, Lu Z. (2014). NCBI disease corpus: A resource for disease name recognition and normalization. *Journal of Biomedical Informatics*, 47:1–10. https://doi.org/10.1016/j.jbi.2013.12.006

---

## Subset Used in This Study

This study uses an **embedded representative subset** of 180 sentences constructed from the NCBI Disease corpus vocabulary and annotation conventions. The subset is defined programmatically in `data/ncbi_disease_subset.py` as a Python function `get_dataset()`.

### Why an embedded subset?

| Reason | Detail |
|---|---|
| **Offline reproducibility** | Eliminates network dependencies; experiment runs identically in any environment with Python installed |
| **Controlled scope** | 180 sentences is sufficient for a comparative method study; full 793-abstract corpus would require preprocessing infrastructure beyond this lab's scope |
| **Pedagogical fit** | Embedded data makes the codebase self-contained for academic submission |

### Subset Characteristics

| Property | Value |
|---|---|
| Total sentences | 180 |
| Disease entity types | Single-token (e.g., "leukemia") and multi-token (e.g., "amyotrophic lateral sclerosis") |
| Entity token fraction | ~30% B-Disease or I-Disease; ~70% O |
| Disease vocabulary | Drawn from NCBI Disease corpus, OMIM, and MeSH — includes ~120 unique disease terms |
| Sentence contexts | Clinical description, gene-disease association, treatment mention, epidemiology, comparative/contrastive |

### Disease Vocabulary (representative sample)

Huntington disease, breast cancer, Alzheimer disease, cystic fibrosis, type 2 diabetes, Parkinson disease, schizophrenia, colorectal cancer, lung cancer, ovarian cancer, prostate cancer, leukemia, lymphoma, melanoma, epilepsy, asthma, COPD, hypertension, atherosclerosis, Crohn disease, ulcerative colitis, multiple sclerosis, amyotrophic lateral sclerosis, rheumatoid arthritis, systemic lupus erythematosus, Huntington's disease, myocardial infarction, Duchenne muscular dystrophy, retinitis pigmentosa, tuberous sclerosis *(and ~90 additional terms)*

---

## Annotation Scheme

This dataset uses the **BIO (Beginning-Inside-Outside)** tagging scheme, standard for sequence labelling tasks:

| Tag | Meaning | Example |
|---|---|---|
| `B-Disease` | Beginning token of a disease entity | "**Huntington**" in "Huntington disease" |
| `I-Disease` | Continuation token of a disease entity | "**disease**" in "Huntington disease" |
| `O` | Non-entity token | "patients", "with", "were" |

### BIO Consistency Rules
- An `I-Disease` token must always be preceded by `B-Disease` or `I-Disease` (never at sentence start or after `O`)
- Each sentence is an independent label sequence
- Entity spans do not cross sentence boundaries

---

## Split Protocol

The 180 sentences are split once using a fixed random seed before any training or evaluation:

| Split | Fraction | Approx. sentences | Purpose |
|---|---|---|---|
| Train | 70% | 126 | Model fitting (and ablation subsampling) |
| Validation | 15% | 27 | Hyperparameter tuning (not used in reported metrics) |
| Test | 15% | 27 | Final evaluation — held out from all training decisions |

**Parameters:**
- `random_state = 42`
- Shuffled before split
- Same split used for all three methods and all ablation fractions (test set never changes)

---

## Loading the Data

```python
import sys
sys.path.insert(0, '.')  # from project root
from data.ncbi_disease_subset import get_dataset

sentences = get_dataset()
# sentences: list of (tokens, labels) tuples
# tokens: list of str
# labels: list of str (B-Disease, I-Disease, O)

print(f"Total sentences: {len(sentences)}")
tokens, labels = sentences[0]
print(f"Example tokens: {tokens}")
print(f"Example labels: {labels}")
```

---

## File Index

| File | Description |
|---|---|
| `data/ncbi_disease_subset.py` | Python module defining `get_dataset()` — returns 180 (tokens, labels) tuples |
| `data/README.md` | This file |
