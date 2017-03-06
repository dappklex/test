
# coding: utf-8

# # Python Basic Sharing
# ## Python2 & Python3
# Life is short. To use Python2 or Python3, it's a question.

# In[17]:

# Python2
'''
print 5
print 5/2     # 2
print 5//2    # 2.5
print(2)      # 2
print(2,3)    # (2, 3)
print u'中文'
print u'\u4e2d\u6587'

# -*- coding: utf-8 -*-
from __future__ import print_function,division

print(5)
print(5/2)    # 2.5
print(5//2)   # 2.5
print(2)      # 2
print(2,3)    # 2 3
print('中文')
print('\u4e2d\u6587')
'''

# Python3
list()


# ## Indentation
# Python: 从入门到购买游标卡尺

# In[ ]:

for i in range(3,100):
    if i % 2:
        if isPrime(i):
            pass
        elif isOdd(i):
            for j in range(3,i,2):
                if i%j==0:
                    print(j)
                    if j>(i/2):
                        print('impossible')
else:
    print('ok')


# In[16]:

for i in 'Hello, world!':
    print(i,end='')


# ## Data Structure

# In[ ]:

# +/-
# + - * / %
# **
# ()


# In[30]:

# int,float,str
''
""
''''''
""""""

print('''
123
abc
        ssss
''')
print('\t\n\'\\')
print(r'\t\n\'\\')

print('''fauhfasdfasd'fafsdasd""dfdfa''')


# In[32]:

# None,bool
print(None)
print(0==False)
print(1==True)
print(2==True)
print('i'==True)
if 2:print(2)
if 'i':print('i')


# In[34]:

# list,tuple,dict,set
#list
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
print('9.',a[1::2],sep='')
print('10.',a[::-1],sep='')
b+='d'
a+=c
print('11.',b)
print('12.',a)


# In[36]:

print(range(10))
for i in range(10):print(i)
print(list(range(10)))


# In[37]:

a=list(range(10))
b=a
a.append('10')
print(b)


# In[38]:

a=list(range(10))
b=a
a+='10'
print(b)


# In[39]:

a=list(range(10))
b=a
a=a+['10']
print(b)


# In[40]:

import copy
a=[1,2,3]
b=[4,5,6,a]
c=copy.copy(b)
d=copy.deepcopy(b)
a.append(0)
b.append(7)
print(a)
print(b)
print(c)
print(d)


# In[46]:

from random import shuffle
a=list(range(100))
print(a)
shuffle(a)
print(a[:10])
a.sort()
print(a[:10])


# In[49]:

for i in range(1):
    a=[11111111111111,
  2222222222,
3333333333333333333]
print(a)


# In[50]:

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


# In[62]:

a='abcdefghijklmnopqrstuvwxyz'
a=list(a)
shuffle(a)
print(''.join(a))


# In[64]:

a='abcdefghijklmnopqrstuvwxyz'
b=list(range(len(a)))
shuffle(b)
print(b)


# In[71]:

from numpy import *
c=array(b)
print(c[1])


# In[ ]:




# In[ ]:



