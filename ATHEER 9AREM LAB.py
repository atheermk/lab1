#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[4]:


from platform import python_version
print(python_version())


# In[5]:


import numpy
numpy.version.version


# In[ ]:





# In[9]:


import gensim as gs
print(gs.__version__)


# In[12]:


print(str“Tokenization is the process of breaking down text document apart into those pieces”)  


# In[25]:


Sentence= "Tokenization is the process of breaking down text documentapart into those pieces"


# In[28]:


import gensim as gs
tokenizedWord= list(gs.utils.tokenize(Sentence)) 




# In[29]:


tokenizedWord


# In[30]:


gs.utils.tokenize

help(gs.utils.tokenize)


# In[ ]:





# In[48]:


import gensim
from gensim import corpora
from pprint import pprint  
text = [""" In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Computer science defines AI research as the study of intelligent agents: any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals."""]  
tokens = [[token for token in sentence.split()] for sentence in text]  
gensim_dictionary = corpora.Dictionary() 
gensim_corpus 	= 	[gensim_dictionary.doc2bow(token, allow_update=True) for token in tokens]  
print(gensim_corpus) 


# In[49]:


word_frequencies = [[(gensim_dictionary[id], frequence) for id, frequence in couple] for couple in gensim_corpus]
print(word_frequencies)


# In[54]:


from gensim.utils import simple_preprocess
from smart_open import smart_open
import os

tokens = [simple_preprocess(sentence, deacc=True) for sentence in open(r'C:\\Users\\Pheonix\\Desktop' encoding='utf-8')]

gensim_dictionary = corpora.Dictionary()
gensim_corpus = [gensim_dictionary.doc2bow(token, allow_update=True) for token in tokens]
word_frequencies = [[(gensim_dictionary[id], frequence) for id, frequence in couple] for couple in gensim_corpus]

print(word_frequencies)


# In[ ]:




