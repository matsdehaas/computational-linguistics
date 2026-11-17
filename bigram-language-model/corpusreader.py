# -*- coding: utf-8 -*-
"""
Created on Thu May 11 14:05:26 2023

@author: Sander
"""
import glob
from nltk.tokenize import word_tokenize

class CorpusReader:
    
    def __init__(self, directory): 
        
        self.path_name = directory # initializeer de directory path name waar de text staat
        
        
        
    def sents(self):
        
        alltext = glob.glob(self.path_name+"/*")
        
        with open(alltext[0]) as f:
            
            total_corpus = f.readlines()
            
        for i in range(1,len(alltext)):
            
            with open(alltext[i]) as f:
                
                total_corpus += f.readlines() # lees alle lines in de text files 
        
        tokens = []
        
        for i in range(0,len(total_corpus)):
            
            if len(total_corpus[i].split())!=0: # verwijder de lege lines 
                
                tokens.append(word_tokenize(total_corpus[i]))
            
        return tokens