#!/usr/bin/env python
# coding: utf-8

# In[2]:


#indexing with sequence
#string indexing


# In[4]:


a='communication'
print([0])


# In[7]:


a='communication'
print(a[0],[3])


# In[8]:


print(a[0:])


# In[9]:


print(a[:-1])


# In[11]:


print(a[0:5:2])


# In[13]:


#list indexing

a=[1,3,'hi',(7,8),{'a for':'value'}]
print(a[0])


# In[15]:


print(a[0:3])


# In[16]:


print(a[1],a[3])


# In[17]:


print(a[:-1])


# In[19]:


print(a[0:5:2])


# In[20]:


#dictionary indexing
a={'name':'xyz','age':21,'course':'python'}


# In[21]:


print(a['age'])


# In[22]:


#tuple indexing
a=('fruits',34,4.5)
print(a[0])


# In[23]:


print(a[0:3])


# In[24]:


print(a[:-1])


# In[25]:


print(a[0:3:1])


# In[26]:


#slicing indexing with sequence:
a=("a","b","c","d","e","f","g","h")
print(a[0:8])


# In[29]:


print(a[0:8:4])


# In[30]:


print(a[3:8])


# In[31]:


print(a[3:])


# In[32]:


print(a[:-3])


# In[33]:


#exceptional handling
#using try,except and else block

try:
  print(x)
except:
  print("An exception occurred")


# In[34]:


try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# In[40]:


try:
  print("Hey!!")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


# In[43]:


try:
  print(3690)
except:
  print("I'm there!!")
finally:
  print("not there")


# In[45]:


#regular expression
'Python has a built-in package called re, which can be used to work with Regular Expressions.'
#findall()
import re

txt = "I'm doing internship in internity"
x = re.findall("shi", txt)
print(x)


# In[46]:


#find empty()
import re

txt = "I'm doing internship in internity"
x = re.findall("Data Science", txt)
print(x)


# In[47]:


#search()
import re

txt = "I'm doing internship in internity"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


# In[48]:


#Split the string at every white-space character:
import re

txt = "I'm doing internship in internity"
x = re.split("\s", txt)
print(x)


# In[49]:


#using sub fuction
#Replace all white-space characters with the digit "9":
import re

txt = "I'm doing internship in internity"
x = re.sub("\s", "9", txt)
print(x)


# In[ ]:




