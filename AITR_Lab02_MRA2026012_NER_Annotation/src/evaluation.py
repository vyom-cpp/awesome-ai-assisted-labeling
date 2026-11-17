"""
Evaluation utilities for NER experiments.
Vyom Sutariya | MRA2026012 | AITR Lab 02
"""

import csv
import os
from seqeval.metrics import (
    precision_score,
    recall_score,
    f1_score,
    classification_report,
)


def compute_metrics(true_seqs: list, pred_seqs: list) -> dict:
    """
    Compute entity-level Precision, Recall, F1 using seqeval.

    Parameters
    ----------
    true_seqs : list of list of str   (gold BIO labels)
    pred_seqs : list of list of str   (predicted BIO labels)

    Returns
    -------
    dict with keys: precision, recall, f1
    """
    p = precision_score(true_seqs, pred_seqs, zero_division=0)
    r = recall_score(true_seqs, pred_seqs, zero_division=0)
    f = f1_score(true_seqs, pred_seqs, zero_division=0)
    return {'precision': round(p, 4), 'recall': round(r, 4), 'f1': round(f, 4)}


def get_classification_report(true_seqs: list, pred_seqs: list) -> str:
    """Return full seqeval classification report string."""
    return classification_report(true_seqs, pred_seqs, zero_division=0)


def save_metrics_csv(results_dict: dict, path: str):
    """
    Save per-method metrics to CSV.

    Parameters
    ----------
    results_dict : dict  {method_name: {precision, recall, f1}}
    path : str           destination CSV path
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['method', 'precision', 'recall', 'f1'])
        for method, metrics in results_dict.items():
            writer.writerow([
                method,
                metrics['precision'],
                metrics['recall'],
                metrics['f1'],
            ])
    print(f"Saved metrics CSV → {path}")


def save_ablation_csv(ablation_results: list, path: str):
    """
    Save ablation study results to CSV.

    Parameters
    ----------
    ablation_results : list of dict
        Each dict has keys: method, fraction, precision, recall, f1
    path : str
        Destination CSV path
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['method', 'fraction', 'precision', 'recall', 'f1'])
        for row in ablation_results:
            writer.writerow([
                row['method'],
                row['fraction'],
                row['precision'],
                row['recall'],
                row['f1'],
            ])
    print(f"Saved ablation CSV → {path}")
