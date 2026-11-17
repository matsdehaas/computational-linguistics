# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:43:45 2023

@author: Sander
"""
import re
import random
class BigramModel:
    
    
    def __init__(self,tokenized_sentences):
        
        new_tokenized_sentences = []
              
        for sentence in tokenized_sentences:
            
            new_tokenized_sentence = []
            new_tokenized_sentence.append("<s>") # begin de nieuwe lijst met de start 
            
            for token in sentence:
                
                if not re.match(r'^[_\W]+$',token): # als de token niet alleen maar puntuatie bevat voeg toe aan de lijst
                    
                    new_tokenized_sentence.append(token.lower()) # maak de token lower case
                    
            new_tokenized_sentence.append("</s>")        # eindpunt van de lijst
            new_tokenized_sentences.append(new_tokenized_sentence)        
         
            
        self.unigram_frequency_tabel = {} # sla alle counts op in een tabel
        self.bigram_frequency_tabel = {}
        for sentence in new_tokenized_sentences:
             
            for token in sentence:
                 
                 if token in self.unigram_frequency_tabel: # als token al in de tabel doe plus 1 
                     
                     self.unigram_frequency_tabel[str(token)] += 1
                     
                 else:
                     
                     self.unigram_frequency_tabel[str(token)] = 1 # zo niet dan nieuwe key value pair
        
        for sentence in new_tokenized_sentences:
            
            for i in range(0, len(sentence)-1):
                
               bigram =  str(sentence[i]) +" "+ str(sentence[i+1])
               
               if bigram in self.bigram_frequency_tabel:
                   
                   self.bigram_frequency_tabel[bigram] += 1
                   
               else:
                    
                    self.bigram_frequency_tabel[bigram] = 1
                   
                   
                   
                   
                   
                   
    def probability(self, w, w_n, smoothing_constant):
       
        if w not in list(self.unigram_frequency_tabel.keys()) or w_n not in list(self.unigram_frequency_tabel.keys()):
            
            return 0.0
        
        elif smoothing_constant==0:
            
           return self.bigram_frequency_tabel[w+" "+w_n]/self.unigram_frequency_tabel[w]
       
        else:
           if w+" "+w_n not in self.bigram_frequency_tabel.keys():
               return 1/(self.unigram_frequency_tabel[w]+smoothing_constant)
           else:
               return (self.bigram_frequency_tabel[w+" "+w_n]+1)/(self.unigram_frequency_tabel[w]+smoothing_constant)
    
    
    def perplexity(self, sent, smoothing_constant):
        
        new_tokenized_sentence = []
        new_tokenized_sentence.append("<s>") # begin de nieuwe lijst met de start 
        
        for token in sent:
            
            if not re.match(r'^[_\W]+$',token): # als de token niet alleen maar puntuatie bevat voeg toe aan de lijst
                
                new_tokenized_sentence.append(token.lower()) # maak de token lower case
                
        new_tokenized_sentence.append("</s>")
        
        #prob = self.unigram_frequency_tabel[new_tokenized_sentence[0]]/sum(self.unigram_frequency_tabel.values())
        prob = 1
        
        for i in range(1,len(new_tokenized_sentence)):
            
            if self.probability(new_tokenized_sentence[i-1], new_tokenized_sentence[i],smoothing_constant)==0:
                
                return 0
            
            prob*=1/self.probability(new_tokenized_sentence[i-1], new_tokenized_sentence[i],smoothing_constant)
            
        return prob**(1/(sum(self.unigram_frequency_tabel.values())+sum(self.bigram_frequency_tabel)))
    
    def choose_successor(self, word, smoothing_constant):
        
        if word not in list(self.unigram_frequency_tabel.keys()):
            
            return None 
        
        keys = list(self.bigram_frequency_tabel.keys())
        bigram_prob = {}
        
        for i in range(0, len(keys)):
            bigram = keys[i].split(" ")
            
            if bigram[0]==word:
                
                bigram_prob[bigram[1]] = self.probability(bigram[0], bigram[1], smoothing_constant)
        
        return random.choices(list(bigram_prob.keys()), weights = list(bigram_prob.values()), k=1)

                   
                   
                   
                   
                   
                   
                