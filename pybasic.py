
# coding: utf-8

# # Python Basic Sharing
# 
# ## Python2 & Python3
# Life is short. To use Python2 or Python3, it's a question.

# In[ ]:

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
# 

# In[ ]:

for i in range(3,100):
    if i % 2:
        if isPrime(i):
            pass
        else:
            for j in range(3,i,2):
                if i%j==0:
                    print(j)
                    if j>(i/2):
                        print('impossible')
    else:
        print('ok')


# ## Data Structure

# In[ ]:

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


# In[ ]:

# None,bool
None
0==False
1==True
2==True
'1'==True
if 2:print(2)
if 'i':print('i')


# In[ ]:

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
print('9.',a[::2],sep='')
print('10.',a[::-1],sep='')
b+='d'
a+=c
print('11.',b)
print('12.',a)


# In[ ]:

a=list(range(10))
b=a
a+='10'
print(b)

a=list(range(10))
b=a
a.append('10')
print(b)

a=list(range(10))
b=a
a=a+['10']
print(b)


# In[ ]:

import copy
a=[1,2,3]
b=[4,5,6,a]
c=copy.copy(b)
d=copy.deepcopy(b)
a.append(0)
b.append(7)
print(b)
print(c)
print(d)


# In[ ]:

print(a.__len__())
print(len(a))

from random import shuffle
a=list(range(10))
print(a)
shuffle(a)
print(a)
a.sort()
print(a)


# In[ ]:

a=[1,
  2,
3]
print(a)


# In[ ]:

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


# In[ ]:

# tuple
a=1
b='2'
a,b=b,a
print('a=%s,b=%d.' %(a,b))
[c,d]=[1,2]
print('c=%d,d=%d' %(c,d))


# In[ ]:

a=1
b=1,
c=(1,2,3)
d=zip(['1','2','3'],[4,5,6])
print(a)
print(b)
print(c)
print(d)


# In[ ]:

# dict
e=dict(d)
print(e)


# In[ ]:

a='Welcome to Python Basic Sharing.'
b={}
for i in a: b[i]=b.get(i,0)+1
print(b)
print(b.keys())
print(b.values())
print(b.items())


# In[ ]:

from pprint import pprint
pprint(b)


# In[ ]:

# set
a=set([1,1,1,1,1,1])
print(a)
a.add(2)
a.remove(1)
print(a)


# In[ ]:

a={1,2,3}
b={3,4,5}
print(a&b)
print(a|b)
print(a-b)


# ## List Comprehension & Generator

# In[ ]:

# list comprehension
a=[x for x in range(10)]
b=[x*y for x in range(1,11,2) for y in range(2,12,2)]
c=[x*y for x,y in zip(list(range(1,11,2)),list(range(2,12,2)))]
print(a)
print(b)
print(c)


# In[ ]:

import os
filelist=[x for x in os.listdir('.')]
fulllist=['./'+x for x in filelist]
print(filelist)
print(fulllist)


# In[ ]:

# generator
a=(x for x in range(10))
print(a)
print(list(a))


# In[ ]:

def odd(x):
    for i in range(x):
        if i%2==1:
            yield i
print(list(odd(10)))
a=odd(15)
print(a)
print(list(a))


# In[ ]:

try:
    a=odd(10)
    for i in range(100):
        print(next(a))
except StopIteration:
    raise StopIteration('Too many')


# In[ ]:

def odd():
    i=1
    while True:
        if i%2==1:
            yield i
        i+=1
a=odd()
for i in range(10):
    print(next(a))


# ## map, reduce & filter

# In[ ]:

#map
a=list(range(10))
print(map(lambda x:x**2,a))
print(list(map(lambda x:x**2,a)))


# In[ ]:

#reduce
from functools import reduce
a=range(100)
print(reduce(lambda x,y:x+y,a))
print(reduce(lambda x,y:[x]+[y],a))
print(reduce(lambda x,y:list(x),a))


# In[41]:

a=range(10)
print(reduce(lambda x,y:str(x)+' + '+str(y),a),'=',sum(a))


# In[ ]:

#filter
a=range(100)
print(list(filter(lambda x:True if x%2==1 else False,list(a))))


# In[ ]:




# In[ ]:



