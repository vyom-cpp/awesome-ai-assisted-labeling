"""
NER baselines: DictionaryNER, LogRegNER, CRFNER.
Vyom Sutariya | MRA2026012 | AITR Lab 02
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
import sklearn_crfsuite

from features import (
    word_features,
    sentence_to_crf_features,
    get_X_y_for_lr,
)


# ============================================================
# 1. DICTIONARY NER
# ============================================================

DISEASE_DICT = [
    # --- Single-token ---
    "Huntington", "Alzheimer", "Parkinson", "schizophrenia",
    "leukemia", "melanoma", "epilepsy", "asthma", "COPD",
    "hypertension", "atherosclerosis", "tuberculosis", "malaria",
    "sepsis", "pneumonia", "osteoporosis", "hypothyroidism",
    "hyperthyroidism", "depression", "obesity", "cirrhosis",
    "myelofibrosis", "acromegaly", "gout", "hyperuricemia",
    "phenylketonuria", "galactosemia", "thalassemia", "hemophilia",
    "pheochromocytoma",

    # --- Two-token ---
    "Huntington disease", "Alzheimer disease", "Parkinson disease",
    "breast cancer", "lung cancer", "ovarian cancer", "prostate cancer",
    "colorectal cancer", "cervical cancer", "bladder cancer", "gastric cancer",
    "thyroid cancer", "pancreatic cancer", "kidney cancer", "esophageal cancer",
    "cystic fibrosis", "Crohn disease", "multiple sclerosis",
    "heart failure", "atrial fibrillation", "bipolar disorder",
    "kidney stones", "acute pancreatitis", "bacterial meningitis",
    "Wilson disease", "Gaucher disease", "Fabry disease", "Pompe disease",
    "Marfan syndrome", "Down syndrome", "Angelman syndrome", "Graves disease",
    "Addison disease", "Cushing syndrome", "Paget disease", "polycythemia vera",
    "essential thrombocythemia", "psoriatic arthritis", "ankylosing spondylitis",
    "lupus nephritis", "Barrett esophagus", "Hodgkin lymphoma",

    # --- Three-token ---
    "type 2 diabetes", "type 1 diabetes",
    "amyotrophic lateral sclerosis",
    "systemic lupus erythematosus",
    "rheumatoid arthritis",
    "ulcerative colitis",
    "multiple myeloma",
    "Crohn disease",
    "colorectal cancer",
    "coronary artery disease",
    "chronic kidney disease",
    "acute pancreatitis",
    "chronic myeloid leukemia",
    "acute myeloid leukemia",
    "acute lymphoblastic leukemia",
    "diffuse large B-cell lymphoma",
    "non-Hodgkin lymphoma",
    "hepatocellular carcinoma",
    "glioblastoma multiforme",
    "spinal muscular atrophy",
    "myelodysplastic syndrome",
    "myocardial infarction",
    "renal cell carcinoma",
    "clear-cell renal cell carcinoma",
    "tuberous sclerosis complex",
    "neurofibromatosis type 1",
    "fragile X syndrome",
    "Prader-Willi syndrome",
    "sickle cell disease",
    "beta-thalassemia major",
    "hemophilia A",
    "major depressive disorder",
    "generalized anxiety disorder",
    "urinary tract infection",
    "Clostridium difficile infection",
    "irritable bowel syndrome",
    "inflammatory bowel disease",
    "cardiovascular disease",
    "Lynch syndrome",
    "hepatitis B", "hepatitis C",
    "HIV infection",
    "ischemic stroke",
    "pituitary adenoma",
    "chronic lymphocytic leukemia",
    "Waldenström macroglobulinemia",
    "frontotemporal dementia",
    "Dravet syndrome",
    "temporal lobe epilepsy",
]


def _build_trie(disease_list):
    """
    Build token-level trie for greedy matching.
    Returns dict mapping first-token → list of token-tuples.
    """
    trie = {}
    for disease in disease_list:
        tokens = disease.lower().split()
        key = tokens[0]
        trie.setdefault(key, [])
        trie[key].append(tuple(tokens))
    # sort longest first so greedy picks longest match
    for key in trie:
        trie[key].sort(key=lambda x: -len(x))
    return trie


class DictionaryNER:
    """
    Rule-based NER using greedy longest-match against a disease dictionary.
    No training required.
    """

    def __init__(self):
        self._trie = _build_trie(DISEASE_DICT)

    def predict(self, list_of_token_seqs: list) -> list:
        """
        Parameters
        ----------
        list_of_token_seqs : list of list of str

        Returns
        -------
        list of list of str  (BIO labels)
        """
        all_preds = []
        for tokens in list_of_token_seqs:
            labels = ['O'] * len(tokens)
            i = 0
            while i < len(tokens):
                key = tokens[i].lower()
                matched = False
                if key in self._trie:
                    for phrase_tokens in self._trie[key]:
                        n = len(phrase_tokens)
                        if i + n <= len(tokens):
                            window = tuple(t.lower() for t in tokens[i:i + n])
                            if window == phrase_tokens:
                                labels[i] = 'B-Disease'
                                for j in range(1, n):
                                    labels[i + j] = 'I-Disease'
                                i += n
                                matched = True
                                break
                if not matched:
                    i += 1
            all_preds.append(labels)
        return all_preds


# ============================================================
# 2. LOGISTIC REGRESSION NER
# ============================================================

class LogRegNER:
    """
    Token-level Logistic Regression NER using hand-crafted features.
    """

    def __init__(self):
        self.clf = LogisticRegression(
            max_iter=1000,
            C=1.0,
            random_state=42,
            solver='lbfgs',
        )
        self.vectorizer = None

    def fit(self, list_of_token_seqs: list, list_of_label_seqs: list):
        """Train on provided token/label sequences."""
        X, y, vectorizer = get_X_y_for_lr(list_of_token_seqs, list_of_label_seqs)
        self.vectorizer = vectorizer
        self.clf.fit(X, y)

    def predict(self, list_of_token_seqs: list) -> list:
        """Predict BIO labels for each sentence."""
        all_preds = []
        for tokens in list_of_token_seqs:
            feat_dicts = [word_features(tokens, i) for i in range(len(tokens))]
            X = self.vectorizer.transform(feat_dicts)
            preds = self.clf.predict(X)
            all_preds.append(list(preds))
        return all_preds


# ============================================================
# 3. CRF NER
# ============================================================

class CRFNER:
    """
    CRF NER using sklearn-crfsuite with identical feature set to LogRegNER.
    Models label transition probabilities — the standard pre-neural NER method.
    """

    def __init__(self):
        self.crf = sklearn_crfsuite.CRF(
            algorithm='lbfgs',
            c1=0.1,
            c2=0.1,
            max_iterations=100,
            all_possible_transitions=True,
        )

    def fit(self, list_of_token_seqs: list, list_of_label_seqs: list):
        """Train CRF on sentence-level feature sequences."""
        X = [sentence_to_crf_features(tokens) for tokens in list_of_token_seqs]
        y = [list(labels) for labels in list_of_label_seqs]
        self.crf.fit(X, y)

    def predict(self, list_of_token_seqs: list) -> list:
        """Return predicted BIO label sequences."""
        X = [sentence_to_crf_features(tokens) for tokens in list_of_token_seqs]
        return self.crf.predict(X)
