#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk 
import os 
import string
import numpy as np
import copy
import pandas as pd
import pickle
import re


# In[2]:


pip install num2words


# In[4]:


title = "used files"
os.chdir(r'C:\Users\Pheonix\Desktop\mini_newsgroups\comp.graphics')
paths = []
for (dirpath, dirnames, filenames) in os.walk(str(os.getcwd())+'/'+title+'/'):
    for i in filenames:
        paths.append(str(dirpath)+str("\\")+i) 

paths


# In[5]:


for i in paths:
    file = open(paths[paths.index(i)])
    print(file.read(),'\n\n-------------------------\n\n')


# In[6]:


def remove_stop_words(data):
    stop_words = stopwords.words('english')
    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if w not in stop_words:
            new_text = new_text + " " + w
    return np.char.strip(new_text) 

#Removing punctuation
def remove_punctuation(data):
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~\n"
    for i in range(len(symbols)):
        data = np.char.replace(data, symbols[i], ' ')
        data = np.char.replace(data, " ", " ")
    data = np.char.replace(data, ',', '')
    return data 

#Convert to lowercase
def convert_lower_case(data):
    return np.char.lower(data)

#Stemming
def stemming(data):
    stemmer= PorterStemmer()

    tokens = word_tokenize(str(data))
    new_text = ""
    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)
    return np.char.strip(new_text) 

#Converting numbers to its equivalent words 
def convert_numbers(data):
    data = np.char.replace(data, "0", " zero ")
    data = np.char.replace(data, "1", " one ")
    data = np.char.replace(data, "2", " two ")
    data = np.char.replace(data, "3", " three ")
    data = np.char.replace(data, "4", " four ")
    data = np.char.replace(data, "5", " five ")
    data = np.char.replace(data, "6", " six ")
    data = np.char.replace(data, "7", " seven ")
    data = np.char.replace(data, "8", " eight ")
    data = np.char.replace(data, "9", " nine ")
    return data 

#Removing header 
def remove_header(data):
    try:
        ind = data.index('\n\n')
        data = data[ind:]
    except:
        print("No Header")
    return data 

#Removing apostrophe 
def remove_apostrophe(data):
    return np.char.replace(data, "'", "") 

#Removing single characters 
def remove_single_characters(data):
    words = word_tokenize(str(data))
    new_text = ""
    for w in words:
        if len(w) > 1:
            new_text = new_text + " " + w
    return np.char.strip(new_text)

#to use all the previous
def preprocess(data):
    data = remove_header(data) 
    data = convert_lower_case(data)
    data = convert_numbers(data)
    data = remove_punctuation(data)
    data = remove_stop_words(data)
    data = remove_apostrophe(data)
    data = remove_single_characters(data)
    data = stemming(data) 
    return data


# In[7]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
from num2words import num2words


# In[8]:



processed_text = []
for i in range(len(filenames)):
    file = open(dirpath+'/'+ filenames[i], 'r', encoding='cp1250', errors='ignore')
    text = file.read().strip()
    file.close()
    processed_text.append(word_tokenize(str(preprocess(text))))
    print(processed_text)


# In[9]:


DF = {}
N = len(processed_text)

for i in range(N):
    tokens = processed_text[i]
    for w in tokens:
        try:
            DF[w].add(i)
        except:
            DF[w] = {i}
            
for i in DF:
    DF[i] = len(DF[i])

DF


# In[11]:


total_vocab_size = [x for x in DF]
print(total_vocab_size[:5])


# In[12]:


print(len(DF))


# In[14]:


def doc_freq(word):
    c = 0
    try:
        c = DF[word]
    except:
        pass
    return c


# In[15]:


word = 'one'
print('word = ',word,'--> frequency = ', doc_freq(word))


# In[16]:


doc = 0
tf_idf = {}

for i in range(N):
    
    tokens = processed_text[i]
    counter = Counter(tokens + processed_text[i])
    words_count = len(tokens + processed_text[i])

    for token in np.unique(tokens):
        
        tf = counter[token]/words_count
        df = doc_freq(token)
        idf = np.log((N+1)/(df+1))
        
        tf_idf[doc, token] = tf*idf
        
    doc += 1 

tf_idf


# In[17]:


dict_items = tf_idf.items()

print(list(dict_items)[:1])


# In[18]:


def matching_score(k, query):
    preprocessed_query = preprocess(query)
    tokens = word_tokenize(str(preprocessed_query))
    print("Matching Score")
    print("\nQuery:", query)
    print("")
    print(tokens)

    query_weights = {} 
    for key in tf_idf:
        if key[1] in tokens:
            try:
                query_weights[key[0]] += tf_idf[key]
            except:
                query_weights[key[0]] = tf_idf[key]

    query_weights = sorted(query_weights.items(), key=lambda x: x[1], reverse=True)
    print("")

    l = []

    for i in query_weights[:k]:
        l.append(i[0])

    print(l)

matching_score(2, "I recently got a file describing a library")


# In[ ]:




