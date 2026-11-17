"""
run_experiment.py — Full NER experiment pipeline.
Vyom Sutariya | MRA2026012 | AITR Lab 02

Usage:
    python scripts/run_experiment.py
"""

import sys
import os
import random

# --- Path setup so imports work from project root ---
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_SCRIPT_DIR)
sys.path.insert(0, _PROJECT_ROOT)
sys.path.insert(0, os.path.join(_PROJECT_ROOT, 'src'))

import numpy as np
from sklearn.model_selection import train_test_split

from data.ncbi_disease_subset import get_dataset
from baselines import DictionaryNER, LogRegNER, CRFNER
from evaluation import (
    compute_metrics,
    get_classification_report,
    save_metrics_csv,
    save_ablation_csv,
)

# ------------------------------------------------------------------ #
# Config
# ------------------------------------------------------------------ #
RANDOM_SEED = 42
TEST_SIZE = 0.15
VAL_SIZE = 0.15
ABLATION_FRACTIONS = [0.1, 0.25, 0.5, 1.0]
RESULTS_DIR = os.path.join(_PROJECT_ROOT, 'results')
os.makedirs(RESULTS_DIR, exist_ok=True)

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)


# ------------------------------------------------------------------ #
# Utilities
# ------------------------------------------------------------------ #
def print_table(title: str, results: dict):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")
    print(f"  {'Method':<30} {'Precision':>10} {'Recall':>10} {'F1':>10}")
    print(f"  {'-'*62}")
    for method, m in results.items():
        print(f"  {method:<30} {m['precision']:>10.4f} {m['recall']:>10.4f} {m['f1']:>10.4f}")
    print(f"{'='*60}")


def print_ablation_table(ablation_results: list):
    print(f"\n{'='*70}")
    print(f"  ABLATION STUDY — F1 by Training Fraction")
    print(f"{'='*70}")
    print(f"  {'Method':<20} {'Fraction':>10} {'Precision':>12} {'Recall':>10} {'F1':>10}")
    print(f"  {'-'*64}")
    for row in ablation_results:
        print(f"  {row['method']:<20} {row['fraction']:>10.2f} "
              f"{row['precision']:>12.4f} {row['recall']:>10.4f} {row['f1']:>10.4f}")
    print(f"{'='*70}")


# ------------------------------------------------------------------ #
# 1. Load & split data
# ------------------------------------------------------------------ #
print("\nLoading NCBI Disease subset …")
dataset = get_dataset()
print(f"  Total sentences: {len(dataset)}")

# Compute entity density
total_tokens = sum(len(t) for t, _ in dataset)
entity_tokens = sum(sum(1 for l in ls if l != 'O') for _, ls in dataset)
print(f"  Total tokens:    {total_tokens}")
print(f"  Entity tokens:   {entity_tokens}  ({100*entity_tokens/total_tokens:.1f}%)")

sentences = [t for t, _ in dataset]
labels = [l for _, l in dataset]

# First split off test set
sents_trainval, sents_test, labels_trainval, labels_test = train_test_split(
    sentences, labels, test_size=TEST_SIZE, random_state=RANDOM_SEED
)

# Then split off validation set from train+val
val_ratio_of_trainval = VAL_SIZE / (1.0 - TEST_SIZE)
sents_train, sents_val, labels_train, labels_val = train_test_split(
    sents_trainval, labels_trainval,
    test_size=val_ratio_of_trainval,
    random_state=RANDOM_SEED,
)

print(f"\nData split:")
print(f"  Train : {len(sents_train)} sentences")
print(f"  Val   : {len(sents_val)} sentences")
print(f"  Test  : {len(sents_test)} sentences")


# ------------------------------------------------------------------ #
# 2. Baseline evaluation on FULL train set
# ------------------------------------------------------------------ #
print("\n\nTraining models on full training set …")

# -- Dictionary NER (no training) --
print("  [1/3] DictionaryNER … (no training)")
dict_ner = DictionaryNER()

# -- Logistic Regression NER --
print("  [2/3] LogRegNER … fitting")
lr_ner = LogRegNER()
lr_ner.fit(sents_train, labels_train)

# -- CRF NER --
print("  [3/3] CRFNER … fitting")
crf_ner = CRFNER()
crf_ner.fit(sents_train, labels_train)

print("  Done.")

# ------------------------------------------------------------------ #
# 3. Evaluate on test set
# ------------------------------------------------------------------ #
print("\nEvaluating on test set …")

dict_preds = dict_ner.predict(sents_test)
lr_preds = lr_ner.predict(sents_test)
crf_preds = crf_ner.predict(sents_test)

results = {
    'DictionaryNER': compute_metrics(labels_test, dict_preds),
    'LogRegNER': compute_metrics(labels_test, lr_preds),
    'CRFNER': compute_metrics(labels_test, crf_preds),
}

print_table("MAIN RESULTS — Test Set", results)

# Detailed reports
for name, preds in [('DictionaryNER', dict_preds), ('LogRegNER', lr_preds), ('CRFNER', crf_preds)]:
    print(f"\n--- {name} Classification Report ---")
    print(get_classification_report(labels_test, preds))

# ------------------------------------------------------------------ #
# 4. Ablation: vary training fraction for LR and CRF
# ------------------------------------------------------------------ #
print("\n\nRunning ablation study …")
ablation_results = []

n_train = len(sents_train)
for fraction in ABLATION_FRACTIONS:
    n_subset = max(1, int(n_train * fraction))
    # Deterministic subsample
    rng = np.random.RandomState(RANDOM_SEED)
    indices = rng.choice(n_train, size=n_subset, replace=False)
    sub_sents = [sents_train[i] for i in indices]
    sub_labels = [labels_train[i] for i in indices]

    print(f"  fraction={fraction:.2f}  n_train={n_subset}")

    # LogReg
    lr_ab = LogRegNER()
    lr_ab.fit(sub_sents, sub_labels)
    lr_ab_preds = lr_ab.predict(sents_test)
    lr_ab_metrics = compute_metrics(labels_test, lr_ab_preds)
    ablation_results.append({
        'method': 'LogRegNER', 'fraction': fraction,
        **lr_ab_metrics,
    })

    # CRF
    crf_ab = CRFNER()
    crf_ab.fit(sub_sents, sub_labels)
    crf_ab_preds = crf_ab.predict(sents_test)
    crf_ab_metrics = compute_metrics(labels_test, crf_ab_preds)
    ablation_results.append({
        'method': 'CRFNER', 'fraction': fraction,
        **crf_ab_metrics,
    })

print_ablation_table(ablation_results)

# ------------------------------------------------------------------ #
# 5. Save CSVs
# ------------------------------------------------------------------ #
save_metrics_csv(results, os.path.join(RESULTS_DIR, 'metrics.csv'))
save_ablation_csv(ablation_results, os.path.join(RESULTS_DIR, 'ablation.csv'))

print("\n\nExperiment complete. Results saved to results/")
print(f"  metrics.csv   → {os.path.join(RESULTS_DIR, 'metrics.csv')}")
print(f"  ablation.csv  → {os.path.join(RESULTS_DIR, 'ablation.csv')}")
