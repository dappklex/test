# coding=utf-8
# -*- coding: utf-8 -*-
'''
HSBC Python基础
（2016年12月21日，广州）
'''

import os
os.getcwd()
from numpy  import *
import pandas as pd

print u'中文'

x,y,z=3,4,5
x+=1
y*=2
z**=3
x,y,z

#  Python初步

# 案例1：温度转换
input_str = raw_input('温度是?')
if input_str[-1] in ['C', 'c']:
    f = 1.8 * eval(input_str[0:-1]) + 32  # 将输入字符串中，除最后一位外的子串转换成数字
    print '转换后的温度是 %d 华氏度' % f
elif input_str[-1] in ['F', 'f']:
    c = (eval(input_str[0:-1]) - 32) / 1.8
    print '转换后的温度是 %d 摄氏度' % c
else:
    print '输入错误!'

# 字符串切片：
tIndex = 'Python'
tIndex[4]
tIndex[-1]
tIndex[0]
tIndex[-5]    # 倒着数
tIndex[1:-2]
tIndex[:3]
tIndex[3:]
tIndex[:]

# 输入输出语句
input( "What is your name?")  # 直接输入Python是不认的，要加入引号。或者输入表达式。
raw_input("What is your name?")  # 不论输入什么，以字符串对待。

# 赋值语句
# x, y=y, x  #互换

num1, num2 = input("请输入2个数，用逗号分开：")
avg_num = (num1 + num2) / 2
print("平均数是 %d") % avg_num  # %d是以整数类型输出

# 分支语句（见前面温度转换的例子）
'''
if
elif
...
else:
'''

# 循环语句
'''
for i in range(计数值)
'''

range(1,6)
range(1,5,2)
range(5)
[x * x for x in range(1, 11)]
[x * x for x in range(1, 11) if x % 2 == 0]


# eval()
eval("1+2")
eval("123")
eval("'hello'")
eval("hello")


# 函数
# 把温度转换的案例封装成函数：
def tempConvert():
    input_str = raw_input('温度是?')
    if input_str[-1] in ['C', 'c']:
        f = 1.8 * eval(input_str[0:-1]) + 320  # 将输入字符串中，除最后一位外的子串转换成数字
        print '转换后的温度是 %d 华氏度' % f
    elif input_str[-1] in ['F', 'f']:
        c = (eval(input_str[0:-1]) - 32) / 1.8
        print '转换后的温度是 %d 摄氏度' % c
    else:
        print '输入错误!'

tempConvert()

# 案例2：房屋贷款的计算（等额本息法，即每月还款额度相同）
def house_loan(a, p, y):
    m = a * 10000 * (p / 12) * (1 + p / 12) ** (12 * y) / ((1 + p / 12) ** (12 * y) - 1)
    return m

A, Y = input("请输入贷款总金额和年数并用逗号隔开：")
dkfs = raw_input("请输入贷款方式：")
p = 0
if dkfs in ['c', 'C']:
    if Y > 0 and Y <= 1:
        p = 0.06
    elif Y > 1 and Y <= 3:
        p = 0.0615
    elif Y > 3 and Y <= 5:
        p = 0.064
    elif Y > 5:
        p = 0.0655
    else:
        print "输入错误！"
elif dkfs in ['g', 'G']:
    if Y > 0 and Y <= 5:
        p = 0.04
    elif Y > 5:
        p = 0.045
    else:
        print "输入错误！"
else:
    print "输入错误！"

M = house_loan(A, p, Y)
print "月供是：%5.2f" % M

'''
抓了a,b,c,d4名犯罪嫌疑人.其中有一名是小偷，审讯中：
a说我不是小偷
b说c是小偷
c说小偷肯定是d
d说c胡说！
其中有3个人说的是实话，一个人说的是假话，编程推断谁是小偷。
'''
for thief in ['a','b','c','d']:
    sum = (thief != 'a') + (thief == 'c') + (thief == 'd') + (thief !='d')
    if sum == 3:
        print "小偷是：%s " % thief

#数学库和随机库
#Monte Carlo模拟：
import random
NUMBER_OF_TRIALS = 1000000
numberOfHits = 0
for i in range(NUMBER_OF_TRIALS):
    x = random.random() * 2 - 1       #在(-1,1)内
    y = random.random() * 2 - 1
    if x * x + y * y <= 1:
        numberOfHits += 1
pi = 4 * float(numberOfHits) / NUMBER_OF_TRIALS
print('PI is %5.5f'%(pi))

from random import *
random()
uniform(1,10)
randint(1, 10)
randrange(0,10,3)
range(10)
ra=range(10)
choice(ra)
shuffle(ra)
ra
sample(ra,4)

seed(10)
uniform(1,10)
uniform(1,10)

#Python标准库：
import calendar
calendar.prmonth(2016,12)
calendar.prcal(2017)

import datetime
d1=datetime.datetime(1984,5,29)  #生日
d2=datetime.datetime.now()
print("年龄是"+str((d2-d1).days/365))


# 字符串和正则表达式
str1="Hello"
str2='Gino'
print str1, str2
type(str1)

for ch in "pine!":
    print ch

#正则表达式：
'''
用\d可以匹配一个数字，\w可以匹配一个字母或数字，.可以匹配任意字符。特殊字符用'\'转义。
用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，
用{n}表示n个字符，用{n,m}表示n-m个字符。
\d{3}\s+\d{3,8}：
\d{3}表示匹配3个数字，例如'010'；
\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
\d{3,8}表示3-8个数字，例如'1234567'。
*[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，
比如'a100'，'0_Z'，'Py3000'等等；
*[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，
后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量。
^表示行的开头，^\d表示必须以数字开头。
$表示行的结束，\d$表示必须以数字结束。
'''
s = 'ABC\\-001'     # Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'

#建议使用Python的r前缀，就不用考虑转义的问题：
s = r'ABC\-001' # Python的字符串
# 对应的正则表达式字符串不变：
# 'ABC\-001'

import re
re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
re.match(r'^\d{3}\-\d{3,8}$', '010 12345')
#match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。

#切分字符串:
'a b   c'.split(' ')  #无法识别空格
re.split(r'\s+', 'a b   c')
re.split(r'[\s\,]+', 'a,b, c  d')
re.split(r'[\s\,\;]+', 'a,b;; c  d')

#分组提取：
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
m
m.group(0)  #原始字符串
m.group(1)
m.group(2)

import re
m = re.search('[0-9]','abcd4ef')
print(m.group(0))

#贪婪匹配:
#怎样匹配出数字后面的0?
re.match(r'^(\d+)(0*)$', '102300').groups()
#由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
#让\d+采用非贪婪匹配（尽可能少匹配），才能把后面的0匹配出来，加个?就可让\d+采用非贪婪匹配：
re.match(r'^(\d+?)(0*)$', '102300').groups()

#如果一个正则表达式要重复使用几千次，可以预编译该正则表达式:
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
re_telephone.match('010-12345').groups()
re_telephone.match('010-8086').groups()

#  循环结构
i=1;sum=0
while i<=100:
    sum+=i
    i+=1
print "sum",sum

i=1;mu=0;s=0.0
n=input('请输入n值：')
while i<=n:
    mu+=i
    i+=1
    t=1.0/mu
    s=s+t
print 's=',s

#使得2+4+6+8+10+...+n<1000成立的最大的n值？
sum=0;i=2
while True:
    sum+=i
    if sum>=1000:
        break
    else:
        i+=2
print i

#2000以内能被17整除的所有正整数？
for i in range(1,2001,1):
    if i%17!=0:
        continue
    print i,

#pass:传递而不是略过！
for letter in 'python':
    if letter=='h':
        pass                    #把pass改为continue试试
        print 'h是被pass的部分'
    print '当前字母：', letter
print "再见!"

#continue语句：
mylist=["zope","Python","Perl","Linux"]
for cc in mylist:
    if cc=="Perl":
        continue
    else:
        print cc

for cc in mylist:
    if cc == "Perl":
        pass   #什么也不做,占位符，让程序先走下去看看，否则语法错误
    else:
        print cc

#第五章 序列与字典
x=[8,1.3,"a"]
x[0]
x[-1]
x[1:2]
x[:2]
x[1:]
x[:]
x*3
2 in x
len(x)

#列表
a_list=['a','b','c']
print(a_list[2])

a_list[0]=123
print a_list

a_list.append(True)
a_list

a_list.extend(['x',6])
a_list

a_list.insert(1,'c')
a_list

a_list.count('c')

del a_list[0]
a_list

a_list.remove('c')   #第一个被移走
a_list

a_list.pop()
a_list

a_list.pop(1)    #把c移走了
a_list

a_list.reverse()
a_list

a_list.sort()
a_list

#使用列表对象的方法：
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
L

[m + n for m in 'ABC' for n in 'XYZ']
[d for d in os.listdir('.')]
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]

t=[]
t.append(271)   #1月份的电量
t.extend([151,78,92,83,134,357,421,210,88,92,135])  #其余11个月的电量
t
t.remove(421)
t.insert(7,425)
#用电量最高的月份？
t.index(max(t))+1
#用电量从高低排序：
t.sort(reverse=True)
t.sort()
t[::-1]

#元组（只读列表）
tup=('physics','chemistry',1997,2000)
print tup
del tup
print tup

t = (1,) #Python在显示只有1个元素的tuple时，会加一个逗号
t

#字符串操作：
s="Pythonn"

s.index('P')
s.index('h',1,4)
s.index('y',1,4)
s.index('y',3,4)

s.find('t')

s.replace('n','i')
s.count('n')

s.split()

s="Hello Gino Good morning!"
s.split()

s='name:haha,age:20|name:python,age:30|name:fef,age:55'
x,y=s.split('|',1)   #别写2，一个个分
print x
print y

li=['apple','peach','pear']
sep='-'
s=sep.join(li)
s

#检测字符串是否全是数字：
mystr=raw_input("请输入一个字符串：\n")
patt="0123456789"
founderr=False
for cc in mystr:
    if cc not in patt:
        founderr=True
if founderr:
    print("该字符串包含非数字字符。")
else:
    print("该字符串全是数字字符。")

#转换
s="123,45"
list(s)
tuple(s)

s=('a','b','c','d')
"".join(tuple(s))

s=['a','b','c','d']
"".join(list(s))

#字典
d={'Gino':95,'Bob':75,'Tom':85}
d['Gino']
#字典的特性请记住。

d.keys()
d.has_key('Gino')
d.values()
d.get('Tom')
d.items()

del d['Gino']
print d

d.pop('Bob')
print d

d.clear()
d

tel={'gree':8127,'mark':8567,'Gino':8333}
tel1={'gree':8562,'star':8622}
tel.update(tel1)
tel

'gree' in tel

'''
案例5：已知10个学生的姓名和成绩，请找出其中的最高分和最低分，
并求出10个学生的平均分。
'''
stu_score={"Gino":95,"Mike":79,"Mith":42,"Pete":83,"Jack":55,
           "Lucy":91,"Duke":71,"Vict":69,"Zoro":63,"Luke":87}
max_score=0
max_stu_name=''
min_score=100
min_stu_score=''
avg_score=0
stu_num=len(stu_score)
print "成绩分别是："
for key in stu_score.keys():
    print key,":",stu_score[key],";",
#换行：
    print
print
print

#进行统计：
for key in stu_score.keys():
    if stu_score[key]>max_score:
        max_score=stu_score[key]
        max_stu_name=key
    if stu_score[key]<min_score:
        min_score=stu_score[key]
        min_stu_name=key
    avg_score+=stu_score[key]
avg_score=avg_score/stu_num

print "全班共有",stu_num,"人，平均成绩为：",avg_score,"分。"
print "最高分是：",max_stu_name,max_score,"分"
print "最低分是：",min_stu_name,min_score,"分"

#集合：
s1={2,4,6,8,10}
s1
s2={'hello'}
s2
s3=set('hello')
s3
s5=set(['he','hello','her','here'])
s5
L1=[1,2,3,4,1,2,3,4]
s4=set(L1)
s4
L2=list(s4)
L2
s2<=s5
s7={'hen','height','her'}
s7|=s2
s7
s7.union(s2)
s7&s5
s7.intersection(s5)
s7|s5
s7^s5

# numpy之数组用法
a = arange(15).reshape(3, 5)
a
a.shape
a.ndim  #2个维度
a.size

b = array([6, 7, 8])
b
b.ndim #1个维度

#可以使用array函数从常规的列表和元组创造数组：
a = array( [2,3,4] )
a
a.dtype
b = array([1.2, 3.5, 5.1])
b.dtype

b = array( [ (1.5,2,3), (4,5,6) ] )
b

zeros( (3,4) )
ones( (2,3,4), dtype=float64 )  #注意第一个2是控制有多少个的
empty( (2,3) )

arange( 0, 2, 0.3 )  #返回的是数组！

#打印数组：
a = arange(6)
print a

b = arange(12).reshape(4,3)
print b

c = arange(24).reshape(2,3,4)
print c

print arange(10000).reshape(100,100)
set_printoptions(threshold='nan')  #可打印整个数组

set_printoptions(threshold=5)
print(arange(10))

set_printoptions(precision=4)
print(array([1.123456789]))

#基本运算：
a = array( [20,30,40,50] );a
b = arange( 4 );b
c=a-b;c
b**2
a<33

A = array( [[1,1],
            [0,1]] )
B = array( [[2,0],
            [3,4]] )
A*B
dot(A,B)  #矩阵乘法!

a = ones(3, dtype=int32);a
b = linspace(0,pi,3);b
b.dtype.name
c = a+b
c
c.dtype.name

a = random.random((2,3))
a
a.sum()  #6个数之和
a.min()
a.max()

b = arange(12).reshape(3,4)
b
b.sum(axis=0)                            # column
b.max(axis=1)                            # row
b.cumsum(axis=1)

#索引，切片和迭代:
a = arange(10)**3
a
a[2:5]
a[:6:2] = -1000    # 即a[0:6:2] = -1000
a
a[ : :-1]          # reversed a

def f(x,y):return 10*x+y
b = fromfunction(f,(5,4),dtype=int)  #观察看规律
b
b[0:5, 1]
b[ : ,1]         #同前
b[1:3, : ]
b[-1]            #相当于b[-1,:]
for row in b:print row
for element in b.flat:print element,  #使用flat属性，该属性是数组元素的一个迭代器

a = arange(12)**2 ;a
i = array([1,1,3,8,5])
a[i]
j = array([[3, 4], [ 9, 7]])
a[j]

palette = array( [ [0,0,0],
                   [255,0,0],
                   [0,255,0],
                   [0,0,255],
                   [255,255,255] ] )
image = array( [ [ 0, 1, 2, 0 ],
                 [ 0, 3, 4, 0 ]  ] )
palette[image]

time = linspace(20, 145, 5);time
data = sin(arange(20)).reshape(5,4);data
ind = data.argmax(axis=0);ind
time_max = time[ind];time_max
data_max = data[ind, xrange(data.shape[1])]  # => data[ind[0],0], data[ind[1],1]...
data_max
all(data_max == data.max(axis=0))

A = arange(12);A
A.shape = (3, 4)
M = mat(A.copy())
print A;M
A[1:,].take([1,3],axis=1)
A[0,:]>1
A[:,A[0,:]>1]
M[0,:]>1
M[:,M[0,:]>1]   #错误！
M[:,M.A[0,:]>1]

#  函数与模块
#函数可以返回多个值:
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print x, y

def Swap_Ref(x,y):
    t=x
    x=y
    y=t
a=10;b=20
print "exchange before a=",a,"b=",b
Swap_Ref(a, b)
print "exchange after a=",a,"b=",b

def max_num(x,y):
    if x>y:
        return  x
    else :
        return y
print max_num(2,3)

another=max_num
another(1,8)

#可变长参数：
def foo(x,*y,**z):    #一元组一字典
    print x
    print y
    print z
foo(1)
foo(1,2,3,4)
foo(1,2,3,a="a",b="b")

#要计算a^2+ b^2+ c^2+ ……
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1, 2)
calc()
nums = [1, 2, 3, 4]
calc(*nums)


#lambda函数：
f=lambda a,b:a+b
f(1,2)
f("abc","def")

Arr=[(lambda x:x**2),(lambda x:x**3),(lambda x:x**4)]
print (Arr[0](2),Arr[1](2),Arr[2](2))

#map函数：
arr=map(lambda x: x**2, [2,4,6,8,10])
for ee in enumerate(arr):
    print ee

#iter函数：
list=[111,222,333]
it=iter(list)
print (next(it))
print (next(it))
print (next(it))

#迭代器之filter函数：
def is_even(x):
    return x % 2 == 0
arr=filter(is_even, [1,2,3,4,5,6,7,8,9,10])
for e in enumerate(arr):
    print e

#迭代器之enumerate函数：
list=[111,222,333]
for index, val in enumerate(list):
    print ("第%d个元素是%s"%(index+1, val))

#生成器：
#example1:
def addlist(alist):
    for i in alist:
        yield i+1
alist=[1,2,3,4]
for x in addlist(alist):
    print x,

#example2:
def Fibonacci(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print b,
        yield b         #运行这步将变成生成器！一边循环一边计算的机制，称为生成器。
        a, b = b, a + b
        n+=1
Fibonacci(8)
for nnn in Fibonacci(9):print nnn,

L = [x*x  for x in range(10)];L
L = (x*x  for x in range(10));L
L.next()

for nnnnn in L: print nnnnn,

#xrange用法与range完全相同，所不同的是生成的不是一个数组，而是一个生成器.
#xrange做循环的性能比range好，尤其是返回很大的时候,不占内存空间。
xrange(5)
list(xrange(5))

#reduce函数：
from functools import reduce
def myadd(x,y):
    return x+y
sum=reduce(myadd, (2,4,6,8,10))
print  sum

def fn(x, y):return x * 10 + y
reduce(fn, [1, 3, 5, 7, 9])

#zip函数：
a=[1,2,3];b=[4,5,6,7,8,9]
zipped=zip(a,b)
for element in zipped:
    print element

#比较一下：
list=[2,-6,11,-7,8,15,-14,-1,10,-13,18]
sum=0
for i in range(len(list)):
    if list[i]>0:
        sum+=list[i]
print sum

sum=filter(lambda x: x>0,list)
s=reduce(lambda x, y:x+y, sum)
print s

#递归函数：
#比如计算5的阶乘，一般方法为：
s=1
for i in range(1,6):
    s=s*i
print s

#递归思路为：
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print fact(5)

#汉诺塔问题：
def MoveTower(n, source, dest, temp):
    if n==1:
        print "移动"+source+"→"+dest+"."
    else:
        MoveTower(n-1, source, temp, dest)
        MoveTower(1, source, dest, temp)
        MoveTower(n-1, temp, dest, source,)

MoveTower(2, "A", "C", "B")

'''约瑟夫环问题：
10个人，从1~10依次编号，每个人开始报数，报到3的人自动出列，
当有人出列后，从后一个人开始重新从1报数，以此类推。
求前8个人的号码?'''
thelist=range(1,11)
deleted=[]
x=0;i=0
while len(deleted)<8:
    if(x>9):
        x=0
    if(thelist[x] not in deleted):
        i+=1
    if i==3:
        print(str(thelist[x])+"出列"),
        deleted.append(thelist[x])
        i=0  #重置0
    x+=1     #要不断累加

#贪心算法：
#问题：用人民币凑足56.32元，每个数量的币种要求尽可能的少。
rmb=[100,50,20,10,5,2,1,0.5,0.1,0.05,0.02,0.01]  #为什么要从大到小排列？
money=56.32
pay=[]
for d in rmb:
    while money>=d:
        money-=d
        pay.append(d)
sum(pay)
pay

# -*- coding: utf-8 -*-
import os
import sys
import numpy as np
from numpy import *
from common_libs import *
import matplotlib.pyplot as plt
# 求解原方程
A=mat([[8,-3,2],[4,11,-1],[6,3,12]])
b=mat([20,33,36])
result= linalg.solve(A,b.T)
print result

# 迭代求原方程组的解：x(k+1)=B0*x(k)+f
B0 = mat([[0.0,3.0/8.0,-2.0/8.0],[-4.0/11.0,0.0,1.0/11.0],[-6.0/12.0,-3.0/12.0,0.0]])
m,n = shape(B0)
f = mat([[20.0/8.0],[33.0/11.0],[36.0/12.0]])

error = 1.0e-6 # 误差阈值
steps = 100 # 迭代次数
xk = zeros((3,1)) # 初始化 xk=x0
errorlist =[] # 记录逐次逼近的误差列表
for k in xrange(steps): # 主程序
	xk_1 = xk     # 上一次的xk
	xk = B0*xk+f  # 本次xk
	errorlist.append(linalg.norm(xk-xk_1)) # 计算并存储误差
	if errorlist[-1]<error: # 判断误差是否小于阈值
		print k+1   # 输出迭代次数
		break
print xk   # 输出计算结果
# 绘制误差收敛散点图
matpts = zeros((2,k+1))
matpts[0] = linspace(1,16,16)
matpts[1] = array(errorlist)
drawScatter(plt,matpts)
plt.show()

#二分查找：
def halffind(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        m=(low+high)//2
        if arr[m]==x:
            return m
        else:
            if x<arr[m]:
                high=m-1
                print high,
            else:
                low=m+1
                print low,
    if low>high:
        return -1
arr=[3,5,6,9,10,11,15,18,19,22,32,35,88,90,91,98]  #须排好序，否则找不到。
while (1):   #换成while True也可以.
    key=int(input("The number you want to find is?"))
    n=halffind(arr,key)
    if n==-1:
         print("can't find")
    else:
         print(key,"is in the position",n)

#排序：
#插入排序:
def insertSort(a):
    for i in range(len(alist)-1):
        for j in range(i+1,len(alist)):
            if a[i]>a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a

#冒泡排序:
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

#选择排序:
def selectionSort(alist):
    j = 0
    while j != len(alist):
        for i in range(j, len(alist)):
            if alist[i] < alist[j]:
                alist[j],alist[i] = alist[i],alist[j]
        j = j+1
    return alist

alist = [54,26,99,17,77,31,61,55,20,2,75]
print insertSort(alist)
print bubbleSort(alist)
print selectionSort(alist)

#冒泡排序2：
def bublesort2(l,n):
    for i in range(0,n-1,1):
        for j in range(0,n-1-i,1):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    print(l)
l=[2,-4,-27,8,9,17,93]
print(l)
n=len(l)
bublesort2(l,n)

#快速排序(递归)
'''
选定一个key值然后把比他小的放到一边，把比他大的放到另一边，
然后不断的分下去，直到最小的元素和最大的元素为止。
'''
def  qiucksort(arr):
    return [] if arr == [] else \
        qiucksort([y for y in arr[1:] if y<arr[0]])+[arr[0]]+\
        qiucksort([y for y in arr[1:] if y>=arr[0]])

arr=[4, 2, 1, 5, 3, 7, 6]
b=qiucksort(arr)
print "原数组为：",arr
print "排序后数组为：",b
[4]+[5]


#局部变量：
def func(x):
    print "x is", x
    x=2
    print "changed local x to", x
x=50
func(x)
print "x is still",x

#全局变量：
def func():
    global x
    print "x is",x
    x=2
    print "changed global x to", x
x=50
func()
print "Value of x is",x

#  面向对象编程简介
class Person:        #声明类
    name="Gino"
    age=40
    def sayHi(self):
        print 'Hello, Gino! Many people like you'
print Person.name
print Person.age

P=Person()   #创建对象P:对象是类的实例
P.sayHi()

#再定义一个类和构造对象：
import math
class Circle:
    # Construct a circle object
    def __init__(self, radius=1):
        self.radius = radius

    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi

    def setRadius(self, radius):
        self.radius = radius

c=Circle(5)
c.getPerimeter()
c.getArea()
c.radius
print "Area is", Circle(5).getArea()  #匿名对象
# self是指向对象本身的参数，例如，可以使用self.x访问实例变量x；
# 实例变量的作用域是整个类。

#实例属性（只为单独的特定的对象所拥有）：
class People:
    name='Gino'
p=People()
p.age=12  #在类之外定义
print p.name
print p.age
print People.name
Print People.age

class People:
    name='Gino'
    def __init__(self, age):  #这是内置的构造方法，在实例化对象时自动调用
        self.age=age

p=People(19)

print p.name
print p.age
print People.name
Print People.age

#类属性（类中方法之外定义的属性）：
class People:
     name='Gino'  #公有的类属性
     __age=12     #私有的类属性

p=People()

print p.name
print p.__age       #错误，不能访问私有的
print People.name
Print People.__age

#修改与删除类属性：
class People:
    country='China'

print People.country
p=People()
print p.country
p.country='America'
print p.country
del p.country
print p.country

#对象方法之公有：
class Person:
    def sayHi(self):    #公有方法
        print 'Hello, how are you?'
p=Person()
p.sayHi()

#对象方法之私有：
class Person:
    def __sayHi(self):    #私有方法
        print 'Hello, how are you?'
    def output(self):
        self.__sayHi()   # 只能在对象的公有方法中通过self调用

p=Person()
p.__sayHi()   #错误！不能通过对象名调用
p.output()

#类方法：
'''
静态方法无需传入self参数，类成员方法需传入代表本类的cls参数；
静态方法是无法访问实例变量的，而类成员方法也同样无法访问实例变量，但可以访问类变量.
'''
class MyClass:
    @classmethod
    def classMethod(cls):
        print("class method")
MyClass.classMethod()

#静态方法：
'''静态方法仅是类中的函数, 不需要绑定实例,
也就是说静态方法的定义不需要传入 self 参数.
静态方法不属于类的某一个实例对象, 而是属于类本身.
'''
class Fruit:
    price=0
    @staticmethod
    def getPrice():
        return Fruit.price
    @staticmethod
    def setPrice(p):
        Fruit.price=p

print(Fruit.getPrice())
Fruit.setPrice(9)
print(Fruit.getPrice())

#构造函数：
class Complex:
    def __init__(self, realpart, imagpart):
        self.r=realpart
        self.i=imagpart
x=Complex(3.0, -4.5)
print x.r, x.i

class Person:
    def __init__(self, name):
        self.name=name
    def sayHi(self):
        print 'Hello, my name is', self.name
p=Person("Gino")
p.sayHi()

#继承性
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print '(Initialized SchoolMember:%s)' %self.name
    def tell(self):
        '''Tell my details.'''
        print 'Name:"%s"Age:"%s"' %(self.name, self.age)

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print '(Initialized Teacher:%s)' %self.name
    def tell(self):
        SchoolMember.tell(self)
        print 'Salary:"%d' %self.salary

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)   #子类的构造函数必须显式调用基类的构造函数
        self.marks=marks
        print '(Initialized Student:%s)' %self.name
    def tell(self):
        SchoolMember.tell(self)
        print 'Marks:"%d' %self.marks

t=Teacher('Mr.Gino',40,30000)
s=Student('Peter',21,95)

members=[t,s]
for member in members:
    member.tell()     #一起运行


#第八章 文件和模块
f=open('poem.txt','w')    #不用事先建立文本文件
poem='''\
Whenever you need me, I'll be here.
Whenever you're in trouble, I'm always near.
Whenever you feel helpless...
Reach out for me, and I will give you my aid!
 '''
f.write(poem)
f.close()

f=open('f:\poem.txt',"r")
re=f.read()
print re
f.close()

f=open('poem.txt',"r")
line=f.readline()
while line:
    print line,
    line=f.read()
f.close()

f=open('F:\poem.txt',"r")
for line in f.readlines():
    print line
f.close()

#文件指针：
f=open('poem.txt',"r+")
f.seek(0)
f.write('Hello!')
f.seek(9)    #大于0表示移动到文件头之后的位置
f.write('OK')
f.seek(0,2)     #(0,2)移动到最后。这里请尝试总结指针规律！
f.write('Bye for now')
f.close()

f=open('poem.txt',"r")
re=f.read()
print re
f.close()

#存储器：
import cPickle as p
shoplistfile="shoplist2.txt"
shoplist=['apple','banana','orange']

f=file(shoplistfile,'w')
p.dump(shoplist, f)
f.close()

del shoplist

f=file(shoplistfile)
storedlist=p.load(f)
print storedlist

#处理异常：
#!/usr/bin/env python
# 去环境设置寻找python目录
def safe_float(object):
    "safe version of float()"
    try:
        retval = float(object)
    except (TypeError, ValueError), diag:
        retval = str(diag)
    return retval

def main():
    'handles all the data processing'
    log = open('cardlog.txt', 'w')
    try:
        ccfile = open('carddata.txt', 'r')
    except IOError, e:
        log.write('no txns this month\n')
	log.close()
        return

    txns = ccfile.readlines()
    ccfile.close()
    total = 0.00
    log.write('account log:\n')

    for eachTxn in txns:
        result = safe_float(eachTxn)
        if isinstance(result, float):
            total += result
            log.write('data... processed\n')
	else:
            log.write('ignored: %s' % result)
    print '$%.2f (new balance)' % (total)
    log.close()

if __name__ == '__main__':
    main()

x = 'abc'
y = 123
isinstance(x, str)
isinstance(y, str)

def test():
    print "test is running"
if __name__ == "__main__":      #自运行时调用该程序块
    print "test main is working"
if __name__ == "test":          #import时调用该程序块
    print "test is invoked"
'''
一个.py文件，如果是自身在运行，那么他的__name__值就是"__main__"；
如果它是被别的程序导入的（作为一个模块），比如：import re
那么，他的__name__就不是"__main__"了。
所以，在.py文件中使用这个条件语句，可以使这个条件语句块中的命令只在它独立运行时才执行
'''

#  数组和矢量的计算
from numpy import *
import numpy as np
data1 = [6,7.5,8,0,1]
arr1 = np.array(data1)
arr1

data2 = ([1,2,3,4],[5,6,7,8])
arr2 = np.array(data2)
arr2
arr2.ndim
arr2.shape

arr1.dtype
arr2.dtype

np.zeros(10)
np.zeros((3,6))
np.arange(15)

arr = np.array([[1.,2.,3.],[4.,5.,6.]])
arr
arr*arr
arr-arr
1/arr
arr**0.5

arr = np.arange(10)
arr
arr[5]
arr[5:8]
arr[5:8] = 12
arr

arr_slice = arr[5:8]
arr_slice[1] = 12345
arr

arr_slice[:] = 64
arr

arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr3d
arr3d[0]
old_values = arr3d[0].copy()
arr3d[0] = 42
arr3d
arr3d[0] = old_values
arr3d
arr3d[1,1]

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d
arr2d[:1]
arr2d[:2,1:]
arr2d[1, :2]
arr2d[2, :1]
arr2d[:,:1]

names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
np.unique(names)
np.random.normal(size=(5,5))
data =  np.random.randn(7, 4)
data
names=='Bob'
data[names=='Bob']
data[names=='Bob',2:]
names!='Bob'
data[-(names=='Bob')]
mask=(names=='Bob')|(names=='Will')
mask
data[mask]

from numpy import *
a=array([10,20])
tile(a,(3,2))           #构造3X2个copy
tile(42.0,(3,2))

#案例：随机漫步
import random
position=0
walk=[position]
steps=100
for i in xrange(steps):
    step=1 if random.randint(0,1) else -1
    position+=step
    walk.append(position)
print  walk

nsteps=100
draws = np.random.randint(0,2,size=100)   #返回随机的整数，位于半开区间 [low, high)
steps = np.where(draws>0,1,-1)
walks=steps.cumsum()
walks.min()
walks.max()
(np.abs(walk)>=4).argmax()

#案例：线性回归预测
import numpy as np
import sys

N = 5
c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
b = c[-N:]
b = b[::-1]   #相当于reverse
print "b", b

A = np.zeros((N, N), float)
print "Zeros N by N", A

for i in range(N):
   A[i, ] = c[-N - 1 - i: - 1 - i]

print "A", A

(x, residuals, rank, s) = np.linalg.lstsq(A, b)
print x, residuals, rank, s

print np.dot(b, x)    #作预测
#actual close 353.56

#  pandas简介
from pandas import Series, DataFrame
import  pandas as pd

#Series
obj=Series([4,7,-5,3])
obj
obj.values
obj.index

obj2=Series([4,7,-5,3],index=['d','b','a','c'])
obj2
obj2['d']=666
obj2[['c','a','d']]
obj2[obj2>0]

sdata={'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3=Series(sdata)
obj3

states=['California','Ohio','Oregon','Texas']
obj4=Series(sdata, index=states)
obj4
pd.isnull(obj4)
pd.notnull(obj4)
obj4.isnull()

#DateFrame
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
      'year':[2000,2001,2002,2001,2002],
      'pop':[1.5,1.7,3.6,2.4,2.9]}
frame=DataFrame(data)
frame

frame2 = DataFrame(data,columns=['year','state','pop','debt'],
                   index=['one','two','three','four','five'])
frame2
frame2['state']
frame2.year
frame2.ix['three']
frame2['debt'] = np.arange(5.)
frame2

val=Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt']=val
frame2
frame2['eastern']=frame2.state=='Ohio'
frame2

#排序和排名
obj = Series(range(4),index=['d','a','b','c'])
obj.sort_index()

frame=DataFrame(np.arange(8).reshape((2,4)),index=['three','one'],
                columns=['d','a','b','c']);frame
frame.sort_index()
frame.sort_index(axis=1, ascending=False)   #降序排列，axis=1是对列，0是对行。

frame=DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]});frame
frame.sort_values(by='b')
frame.sort_values(by=['a','b'])

data=DataFrame(np.random.randn(1000,4))
data.describe()
col=data[3]  #拿出最后一列
col[np.abs(col)>2]
data[(np.abs(data)>3).any(1)] #选出全部含有绝对值超过3的行

#移除重复数据：
data=pd.DataFrame({'k1':['one']*3+['two']*4,'k2':[1,1,2,3,3,4,4]})
data
data.duplicated()
data.drop_duplicates()
data['v1']=range(7)
data
data.drop_duplicates(['k1'])
data.drop_duplicates(['k1','k2'],keep='last') #保留最后一个即第2个，默认第一个

df1 = DataFrame({'key':['a','a','b','b'],'data1':range(4)})
df2 = DataFrame({'key':['b','b','c','c'],'data2':range(4)})
pd.merge(df1,df2)
pd.merge(df1,df2,how='left')
pd.merge(df1,df2,left_index=True,right_index=True)

# 案例
import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/rasbt/python_reference/master/Data/some_soccer_data.csv')
df
'''
这是一个足球运动员的数据，其中：GP是场数、G是进球数、A是助攻数、
SOT是射正数、PPG是每场比赛的平均得分、P是总得分。
'''
df.columns = [c.lower() for c in df.columns]  #列名称小写
df.tail(3)

df = df.rename(columns={'p': 'points',
                        'gp': 'games',
                        'sot': 'shots_on_target',
                        'g': 'goals',
                        'ppg': 'points_per_game',
                        'a': 'assists',})
df.tail(3)  #重新命名

df['salary'] = df['salary'].apply(lambda x: x.strip('$m'))
df.tail()   #改变列值

df['team'] = pd.Series('', index=df.index)
df.insert(loc=8, column='position', value='')
df.tail(3)    #增加新列


def process_player_col(text):
    name, rest = text.split('\n')
    position, team = [x.strip() for x in rest.split(' — ')]
    return pd.Series([name, team, position])
df[['player', 'team', 'position']] = df.player.apply(process_player_col)
df.tail(3)  #把原来球员一列中的项拆成3项

cols = ['player', 'position', 'team']
df[cols] = df[cols].applymap(lambda x: x.lower())
df.head()

nans = df.shape[0] - df.dropna().shape[0]
print('%d rows have missing values' % nans)  #计算存在NaN的列数

df[df['assists'].isnull()]   #找出assists存在NaN的列
df[df['assists'].notnull()]  #找出assists不存在NaN的列
df.fillna(value=0, inplace=True)
df                           #对NaN列进行填充

import numpy as np
df = df.append(pd.Series(
                [np.nan]*len(df.columns),    # 用NaN填充
                index=df.columns),
                ignore_index=True)
df.tail(3)   #增加新行

df.loc[df.index[-1], 'player'] = 'new player'
df.loc[df.index[-1], 'salary'] = 12.3
df.tail(3)    #对新行赋值

df.sort_values(by='goals', ascending=False, inplace=True)
df.head()
'''
排序。请注意第一列索引已乱。
Series 和 DataFrame 对象的方法中，凡是会对数组作出修改并返回一个新数组的，
往往都有一个replace=False的可选参数。如果手动设定为 True，那么原数组就可以被替换。
'''
df.index = range(1,len(df.index)+1)
df.head()  #重新索引

df_2 = df.copy()
df_2.loc[0:2, 'salary'] = [20.0, 15.0]
df_2.head(3)   #更新列前面2个数

df.set_index('player', inplace=True)
df_2.set_index('player', inplace=True)
df.head(3)     #使用球员当索引

df.update(other=df_2['salary'], overwrite=True)
df.head(3)    #更新薪水列的值

df.reset_index(inplace=True)
df.head(3)    #重新设置索引

df[(df['team'] == 'arsenal') | (df['team'] == 'chelsea')]
df[ (df['team'] == 'arsenal') & (df['position'] == 'forward') ] #选择arsenal对中的前锋

import pandas as pd
close_px=pd.read_csv('stock_px.csv',parse_dates=True, index_col=0)
close_px
close_px[-5:]  #the last 5
rets=close_px.pct_change().dropna()
spx_corr=lambda x: x.corrwith(x['SPX'])
by_year=rets.groupby(lambda x:x.year)
by_year.apply(spx_corr)
by_year.apply(lambda g:g['AAPL'].corr(g['MSFT']))

import statsmodels.api as sm
def regress(data,yvar,xvars):
    Y=data[yvar]
    X=data[xvars]
    X['intercept']=1.
    result=sm.OLS(Y,X).fit()
    return result.params
by_year.apply(regress,'AAPL',['SPX'])

#预备知识：
#1.求欧氏距离：
reload(sys)
sys.setdefaultencoding('utf-8')
vector1 = mat([1,2,3])
vector2 = mat([4,5,6])
print sqrt((vector1-vector2)*((vector1-vector2).T))
#即sqrt(27)

#2.排序：
#用sort函数对列表排序时会影响列表本身，而sorted不会：
a = [1,2,1,4,3,5]
a.sort()
a
a = [1,2,1,4,3,5]
sorted(a)
a
#用sorted(iterable，cmp，key，reverse）：
list1 = [('david', 90), ('mary',90), ('sara',80),('lily',95)]
sorted(list1,cmp = lambda x,y: cmp(x[0],y[0]))  #须统一
sorted(list1,cmp = lambda x,y: cmp(x[1],y[1]))

list1 = [('david', 90), ('mary',90), ('sara',80),('lily',95)]
sorted(list1,key = lambda list1: list1[0])
sorted(list1,key = lambda list1: list1[1])

from operator import itemgetter
sorted(list1, key=itemgetter(1))
sorted(list1, key=itemgetter(0))

import operator
a = [1,2,3]
b = operator.itemgetter(2)   #operator.itemgetter函数获取的不是值，而是定义了一个函数。
b(a)

import numpy as np
x = np.array([[10, 3], [9, 5]])
x
np.argsort(x, axis=0)  #按列排序
np.argsort(x, axis=1)  #按行排序

#最近邻算法案例：
'''
kNN: k Nearest Neighbors

Input:      inX: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)

Output:     the most popular class label
'''

from numpy import *
import operator
from os import listdir

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels
group, labels = createDataSet()
group
labels

#算法：
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

classify0([1.2,0],group, labels, 3)

#案例：手写识别
#首先把32×32的二进制图像矩阵转换为1×1024的向量：
def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

testV = img2vector('testDigits/0_13.txt')
testV[0,0:31]
testV[0,32:63]
len(testV[:])
len(testV.T.tolist())

#手写识别：
def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)    #总共有1934个文本文件
    trainingMat = zeros((m,1024));trainingMat.shape
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
        len(trainingMat[i,:].T.tolist())

    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
        if (classifierResult != classNumStr): errorCount += 1.0
    print "\nthe total number of errors is: %d" % errorCount
    print "\nthe total error rate is: %f" % (errorCount/float(mTest))

handwritingClassTest()

#构建推荐系统（协同过滤方法）：
from math import sqrt

#导入示例的数据：

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

users["Angelica"]

#1.计算距离(例如：Manhattan distance)：
def manhattan(rating1, rating2):
    distance = 0
    commonRatings = False
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
            commonRatings = True
    if commonRatings:
        return distance
    else:
        return -1     #Indicates no ratings in common
manhattan(users["Hailey"], users["Jordyn"])

#定义一个寻找最近用户的函数：
def computeNearestNeighbor(username, users):
    distances = []
    for user in users:
        if user != username:
            distance = manhattan(users[user], users[username])
            distances.append((distance, user))
    distances.sort()
    return distances
computeNearestNeighbor('Angelica', users)

#整合成推荐函数：
def recommend(username, users):
    nearest = computeNearestNeighbor(username, users)[0][1]  #找到最近的那个人
    recommendations = []
    # now find bands neighbor rated that user didn't
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

print( recommend('Hailey', users))
print( recommend('Chan', users))
recommend('Sam', users)
recommend('Angelica', users)  #为什么是空的？

'''
2.用户的评级差异解决：用皮尔逊相关系数解决一致性
(请仔细观察Bill, Jordyn, Hailey的评分特点)
“例如：对于项目A~E，Clara和Robert的评分分别为：
Clara: 4.75, 4.5, 5, 4.25, 4
Robert:4,    3,   5, 2,    1
请问：他们俩评分是否一致？”
字典如何计算皮尔逊相关系数？套公式！
'''
from math import sqrt
def pearson(rating1, rating2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key in rating1:
        if key in rating2:
            n += 1
            x = rating1[key]
            y = rating2[key]
            sum_xy += x * y
            sum_x += x
            sum_y += y
            sum_x2 += pow(x, 2)
            sum_y2 += pow(y, 2)

    denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
    if denominator == 0:
        return 0
    else:
        return (sum_xy - (sum_x * sum_y) / n) / denominator

pearson(users["Angelica"],users["Bill"])
pearson(users["Angelica"],users["Hailey"])
pearson(users["Angelica"],users["Jordyn"])

'''
3.余弦相似度：
应用场景：
a.当在1.5亿首歌上利用播放次数比较2个人时，绝大部分情况下他们之间的公共部分是零，数据是稀疏的；
b.利用词频来比较文本文档相似度时，对于浩瀚的词海，要比较的书的非零属性都相对很少。
余弦相似度定义：x·y的内积/(x的长度·y的长度)
'''
#对于Clara，其长度为：
x=sqrt(4.75**2+4.5**2+5**2+4.25**2+4**2);x
#对于Robert，其长度为：
y=sqrt(4**2+3**2+5**2+2**2+1**2);y
#内积为：
xy=(4.75*4)+(4.5*3)+(5*5)+(4.25*2)+(4*1);xy
#余弦相似度为：
cosxy=xy/(x*y);cosxy  #范围是(-1,1), 此值表示一致性相当好。
'''
总结一下：
a.如果数据稠密，几乎所有的属性没有零值，且属性值大小十分重要，使用距离；
b.如果数据受不同用户使用不同的评级范围的影响，使用皮尔逊相关系数；
c.如果数据稀疏，考虑使用余弦相似度。
d.上述是依赖于单个“最相似”的用户进行推荐，该用户的任何特别倾向会被推荐，
解决的办法是基于多个相似的用户进行推荐，可以使用k近邻方法。
'''
#4.基于物品的协同过滤
#可以使用调整后的余弦相似度，请参见“Python辅助PPT课件1~2页”。
users3 = {"David": {"Imagine Dragons": 3, "Daft Punk": 5,
                    "Lorde": 4, "Fall Out Boy": 1},
          "Matt":  {"Imagine Dragons": 3, "Daft Punk": 4,
                    "Lorde": 4, "Fall Out Boy": 1},
          "Ben":   {"Kacey Musgraves": 4, "Imagine Dragons": 3,
                    "Lorde": 3, "Fall Out Boy": 1},
          "Chris": {"Kacey Musgraves": 4, "Imagine Dragons": 4,
                    "Daft Punk": 4, "Lorde": 3, "Fall Out Boy": 1},
          "Tori":  {"Kacey Musgraves": 5, "Imagine Dragons": 4,
                    "Daft Punk": 5, "Fall Out Boy": 3}}

def computeUserAverages(users):
   results = {}
   for (key, ratings) in users.items():
      results[key] = float(sum(ratings.values())) / len(ratings.values())
   return results
computeUserAverages(users3)
13/3.25

def computeSimilarity(band1, band2, userRatings):
   averages = {}
   for (key, ratings) in userRatings.items():
      averages[key] = (float(sum(ratings.values()))
                      / len(ratings.values()))

   num = 0  # numerator
   dem1 = 0 # first half of denominator
   dem2 = 0
   for (user, ratings) in userRatings.items():
      if band1 in ratings and band2 in ratings:
         avg = averages[user]
         num += (ratings[band1] - avg) * (ratings[band2] - avg)
         dem1 += (ratings[band1] - avg)**2
         dem2 += (ratings[band2] - avg)**2
   return num / (sqrt(dem1) * sqrt(dem2))
computeSimilarity("Kacey Musgraves", "Imagine Dragons", users3)
computeSimilarity("Kacey Musgraves", "Fall Out Boy", users3)

#5.预测David给"Kacey Musgraves"的评级结果：
#请参见“Python辅助PPT课件第3~4页”。


#发现贴吧水贴王：
import urllib2
from bs4 import BeautifulSoup
import csv
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

for k in range(0,100):
    req=urllib2.Request('http://tieba.baidu.com/f?kw=李毅&ie=utf-8&pn='+str(k*50))
    csvfile=file('tiezi.csv','ab+')
    writer=csv.writer(csvfile)
    #writer.writerow(['1','2','3','4'])
    response=urllib2.urlopen(req)
    the_page=response.read()
    soup=BeautifulSoup(the_page, "lxml")
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    for tag in soup.find_all(name="a", attrs={"class":re.compile("j_th_tit")}):
        list1.append("http://tieba.baidu.com"+tag['href'])
        list2.append(tag.string)

    for tag in soup.find_all(name="span", attrs={"class":re.compile("threadlist_rep_num.*")}):
        list3.append(tag.string)

    for tag in soup.find_all(name="span", attrs={"class":re.compile("tb_icon_author$")}):
        list4.append(tag['title'])

    for tag in soup.find_all(name="span", attrs={"class":re.compile("tb_icon_author$")}):
        list5.append(tag['title'])
    data=[]
    for i in range(0,len(soup.find_all(name="a", attrs={"class":re.compile("j_th_tit")}))):
        data.append((list1[i],list2[i],list3[i],list4[i]))
    writer.writerows(data)
    csvfile.close()
    print "第"+str(k)+"页完成"

from collections import Counter
list=[]
csvfile=file('tiezi.csv','rb')
reader=csv.reader(csvfile)
for line in reader:
    list.append(line[3])
csvfile.close()

dict=Counter(list)
list2=sorted(dict.iteritems(),key=lambda asd: asd[1], reverse=True)
for val in list2:
    print val[0], val[1]
