#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

txt = "My name is Omar"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-s]", txt)
print(x)


# In[2]:



import re

txt = "I am 22 old and 6 months"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)


# In[3]:


import re

txt = "My name is omar"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("om.r", txt)
print(x)


# In[4]:


import re

txt = "This is the third lab in information retrieval"

#Check if the string starts with 'hello':

x = re.findall("^omar", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


# In[5]:


import re

txt = "This is the third lab in information retrieval"

#Check if the string ends with 'world':

x = re.findall("retrieval$", txt)
if x:
  print("Yes, the string ends with 'world'")
else:
  print("No match")


# In[6]:


import re

txt = "The aix ai n Spain falls mainly in the plain!"


#Check if the string contains "ai" followed by 1 or more "x" characters:

x = re.findall("aix+", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[7]:


txt = "The aix ai n Spain falls mainly in the plain!"

import re

txt = "rainnn rain raix "

#Check if the string contains "ai" followed by 1 or more "x" characters:

x = re.findall("ain+", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


# In[8]:


import re

txt = 'Regular expression is a sequence of character(s) mainly used to find and replace patterns in a string or file'

#Check if the string starts with 'hello':

x = re.findall("^Regular", txt)
x = re.findall("File$", txt)

print(x)

if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


# In[9]:



txt= 'Regular expression is a sequence of character(s) mainly used to find and replace patterns in a string or file'

start = txt.find("patterns") + len("patterns")
end = txt.find("file")
substring = txt[start:end]
print(substring)


# In[10]:


txt= 'Regular expression is a sequence of character(s) mainly used to find and replace patterns in a string or file'

start = txt.find("patterns") 
end = txt.find("file") + + len("file")
substring = txt[start:end]
print(substring)


# In[11]:


import re
replacement_patterns = [
(r'won\'t', 'will not'),
(r'can\'t', 'cannot'),
(r'i\'m', 'i am'),
(r'ain\'t', 'is not'),
(r'(\w+)\'ll', '\g<1> will'),
(r'(\w+)n\'t', '\g<1> not'),
(r'(\w+)\'ve', '\g<1> have'),
(r'(\w+)\'s', '\g<1> is'),
(r'(\w+)\'re', '\g<1> are'),
(r'(\w+)\'d', '\g<1> would')]

class RegexReplacer(object):
  def __init__(self, patterns=replacement_patterns):
    self.patterns = [(re.compile(regex), repl) for (regex, repl)in patterns]
  def replace(self, text):
    s = text
    for (pattern, repl) in self.patterns:
      (s, count) = re.subn(pattern, repl, s)
    return s
replacer= RegexReplacer()
text= "we'll see how to replace words using regular expressions such dosen't , cann't and so on"
print(replacer.replace(text))


# In[ ]:


#Exercise 3: Get a sentence from the user. If the sentencecontains any repeating characters, apply classRepeatReplacer to remove them.

class RepeatReplacer(object):
    def __init__(self):
        self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
        self.repl = r'\1\2\3'
        def replace(self, word): 
            repl_word = self.repeat_regexp.sub(self.repl, word) 
            if repl_word != word:
                return self.replace(repl_word)
            else:
                return repl_word
    


replacer= RepeatReplacer()
text= input("input your text:")
replacer.replace(text)


# In[ ]:




