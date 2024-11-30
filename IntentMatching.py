import sys

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sys.path.append('./')


def yes_or_no(msg):
    """
    :param msg: response from the user
    :return: yes or no
    """
    with open('./corpus/yes_or_no.data', 'r') as f:
        data = f.readlines()
    yes_corpus = data[0].split(',')
    no_corpus = data[1].split(',')
    all_text = [msg] + yes_corpus + no_corpus
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(all_text)

    input_vector = tfidf[0:1]
    yes_vectors = tfidf[1:len(yes_corpus) + 1]
    no_vectors = tfidf[len(yes_corpus) + 1:]

    yes_similarity = cosine_similarity(input_vector, yes_vectors).mean()
    no_similarity = cosine_similarity(input_vector, no_vectors).mean()
    if yes_similarity > no_similarity:
        return True
    else:
        return False


def get_intent(s):
    """

    :param s: input string
    :return: the user's intent
    """
    data = pd.read_csv('./corpus/intents.data')
    all_sentences = [sent for sentences in data['phrases'].values for sent in sentences.split(';')] + [s]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(all_sentences)
    input_vector = vectors[-1]
    intent_vectors = dict()
    start_idx = 0
    for idx, intent in enumerate(data['intent'].values):
        sentences = data['phrases'][idx].split(';')
        intent_vectors[intent] = vectors[start_idx:start_idx + len(sentences)]
        start_idx += len(sentences)

    max_similarity = 0
    most_likely_intent = None
    for intent, vectors in intent_vectors.items():
        similarity = cosine_similarity(input_vector, vectors).max()
        if similarity > max_similarity:
            max_similarity = similarity
            most_likely_intent = intent

    return most_likely_intent
