# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:52:17 2023

@author: Sander
"""
from corpusreader import CorpusReader
from model import BigramModel
from nltk.tokenize import word_tokenize
def generate_sentence(bigram_model, smoothing_constant):
    
    tokens = []
    tokens.append("<s>")
    succesor = str(bigram_model.choose_successor("<s>", smoothing_constant)[0])
    tokens.append(succesor)
    
    while succesor != "</s>" :
        
        succesor = str(bigram_model.choose_successor(succesor,smoothing_constant)[0])
        tokens.append(succesor)
        
    return tokens
if __name__ == '__main__':
    
    corpus= CorpusReader(r"C:\Users\Sander\OneDrive\Documenten\Kunstmatige Intelligentie\computationele linguistiek\Group assignment 1\train")
    my_model = BigramModel(corpus.sents())
    
    print(" ".join(generate_sentence(my_model,0)))
    print('\n')
    print(" ".join(generate_sentence(my_model,0)))
    
    sent1 = "Suggestive, Watson, is it not?"
    sent2 = "It is amazing that a family can be torn apart by something as simple as a pack of wild dogs!"
    sent3 = "So spoke Sherlock Holmes and turned back to the great scrapbook in which he was arranging and indexing some of his recent material."
    sent4 = "What I like best about my friends is that they are few."
    sent5 = "Friends what is like are they about I best few my that."
    
    print(my_model.perplexity(word_tokenize(sent1),1))
    print(my_model.perplexity(word_tokenize(sent2),1))
    print(my_model.perplexity(word_tokenize(sent3),1))
    print(my_model.perplexity(word_tokenize(sent4),1))
    print(my_model.perplexity(word_tokenize(sent5),1))