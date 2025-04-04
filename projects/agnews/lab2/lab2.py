# -*- coding: utf-8 -*-
"""lab2-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16jKsJgW_GkGqHYZYbyNsMlgCd1VPeap-
"""

import numpy as np
import pandas as pd
import nltk
import os
import re
from nltk.corpus import stopwords
nltk.download('stopwords')

data = pd.read_csv('train/0/0.tsv', sep='\t', header= None)

stemma = data[0].to_list()

def cleaned_data(tokens):
    pattern = r'[^\w\s]'
    stop_words = set(stopwords.words('english'))

    cleaned_tokens = []
    for token in tokens:
        clean_token = re.sub(pattern, '', str(token).lower())
        if clean_token != '' and clean_token not in stop_words:
            cleaned_tokens.append(clean_token)

    return cleaned_tokens

stemma = cleaned_data(stemma)

corpus_count = len(stemma)

import itertools as itertools
from collections import Counter
from nltk.collocations import TrigramCollocationFinder

def calculate_trigrams(corpus):
    words_cnt = Counter()
    trigrams = Counter()
    for i in range(len(corpus) - 3):
        w1,w2,w3 = corpus[i], corpus[i+1], corpus[i+2]
        words_cnt[w1] += 1
        trigrams[(w1, w2, w3)] += 1
    return words_cnt, trigrams

words_freq, trigrams = calculate_trigrams(stemma)

"""поиск часттоты текста"""

trigram_measures = nltk.collocations.TrigramAssocMeasures()

def calculate_MI(words_freq, trigrams, corpus_count):
    mi_scores = []
    for tr in trigrams.keys():
        without_log = (corpus_count ** 2) * trigrams[tr]
        mult = (words_freq[tr[0]] * words_freq[tr[1]] * words_freq[tr[2]])
        mi_scores.append([" ".join(tr), np.log(without_log / mult)])
    return mi_scores

MI_scores = calculate_MI(words_freq, trigrams, corpus_count)

"""Сортирует триграммы по убыванию значений PMI."""

MI_scores_best = sorted(MI_scores, reverse=True, key=lambda x: x[1])

print(finder_thr.nbest(trigram_measures.pmi, 30))

MI_scores_best[:30]

