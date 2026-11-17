"""
Plot results from the NER annotation comparison experiment.

Outputs:
  results/figure1_comparison.png  — grouped bar chart P/R/F1 across 3 methods
  results/figure2_ablation.png    — F1 vs training fraction (LR vs CRF)
"""

import sys
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(PROJECT_ROOT, "results")


def plot_comparison(metrics_path: str, out_path: str):
    df = pd.read_csv(metrics_path)
    methods = df['method'].tolist()
    precision = df['precision'].tolist()
    recall = df['recall'].tolist()
    f1 = df['f1'].tolist()

    x = np.arange(len(methods))
    width = 0.25

    fig, ax = plt.subplots(figsize=(9, 5))
    bars_p = ax.bar(x - width, precision, width, label='Precision', color='#4C72B0', edgecolor='white', linewidth=0.8)
    bars_r = ax.bar(x,          recall,    width, label='Recall',    color='#DD8452', edgecolor='white', linewidth=0.8)
    bars_f = ax.bar(x + width,  f1,        width, label='F1',        color='#55A868', edgecolor='white', linewidth=0.8)

    for bars in (bars_p, bars_r, bars_f):
        for bar in bars:
            h = bar.get_height()
            ax.annotate(f'{h:.3f}',
                        xy=(bar.get_x() + bar.get_width() / 2, h),
                        xytext=(0, 3), textcoords='offset points',
                        ha='center', va='bottom', fontsize=8)

    ax.set_xlabel('Annotation Method', fontsize=12)
    ax.set_ylabel('Score', fontsize=12)
    ax.set_title('Comparison of NER Annotation Methods\n(NCBI Disease Subset — Test Set)', fontsize=13, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(methods, fontsize=11)
    ax.set_ylim(0, 1.12)
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    ax.legend(fontsize=11)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved → {out_path}")


def plot_ablation(ablation_path: str, out_path: str):
    df = pd.read_csv(ablation_path)
    fractions = sorted(df['fraction'].unique())

    fig, ax = plt.subplots(figsize=(8, 5))

    colors = {'LogRegNER': '#DD8452', 'CRFNER': '#4C72B0'}
    markers = {'LogRegNER': 'o', 'CRFNER': 's'}
    labels = {'LogRegNER': 'Logistic Regression NER', 'CRFNER': 'CRF NER'}

    for method in ['LogRegNER', 'CRFNER']:
        sub = df[df['method'] == method].sort_values('fraction')
        ax.plot(sub['fraction'], sub['f1'],
                marker=markers[method], color=colors[method],
                linewidth=2, markersize=7, label=labels[method])
        for _, row in sub.iterrows():
            ax.annotate(f"{row['f1']:.3f}",
                        xy=(row['fraction'], row['f1']),
                        xytext=(4, 4), textcoords='offset points',
                        fontsize=8, color=colors[method])

    ax.set_xlabel('Training Data Fraction', fontsize=12)
    ax.set_ylabel('F1 Score', fontsize=12)
    ax.set_title('Ablation: F1 Score vs Training Data Fraction\n(LR vs CRF on NCBI Disease Subset)', fontsize=13, fontweight='bold')
    ax.set_xticks(fractions)
    ax.set_xticklabels([f'{int(f*100)}%' for f in fractions], fontsize=11)
    ax.set_ylim(0, 1.0)
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)
    ax.legend(fontsize=11)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved → {out_path}")


if __name__ == '__main__':
    metrics_csv  = os.path.join(RESULTS_DIR, 'metrics.csv')
    ablation_csv = os.path.join(RESULTS_DIR, 'ablation.csv')
    fig1_out     = os.path.join(RESULTS_DIR, 'figure1_comparison.png')
    fig2_out     = os.path.join(RESULTS_DIR, 'figure2_ablation.png')

    if not os.path.exists(metrics_csv):
        print(f"ERROR: {metrics_csv} not found. Run run_experiment.py first.")
        sys.exit(1)

    plot_comparison(metrics_csv, fig1_out)
    plot_ablation(ablation_csv, fig2_out)
    print("\nAll figures saved to results/")
