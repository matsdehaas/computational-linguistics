#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 11:49:44 2023

@author: matsdehaas
"""

from nltk.chunk.util import tree2conlltags

def reformat_corpus_for_tagger(training_sentences):
    """
    Given a corpus in nltk.Tree format, returns the corpus as a list of lists of tuples,
    where each tuple ((word, POS), IOB) includes the word, its POS tag, and the IOB tag to be predicted.
    @param training_sentences nltk.Tree list
    """
    return [[((word, pos), iob) for (word, pos, iob) in tree2conlltags(sent)] for sent in training_sentences]

def create_training_data(feature_function, training_sentences):
    """
    Creates training data from the corpus of training_sentences and the feature_function
    :param feature_function: function that maps (untagged sentence, word index,
     history) to a dict of features (from features.py)
    :param training_sentences: training sentences as lists of nltk.Tree objects
    :return: list of (dict, IOB tag) pairs
    """
    train_set = []
    reformatted_sentences = reformat_corpus_for_tagger(training_sentences)
    for sentence in reformatted_sentences:
        history = []
        for i in range(len(sentence)):
            feature_dict = feature_function([pair for (pair, _) in sentence], i, history)
            tag = sentence[i][1]
            history.append(tag)
            train_set.append((feature_dict, tag))
    return train_set