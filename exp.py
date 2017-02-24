
# coding: utf-8

# # Python Basic Training

# ## Python2 or Python3

# In[1]:

print 3//2
print 3/2
print 3.0/2
print 'Python 入门'
print(1,2)


# In[2]:


from __future__ import division,print_function
print(3//2)
print(3/2)
print(3.0/2)
print('Python 入门')
print(1,2)


# ## Data Structure
# Operators:
# - +/-
# - +,-,*,/,%,//
# - \*\*
# - ()
# 
# Type1: 
# - int
# - float
# 
# Type2:
#  - str
#  - list
#  - tuple
#  - dict
#  - set
# 
# Type3: 
# - None

# In[9]:

a='abcdefghijklmn'
b='xyz'
print('1.','***',a+b,'***')
print('2.','***',a*3,'***')
print('3.','***',a*0,'***')
print('4.','***',a*-1,'***')
print('5.',a[0:5],sep='')
print('6.',a[:5],sep='')
print('7.',a[-1],sep='')
print('8.',a[:-1],sep='')
print('9.',a[::2],sep='')
print('10.',a[::-1],sep='')
a+=b
print('11.',a,sep='')


# In[13]:

get_ipython().magic('reset -f')
a=[1,2,3,4,5,6,7,8,9,0]
b=['a','b','c']
c=[[1],[2],[3]]
print('1.',a+b)
print('2.',a*3)
print('3.',a*0)
print('4.',a*-1)
print('5.',a[0:5],sep='')
print('6.',a[:5],sep='')
print('7.',a[-1],sep='')
print('8.',a[:-1],sep='')
print('9.',a[::2],sep='')
print('10.',a[::-1],sep='')
a+=c
b+='d'
print('11.',b)
print('12.',a)


# In[16]:

get_ipython().magic('reset -f')
a=1
b='2'
a,b=b,a
print('a=%s,b=%d.' %(a,b))


# In[ ]:



