#!/usr/bin/env python
# coding: utf-8

# In[13]:


import nltk


# In[14]:


import nltk as nk


# In[15]:


nltk.download('punkt')


# In[16]:


text =" Welcome readers. I hope you find it interesting. Please do reply."


# In[17]:



from nltk.tokenize import sent_tokenize 
print(sent_tokenize(text))


# In[18]:


tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
text=" Welcome readers. I hope you find it interesting. Please do reply."
tokenizer.tokenize(text)


# In[19]:


Arabic_text="مرحبا بكم. نحن نتعلم اساسيات مبادئ استرجاع المعلومات."
tokenizer.tokenize(Arabic_text)


# In[20]:


text = nltk.word_tokenize("Welcome readers. I hope you find it interesting. Please do reply»..")
print (text)


# In[21]:


Arabic=input("Please write a text")
text = nltk.word_tokenize(Arabic)
print(text)


# In[22]:



from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer("[\w]+")
tokenizer.tokenize("Don't hesitate to ask questions or send to me your question to mohsarem@gmail.com")


# In[23]:



from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer("\S+@\S+")
tokenizer.tokenize("Don't hesitate to ask questions or send to me your question to mohsarem@gmail.com")


# In[24]:


text=[" It is a pleasant evening.","Guests, who came from US arrived at the venue","Food was tasty."]
from nltk.tokenize import word_tokenize
tokenized_docs=[word_tokenize(doc)
                for doc in text]
print(tokenized_docs)


# In[25]:


import re
import string
x=re.compile('[%s]' % re.escape(string.punctuation))
tokenized_docs_no_punctuation = []
for review in tokenized_docs: 
    new_review = [] 
    for token in review: 
        new_token = x.sub(u'', token)
        if not new_token == u'': 
            new_review.append(new_token)
            tokenized_docs_no_punctuation.append(new_review)
            print(tokenized_docs_no_punctuation)
            print(text[0].upper())


# In[26]:


nltk.download('stopwords')


# In[27]:


import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stops=set(stopwords.words('english'))
words=["Don't",'hesitate','to','ask','questions']
[word for word in words if word not in stops]


# In[28]:


print(stopwords.words('english'))


# In[29]:


print(stopwords.words('arabic'))


# In[ ]:




