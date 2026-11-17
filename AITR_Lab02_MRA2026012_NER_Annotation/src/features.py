"""
Feature extraction for NER models.
Vyom Sutariya | MRA2026012 | AITR Lab 02
"""

import re
from sklearn.feature_extraction import DictVectorizer
import numpy as np


def _word_shape(word: str) -> str:
    """
    Compress word into a shape string:
      Aa → title-case letter, AA → upper, aa → lower, 00 → digit, -- → other
    """
    shape = []
    for ch in word:
        if ch.isupper():
            shape.append('X')
        elif ch.islower():
            shape.append('x')
        elif ch.isdigit():
            shape.append('0')
        else:
            shape.append('-')
    # Compress consecutive identical chars
    compressed = []
    for c in shape:
        if not compressed or compressed[-1] != c:
            compressed.append(c)
    return ''.join(compressed)


def word_features(sent_tokens: list, i: int) -> dict:
    """
    Returns a feature dict for token at position i in sent_tokens.
    Features: identity, casing, affixes, context window ±2, BOS/EOS indicators.
    """
    word = sent_tokens[i]
    feats = {
        'bias': 1.0,
        'word': word,
        'word.lower': word.lower(),
        'word[-3:]': word[-3:] if len(word) >= 3 else word,
        'word[-2:]': word[-2:] if len(word) >= 2 else word,
        'word[-1:]': word[-1:] if len(word) >= 1 else word,
        'word[:3]': word[:3] if len(word) >= 3 else word,
        'word.isupper': word.isupper(),
        'word.istitle': word.istitle(),
        'word.isdigit': word.isdigit(),
        'word.shape': _word_shape(word),
        'word.has_hyphen': '-' in word,
        'word.has_digit': any(c.isdigit() for c in word),
    }

    # BOS / EOS
    if i == 0:
        feats['BOS'] = True
    if i == len(sent_tokens) - 1:
        feats['EOS'] = True

    # Context window ±1
    if i > 0:
        w_m1 = sent_tokens[i - 1]
        feats.update({
            'word[-1].word': w_m1,
            'word[-1].lower': w_m1.lower(),
            'word[-1].istitle': w_m1.istitle(),
            'word[-1].isupper': w_m1.isupper(),
        })
    else:
        feats['BOS-1'] = True

    if i < len(sent_tokens) - 1:
        w_p1 = sent_tokens[i + 1]
        feats.update({
            'word[+1].word': w_p1,
            'word[+1].lower': w_p1.lower(),
            'word[+1].istitle': w_p1.istitle(),
            'word[+1].isupper': w_p1.isupper(),
        })
    else:
        feats['EOS+1'] = True

    # Context window ±2
    if i > 1:
        w_m2 = sent_tokens[i - 2]
        feats.update({
            'word[-2].word': w_m2,
            'word[-2].lower': w_m2.lower(),
        })
    else:
        feats['BOS-2'] = True

    if i < len(sent_tokens) - 2:
        w_p2 = sent_tokens[i + 2]
        feats.update({
            'word[+2].word': w_p2,
            'word[+2].lower': w_p2.lower(),
        })
    else:
        feats['EOS+2'] = True

    return feats


def sentence_to_crf_features(sent_tokens: list) -> list:
    """
    Returns a list of feature dicts, one per token in sent_tokens.
    Used as input to sklearn_crfsuite.CRF.
    """
    return [word_features(sent_tokens, i) for i in range(len(sent_tokens))]


def get_X_y_for_lr(list_of_sentences: list, list_of_label_seqs: list):
    """
    Flatten token-level features and labels for Logistic Regression.

    Parameters
    ----------
    list_of_sentences : list of list of str
    list_of_label_seqs : list of list of str

    Returns
    -------
    X : scipy sparse matrix, shape (n_tokens, n_features)
    y : np.ndarray of str, shape (n_tokens,)
    vectorizer : fitted DictVectorizer (kept for transform at prediction time)
    """
    all_feat_dicts = []
    all_labels = []

    for tokens, labels in zip(list_of_sentences, list_of_label_seqs):
        for i, label in enumerate(labels):
            all_feat_dicts.append(word_features(tokens, i))
            all_labels.append(label)

    vectorizer = DictVectorizer(sparse=True)
    X = vectorizer.fit_transform(all_feat_dicts)
    y = np.array(all_labels)
    return X, y, vectorizer
