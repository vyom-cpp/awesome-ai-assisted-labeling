import json, sys

nb_path = '/Users/vyom/Developer/robita-cir/AITR_Lab02_MRA2026012_NER_Annotation/notebooks/AITR_Lab02_MRA2026012_NER_Experiment.ipynb'
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code' and any('df_abl = pd.read_csv' in line for line in cell.get('source', [])):
        # replace source with updated plotting code including DictionaryNER
        new_source = [
            "import matplotlib.pyplot as plt\n",
            "import pandas as pd\n",
            "import numpy as np\n",
            "df_abl = pd.read_csv('results/ablation.csv')\n",
            "\n",
            "fig, ax = plt.subplots(figsize=(8, 5))\n",
            "\n",
            "colors = {'DictionaryNER': '#4C72B0', 'LogRegNER': '#DD8452', 'CRFNER': '#55A868'}\n",
            "markers = {'DictionaryNER': 'o', 'LogRegNER': '^', 'CRFNER': 's'}\n",
            "labels_map = {'DictionaryNER': 'Dictionary NER', 'LogRegNER': 'Logistic Regression NER', 'CRFNER': 'CRF NER'}\n",
            "\n",
            "for method in ['DictionaryNER', 'LogRegNER', 'CRFNER']:\n",
            "    sub = df_abl[df_abl['method'] == method].sort_values('fraction')\n",
            "    ax.plot(sub['fraction'], sub['f1'], marker=markers[method], color=colors[method], linewidth=2, markersize=7, label=labels_map[method])\n",
            "    for _, row in sub.iterrows():\n",
            "        ax.annotate(f'{row[\'f1\']:.3f}', xy=(row['fraction'], row['f1']), xytext=(5,4), textcoords='offset points', fontsize=8.5, color=colors[method])\n",
            "\n",
            "ax.set_xlabel('Training Data Fraction', fontsize=12)\n",
            "ax.set_ylabel('F1 Score', fontsize=12)\n",
            "ax.set_title('Ablation: F1 Score vs Training Data Fraction (LR vs CRF vs Dictionary)', fontsize=13, fontweight='bold')\n",
            "fracs = sorted(df_abl['fraction'].unique())\n",
            "ax.set_xticks(fracs)\n",
            "ax.set_xticklabels([f'{int(f*100)}%' for f in fracs], fontsize=11)\n",
            "ax.set_ylim(0, 1.0)\n",
            "ax.yaxis.grid(True, linestyle='--', alpha=0.7)\n",
            "ax.set_axisbelow(True)\n",
            "ax.legend(fontsize=11)\n",
            "fig.tight_layout()\n",
            "plt.savefig('results/figure2_ablation.png', dpi=150, bbox_inches='tight')\n",
            "plt.show()\n",
            "print('✅ Saved results/figure2_ablation.png')\n"
        ]
        cell['source'] = new_source

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)
print('Updated notebook source code')
