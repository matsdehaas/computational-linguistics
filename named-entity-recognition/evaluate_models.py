"""
FILE: evaluate_models.py
Author: Alexis Dimitriadis

Tests the functionality of a pickled model
"""

import pickle
import sys
from nltk.corpus import conll2002 as conll

if len(sys.argv) < 2:
    pickle_path = "best.pickle"
else:
    pickle_path = sys.argv[1]

print(f"Loading the model in {pickle_path}")
ner = pickle.load(open(pickle_path, "rb"))


# Usage 1: parse a list of sentences (with POS tags)
tagzinnen = conll.tagged_sents("ned.train")[1000:1050]
result = ner.parse_sents(tagzinnen)

print("Evaluating on test set")
# Usage 2: self-evaluate (on chunked sentences)
chunkzinnen = conll.chunked_sents("ned.testa")
evaluation = ner.evaluate(chunkzinnen)

function_name = ner.tagger.feature_function.__name__
title = "Evaluation for function: " + function_name + "\n \n"
results = str(evaluation) + "\n \n"

print(title, results)

f = open("evaluation_output.txt", "a")
f.write(title + results)
f.close()
