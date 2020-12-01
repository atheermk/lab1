#!/usr/bin/env python
# coding: utf-8

# In[1]:


Sentence1= "There are many similarity measures used in NLTK package"


# In[2]:


Sentence2= "There are many similarity measures are available in NLTK"


# In[3]:


from __future__ import print_function
from nltk.metrics import *
Sentence1='There are many similarity measures used in NLTK package'.split()
Sentence2='There are many similarity measures are avaliable in NLTK '.split()
print(accuracy(Sentence1,Sentence2))


# In[4]:


from nltk.metrics import *
Sentence1=  set ('There are many similarity measures used in NLTK package')
Sentence2= set('There are many similarity measures are avaliable in NLTK ')
print(recall(Sentence1,Sentence2))


# In[5]:


from __future__ import print_function
from nltk.metrics import *
Sentence1= set ('There are many similarity measures used in NLTK package')
Sentence2= set('There are many similarity measures are avaliable in NLTK ')
print(precision(Sentence1,Sentence2))


# In[7]:


import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd 

Sentence1='There are many similarity measures used in NLTK package'.split()
Sentence2='There are many similarity measures are avaliable in NLTK '.split()
print(confusion_matrix(Sentence1,Sentence2))


# In[8]:


import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
import pandas as pd 

Sentence1='There are many similarity measures used in NLTK package'.split()
Sentence2='There are many similarity measures are avaliable in NLTK '.split()
print(classification_report(Sentence1,Sentence2))


# In[9]:


import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix 

Sentence1='There are many similarity measures used in NLTK package'.split()
Sentence2='There are many similarity measures are avaliable in NLTK '.split()
array = confusion_matrix(Sentence1,Sentence2)

df_cm = pd.DataFrame(array) 

plt.figure(figsize = (10,7))
sn.heatmap(df_cm, annot=True, annot_kws={"size": 16})


# In[10]:


import nltk
from nltk.metrics import *
edit_distance("relate","relation")


# In[11]:



import nltk
from nltk.metrics import *
edit_distance("“suggestion”","“calculation”")


# In[12]:


def jacc_similarity(query, document):
 first=set(query).intersection(set(document))
 second=set(query).union(set(document))
 return len(first)/len(second) 

import nltk
from nltk.metrics import *
X=set(Sentence1)
Y=set(Sentence2)
print(jaccard_distance(X,Y))


# In[13]:


def binary_distance(label1, label2):
 return 0.0 if label1 == label2 else 1.0
import nltk
from nltk.metrics import *

Sentence1='ahmad'
Sentence2='ahmad'

X=set(Sentence1)
Y=set(Sentence2)
binary_distance(X, Y)


# In[14]:


def binary_distance(label1, label2):
 return 0.0 if label1 == label2 else 1.0
import nltk
from nltk.metrics import *

Sentence1= "There are many similarity measures used in NLTK package"
Sentence2= "There are many similarity measures are available in NLTK"

X=set(Sentence1)
Y=set(Sentence2)
binary_distance(X, Y)


# In[15]:


def masi(label1, label2):
    len_intersection = len(label1.intersection(label2))
    len_union = len(label1.union(label2))
    len_label1 = len(label1)
    len_label2 = len(label2) 
    if len_label1 == len_label2 and len_label1 == len_intersection:
        m = 1
    elif len_intersection == min(len_label1, len_label2):
        m = 0.67
    elif len_intersection > 0:
        m = 0.33
    else:
        m = 0
    return 1 - (len_intersection / float(len_union)) * m
X=set([10,20,30,40])
Y=set([30,50,70])
masi(X, Y)


# In[ ]:




