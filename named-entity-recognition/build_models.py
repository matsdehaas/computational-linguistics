import argparse
import pickle

import nltk
from nltk.chunk.util import conlltags2tree, tree2conlltags
from nltk.corpus import conll2002 as conll

from custom_chunker import ConsecutiveNPChunker
import features


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Script to train and pickle classifiers.')
    parser.add_argument('--pickle', help='Path to output pickle file (required)', required=True)
    parser.add_argument('--dataset', help='Name of the dataset to use (e.g., "ned.train")', required=False)
    parser.add_argument('--features', help='Name feature extraction function (e.g., "test_features")', required=False)
    args = parser.parse_args()
    
    if args.dataset is None:
        args.dataset="ned.train"

    # Load training data
    nltk.download('conll2002')
    training = conll.chunked_sents(args.dataset)

    # Train classifier
    my_recognizer = ConsecutiveNPChunker(features.test_features, training)

    if  args.features == "test_features1":
        my_recognizer = ConsecutiveNPChunker(features.test_features1, training)
    elif args.features == "test_features2":
        my_recognizer = ConsecutiveNPChunker(features.test_features2, training)
    elif args.features == "test_features3":
        my_recognizer = ConsecutiveNPChunker(features.test_features3, training)
    else: 
        my_recognizer = ConsecutiveNPChunker(features.test_features, training)

    # Save classifier to pickle file
    with open(args.pickle, 'wb') as file:
        pickle.dump(my_recognizer, file)

if __name__ == '__main__':
    main()
