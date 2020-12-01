#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
from nltk.stem import PorterStemmer
Stemmerporter = PorterStemmer() 
Stemmerporter.stem("dimonstration")


# In[2]:


import nltk
from nltk.stem import PorterStemmer
porter = PorterStemmer()
l_words = ['dogs', 'programming', 'programs', 'programmed', 'cakes', 'indices', 'matrices']
for word in l_words:
    print(f'{word} \t -> {porter.stem(word)}'.expandtabs(15))


# In[3]:


sentence = 'A stemmer for English operating on the stem cat should identify such strings as cats, catlike, and catty. A stem ming algorithm might also reduce the words fishing, fished, and fisher to the stem fish. The stem need not be a word, for ex ample the Porter algorithm reduces, argue, argued, argues, arguing, and argus to the stem argu.'


# In[4]:


from nltk.tokenize import sent_tokenize 
print(sent_tokenize(sentence))


# In[5]:


from nltk.tokenize import sent_tokenize, word_tokenize
sentence = "A stemmer for English operating on the stem cat should identify such strings as cats, catlike, and catty. A stemming algorithm might also reduce the words fishing, fished, and fisher to the stem fish"
tokenized_words = word_tokenize(sentence)
tokenized_sentence = []
for word in tokenized_words:
    tokenized_sentence.append(porter.stem(word))
tokenized_sentence = " ".join(tokenized_sentence)
tokenized_sentence


# In[6]:


from nltk.tokenize import TreebankWordTokenizer

sentence = '''A stemmer for English operating on the stem cat sh
ould identify such strings as cats, catlike, and catty. A stem
ming algorithm might also reduce the words fishing, fished, an
d fisher to the stem fish. The stem need not be a word, for ex
ample the Porter algorithm reduces, argue, argued, argues, arg
uing, and argus to the stem argu.'''

## tokenize the sentence
list = nltk.word_tokenize(sentence)

## print each word in the sentence before and after Stemming 
for word in list:
    print(f'{word} \t -> {porter.stem(word)}'.expandtabs(15))


# In[7]:



from nltk.stem.isri import ISRIStemmer
st = ISRIStemmer()
'حركات' =w
print(st.stem(w))


# In[8]:


file=open("/Users/omaralamri/Desktop/analysis.txt")
Sentences= file.read()
def stemSentence(sentence):
 token_words=word_tokenize(sentence)
 token_words
 stem_sentence=[]
 for word in token_words: 
        
        stem_sentence.append(porter.stem(word))
 stem_sentence.append(" ")
 return "".join(stem_sentence)
print(Sentences)
print("Stemmed sentence")
x=stemSentence(Sentences)
print(x)


# In[9]:


file=open("/Users/omaralamri/Desktop/analysis.txt")
Sentences= file.read()

def stemSentence(sentence): 
    token_words=word_tokenize(sentence) 
    token_words
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ") 
    return "".join(stem_sentence)

print(Sentences) 
print("==========")
print("Stemmed sentence") 
print("==========")
x=stemSentence(Sentences) 
print(x)


# In[10]:


for word in sentence_words:
    print ("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word, pos="v")))


# In[11]:



nltk.download('wordnet')


# In[12]:


from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
sentence = "He was running and eating at same time. He has bad habit of swimming after playing long hours in the Sun."
punctuations="?:!.,;"
sentence_words = nltk.word_tokenize(sentence)
for word in sentence_words:
    if word in punctuations:
        sentence_words.remove(word)
        sentence_words
        print("{0:20}{1:20}".format("Word","Lemma"))
        for word in sentence_words:
            print ("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word)))


# In[ ]:




