# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-

'''
## 列表的创建
a=[]
b=list()

c=[1,2,3]

print([i for i in range(1,11)])  # 表达式创建

print([i for i in range(1,10) if i % 2==0]) # 表达式+判断的列表

print(list('a,gb h'))    # 字符串转化为列表
print('==============')
a=[1,2,3,4,58,5]
# 列表分片：[左边界，右边界，步长]
print(a[1:])
print(a[2:4])
print(a[:-1])   # [1, 2, 3, 4, 58]
print(a[-3:-1]) # [4, 58]

print(a[2:4:2])  # 左边界>右边界  步长>0            [3]
print(a[2:0:-1]) # 左<右  步长<0   ，  否则输出[]  [3, 2] 截取下标为2的数据翻转取-1
print(a[3:0:-2]) # [4, 2]

print(a[4::-2])  # [58, 3, 1]
print(a[4::-1])  # [58, 4, 3, 2, 1]
print(a[4::-3])  # [58, 2]
print('-----')

print(a[::-1])   # [5, 58, 4, 3, 2, 1]
print(a[::-2])   # [5, 4, 2]

a=[1,4,7]
b=[22,44,66]
print(a+b)   ## 直接相加，不改变原列表
a.extend(b)  ## 直加，改变原列表
print(a)
print(3 in a) # 判断一个元素是否在一个列表中

a.insert(2,'str') # 将元素插入一个列表中
print(a)

print(a.count(2)) # 一个元素在列表找那个出现的次数

print(a.index(4)) # 元素在列表中下标位置

## sort() 改变原列表 和 sorted() 不改变原列表
list1=[2,1,4,7,3,55,77,5,1]
list1.sort(reverse=True)   ## reverse:是否为降序
print(list1) # [77, 55, 7, 5, 4, 3, 2, 1, 1]

l=[(1,2),(444,6),(33,44)]
l.sort(reverse=False)
print(l)   # [(1, 2), (33, 44), (444, 6)]

l.sort(key=lambda i:i[1],reverse=True)  ## 指定元组的第二个值来比较，降序排列
print(l)

print('+++++++++++++++++++++')

s=[(1,2),(444,6),(33,44)]
print(sorted(s))   # [(1, 2), (33, 44), (444, 6)]
print(s)

L = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
print(sorted(L,key=lambda x:x[1],reverse=True))  # key:比较一个数据大小

a = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
#   一行代码改成  [11, 1, 2, 3, 5]
# 将原列表去重按升序排列，由于11是两位数，其他为一位数，将每一个数转化为字符串形式，可以取[0],即可以取第一个数字的开头，由于11比其他数字多一位，所以排在第一位。
print(sorted(list(set(a))[::-1],key=lambda i:str(i)))
print(sorted(list(set(a))[::-1],key=lambda v: str(v)[0]))

b = [11, 21, 31, 111, 21, 51, 31, 21, 51, 31]
# [111,11,21,31,51]
print(sorted(list(set(b))[::-1],key=lambda v: str(v)[0]))
print(sorted(list(set(s)),key=lambda i:len(str(i)),reverse=True)) #根据字符串长度，降序排列
print('_____________')


num = [(1,2.5), (1.5, 3.2), (1.3, 4.0), (2.2, 1.8)]
y,z = max(num, key=lambda x:x[0])   ## 取元组第一个数字最大的那个
print(y, z)


num = [(1,2.5), (1.5, 3.2), (1.3, 4.0), (2.2, 1.8)]
y,z = max(num, key=lambda x:x[1])
print(y, z)

#### 按字符串长度排降序
myList = ['青海省','内蒙古自治区','西藏自治区','新疆维吾尔自治区','广西壮族自治区']
print(sorted(myList,key = lambda i:len(i),reverse=True))


## 取列表中字符串长度最大的元素
#  先将字符串按长度从大到小排，在取第一个即最大长度的元素
print(sorted(myList,key = lambda i:len(i),reverse=True)[0])

# 取列表中字符串长度最大的值的长度
print(max(len(str(i)) for i in myList))

# 取列表中字符串长度最大值的下标
print(myList.index(sorted(myList,key = lambda i:len(i),reverse=True)[0]))



## 字符串替换方法：将l中多个s[]字符串按照s列表中值的关系替换
# '1232s[0]er322rs[1]334ffews[2]dcnsdnfsks[3]334s[2]2sds'替换后为 	1232aer322rb334ffewcdcnsdnfskd334c2sds

import re
s=['a','b','c','d']
l='1232s[0]er322rs[1]334ffews[2]dcnsdnfsks[3]334s[2]2sds'
ab=re.findall(r'(s\[.*?])',l)
b=dict(zip(ab,s))
print(b)
for i ,j in b.items():
	w=l.replace(i,j)
	l=w
print(w)   # 1232aer322rb334ffewcdcnsdnfskd334c2sds

src="/docs/img/fea324aca2ed4416872749b8352a5412.jpg"
src="https://seaborn.apachecn.org/docs/img/fea324aca2ed4416872749b8352a5412.jpg"

python的bytes和str两种类型转换的函数encode()、decode()即可！

str通过encode()方法可以编码为指定的bytes；

反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法；

例：

str = 'this is test'

str = str.encode()



##  html文档的正则替换
import requests
import re

url="https://www.95kyh.com/shipin/list-%E5%9B%BD%E4%BA%A7%E7%B2%BE%E5%93%81.html"
headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

result=requests.get(url=url,headers=headers)

res=result.content.decode('utf-8')

f=re.sub(r'(<a href=")','<a href="https://www.95kyh.com',res)
print(f)


## 文档字符串的正则替换。
# 将一个文件中的地址加上域名，并且保存到新建的文件中
import os
import re
import json
os.chdir(r'D:\常用软件\Mysql安装合集')
with open('new.txt','w',encoding='utf-8') as fp:
	with open('html.txt','r',encoding='utf-8') as f:
		for line in f.readlines():
			if 'src':
				a=re.sub(r'src="(/)','src="https://seaborn.apachecn.org/',line)
				fp.write(a)


import urllib.request
from http import cookiejar
url = 'http://www.baidu.com/'
headers = {
	'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'
}

cookie = cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
resp = opener.open(url)

cookieStr = ''
for item in cookie:
	cookieStr = cookieStr + item.name + '=' + item.value + ';'

print(cookieStr)



import requests
from requests.cookies import RequestsCookieJar
from http import cookiejar
import urllib.request


url="https://accounts.douban.com/j/mobile/login/basic"
headers={

		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
		'Referer': 'https://accounts.douban.com/passport/login_popup?login_source=anony',
'Cookie': 'll="118196"; bid=pxZArVf-Vgc; __gads=ID=845d3fef94af27d9:T=1585569580:S=ALNI_Mb-0jh-4b934ko15RSUr7KFRSDUaw; _vwo_uuid_v2=DDA497BBC491E88E97D60DF03C7C9E86C|6cee2c5b01efce851b51130aae8ee61f; _pk_ref.100001.2fad=%5B%22%22%2C%22%22%2C1587287214%2C%22https%3A%2F%2Fmovie.douban.com%2F%22%5D; _pk_id.100001.2fad=883a1a37ba3e5106.1587287214.1.1587287214.1587287214.; viewed="34943818"; gr_user_id=a7a59f2c-5bfc-4f89-a7af-1c54300bb4fa; __utmc=30149280; apiKey=; __utma=30149280.1276462077.1585569765.1588395769.1588403462.9; __utmz=30149280.1588403462.9.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1588403462; login_start_time=1588403471950'
}

data={
		'ck':'',
		'name':17822222222,
		'password': 222222,
		'remember': 'false',
		'ticket':''
}

result=requests.post(url=url,headers=headers,data=data)
print(result.text)
'''

import time

## 字典的创建：
a={'k1':1,'k2':2}

b=dict(k1=1,k2=2)
b1=dict([('j',3)])    ## 创建一个字典

c={}
c['k1']=1
c['k2']=2

d=dict([('k1',1),('k2',2)])

e=dict(zip(['k1','k2'],[1,2]))

f=dict.fromkeys(['k1','k2'],234)    ## 多键对应相同值

g={x:x**2 for x in range(4)}

l=[]
s=[1,2,3,4,5,6]
for i in s:
	d={'num':i}
	l.append(d)
#print(l)       [{'num': 1}, {'num': 2}, {'num': 3}, {'num': 4}, {'num': 5}, {'num': 6}]


## in 检查 key是否存在
d1={'name':'python'}

if 'name' in d1:
	print(d1.get('name'))
print()

## get 获取字典中的值 取代 if.....else....

d1={'name':'python'}
print(d1.get('name'))
print(d1.get('name',22)) # 有对应键，输出对应值
print(d1.get('name1'))   # 无对应键，返回None
print(d1.get('name1',122)) # 无对应键，默认返回设定值


### 删除与替换字典的键值对
print('========== 删除与替换字典 ===========')

#### 删除
a = {"a":12,"b":3,"c":4}
a.pop("a")                 ## 删除单个字典的键，作用原数据
print(a)

f1=a.pop("d",98)           ## 如果key不存在，则可以设置返回值
print(f1)
print(a.pop("b"))          ## 返回删除值


b = {"a":12,"b":3,"c":4,'adf':222,'erer':'spogd','df':[234,5657]}  # 批量删除 a ,b 字典键值对
print(list(b)[2:4])        # ['c', 'adf']
[b.pop(i) for i in list(b)[2:4]]
print(b)         # 剩下 {'a': 12, 'b': 3, 'erer': 'spogd', 'df': [234, 5657]}


### 替换 单个键
print("============= 替换 ==============")
a = {"a":1}
a["b"]=a.pop("a")
print(a)     # {'b': 1}


### 批量替换字典键----------- 方法1
def f(count,a_1):
	return a_1[count]

def func(x):
	u = ['a1', 'b1', 'c1', 'd1']
	return u[count]

ab={"a":1,"b":2,"c":3,"d":4}
a_1=list(ab)
w={}
for count in range(len(ab)):
	w[func(count)]=ab.pop(f(count,a_1))
print(w)   # {'a1': 1, 'b1': 2, 'c1': 3, 'd1': 4} 批量替换字典键


###### 批量替换字典键 --------------- 方法2
def func(x):
	u = ['a1', 'b1', 'c1', 'd1']
	return u[count]
ab={"a":1,"b":2,"c":3,"d":4}
a_1=list(ab)
w={}
count=0
for i, j in ab.items():
	w[func(count)]=j
	count+=1
print(w)   # {'a1': 1, 'b1': 2, 'c1': 3, 'd1': 4} 批量替换字典键

## 批量换字典键 ------------------- 方法3
ab={"a":1,"b":2,"c":3,"d":4}
u = ['a1', 'b1', 'c1', 'd1']
v=list(ab.values())
print(dict(zip(u,v)))
# {'a1': 1, 'b1': 2, 'c1': 3, 'd1': 4}


### 批量替换字典值
def func(count):
	u = ['a1', 'b1', 'c1', 'd1']
	return u[count]

ab={"a":1,"b":2,"c":3,"d":4}
count=0
for i, j in ab.items():
	ab[i]=func(count)
	count+=1
print(ab)  # {'a': 'a1', 'b': 'b1', 'c': 'c1', 'd': 'd1'}

ab={"a":1,"b":2,"c":3,"d":4}
u = ['a1', 'b1', 'c1', 'd1']
k=list(ab.keys())
print(dict(zip(k,u)))
## {'a': 'a1', 'b': 'b1', 'c': 'c1', 'd': 'd1'}


## 字典中添加键值对
## 添加一对键值对
ab={"a":1,"b":2,"c":3,"d":4}
ab.setdefault('e',5)
print(ab)

## 添加多个字典
c={"f":6,"g":7,"j":8}
ab.update(c)
print(ab)
## {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'j': 8}

## setdefault 为 字典中不存在的key设置缺失值
'''
setdefault 的作用是：

如果 key 存在于字典中，那么直接返回对应的值，等效于 get 方法
如果 key 不存在字典中，则会用 setdefault 中的第二个参数作为该 key 的值，再返回该值。
'''
# 做分类统计时，希望把同一类型的数据归到字典中的某种类型中。
print('==============分类统计=================')
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 设置默认值，该key在dict中不存在，新增key-value对
print(cars.setdefault('PORSCHE', 9.2)) # 9.2          =========== 原字典中添加新的键值对
print(cars)
# 设置默认值，该key在dict中存在，不会修改dict内容
print(cars.setdefault('BMW', 3.4)) # 8.5
print(cars)


s=[{'actor':'Bob'},{'money':123},{'area':'China'},{'money1':1233},{'actor':'Bob1'},{'money':1231},{'area':'China1'},{'money1':12331}]
l={}
for x in s:
	for i,j in x.items():
		l.setdefault(i,[]).append(j)
print(l)

s1=[('actor','Bob'),('money',123),('area','China'),('money1',1233),('actor','Bob1'),('money',1231),('area','China1'),('money1',12331)]
n={}
for (i,j) in s1:
	n.setdefault(i,[]).append(j)
print(n)

s2=[['actor','Bob'],['money',123],['area','China'],['money1',1233],['actor','Bob1'],['money',1231],['area','China1'],['money1',12331]]
m={}
for [i,j] in s2:
	m.setdefault(i,[]).append(j)
print(m)

def func(x):
	s = [1, 2, 3, 4]
	return  [ i for i in s]

d1={'name':'python','adf':222,'erer':'spogd'}
v={}
for i,j in d1.items():
	v.setdefault(i,[i]).insert(0,func)
print(v)

d1={'name':'python','adf':222,'erer':'spogd','df':[234,5657]}
v={}
for i,j in d1.items():
	v.setdefault(i,[j,i]).remove(j)   # 删除[j,i] 中的 j 值
print(v)

d1={'name':'python','adf':222,'erer':'spogd','df':[234,5657]}
v={}
for i,j in d1.items():
	v.setdefault(i,[]).extend(i)  # 删除[j,i] 中的 i 值
print(v)

d1={'name':'python','adf':222,'erer':'spogd','df':[234,5657]}
v={}
for i,j in d1.items():
	v.setdefault(i,[]).append(i)  # 删除[j,i] 中的 i 值
print(v)

print('==================')

### append() 和 extend() 区别：
##  作用在列表的区别：
# list.append(object) 向列表中添加一个对象object
# list.extend(sequence) 把一个序列seq的内容添加到列表中
music_media = ['compact disc', '8-track tape', 'long playing record']
new_media = ['DVD Audio disc', 'Super Audio CD']
music_media.append(new_media)                         # 整体添加
print(music_media)

music_media1 = ['compact disc', '8-track tape', 'long playing record']
new_media1 = ['DVD Audio disc', 'Super Audio CD']
music_media1.extend(new_media1)                       # 按部分添加
print(music_media1)

## 作用在字符串的区别：
# append() 无法作用字符串中

P = ['abc', 'jack']
P.extend([12,34,-0.834])                    # 迭代整数可以放置于列表中
P.extend({'key':345})                # 迭代一个字典的Key
P.extend('666')                      # 可迭代对象：字符串
P.extend(['anna', 18,[12,34]])               # 可迭代对象：列表
P.extend({'alice': 19, 'even': 22})  # 可迭代对象：字典（默认key）
P.extend(list({'alice': 19, 'even': 22}.values()))  ## 可以迭代字典的值 values
P.extend(list({'alice': 19, 'even': 22}.items()))   ## ('alice', 19), ('even', 22)
print("New list：", P,'\n')

num = [1,2]
print('将1迭代2次')
num.extend([1]*2)     # [1, 2, 1, 1]
print(num)
print('将2迭代3次')
num.extend([2] * 3)   # [1, 2, 1, 1, 2, 2, 2]
print(num)
num1 = [4,5]
num.extend(num1*3) #num1的元素挨个添加到num中
print(num)
print('===========')


p = ['abc', 'jack']
p.append('stre')
p.append(123)
p.append([23,'srt'])
p.append((23,'sr'))
p.append({'fg':345,'ghj':'ert'})
p.append(list({'fg':345,'ghj':'ert'}))  ## 默认字典Key,以列表形式添加
p.append(list({'fg':345,'ghj':'ert'}.values())) ## 以列表形式添加字典值
p.append(list({'fg':345,'ghj':'ert'}.items()))  ## 以列表形式添加字典键值对的元组
p.append(list({'fg':345,'ghj':'ert'}.items())[1])
print(p)



### python中list使用append()添加dict，值被覆盖问题:
## python变量内存分配问题。python中的对象之间赋值时是按引用传递的。字典被append给列表的是一个地址,当字典声明在循环外的时候,字典始终是第一次声明的那一个,就算一直在追加值,也只不过是将新的值覆盖掉原来的值而已;当字典声明在循环内时,每次循环都会生成一个新的字典,每次的值也就相应的保存在了新的字典内.

d = {'id': None}       # 字典在循环外，新值会覆盖旧值
l = []
for i in range(1, 4):
	d['id'] = i
	l.append(d)
print(l)               # [{'id': 3}, {'id': 3}, {'id': 3}]

l=[]
for i in range(1,4):
	d={'id':None}     # 字典放置循环内部
	d['id']=i
	l.append(d)
print(l)              # [{'id': 1}, {'id': 2}, {'id': 3}]

l=[]
s=[1,2,3,4,5,6]
for i in s:
	d={'num':i}
	l.append(d)
print(l)

print('++++++++++++++++++++')

def func(i):
	s = [1, 2, 3]
	return s[i]
l={}
d1 = {'name': 'python', 'adf': 222, 'erer': 'spogd'}
count=0
for i,j in d1.items():
	l.setdefault(i,[i,j]).insert(0,func(count)) ## 依次插入不同值
	count+=1
print(l)
#{'name': [1, 'name', 'python'], 'adf': [2, 'adf', 222], 'erer': [3, 'erer', 'spogd']}


def func(i):
	s = [1, 2, 3]
	return s[i]
l={}
s=[1,2,3]
d1 = {'name': 'python', 'adf': 222, 'erer': 'spogd'}
count=0
for i,j in d1.items():
	l.setdefault(i,[j]).append(func(count)) # 列表中依次增加不同值
	count+=1
print(l)  # {'name': ['python', 1], 'adf': [222, 2], 'erer': ['spogd', 3]}


###  fromkeys()函数 用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值

seq = ('Google', 'Runoob', 'Taobao')
dict = dict.fromkeys(seq)           ## 未设置字典值
print("新字典为 : %s" % str(dict))

dict = dict.fromkeys(seq, 10)
print("新字典为 : %s" %  str(dict))


seq1 = ('Google', 'Runoob', 'Taobao')
dict = dict.fromkeys(seq1,[10,20,30])
print("新字典为 : %s" %  str(dict))


seq2 = ['Google', 'Runoob', 'Taobao']
dict = dict.fromkeys(seq2,{})            ## 值设为空字典
print("新字典为 : %s" %  str(dict))


#### 用字典实现 switch ... case 语句    字典隐射

data={
	0:'zero',
	1:'one',
	2:'two',
	3:'three',
	4:'four'
}
datas=[0,3,4]
print([data[i] for i in datas])
print(data.get(i,'nothing') for i in datas)  ## 取列表元素，得到对应字典值


### 字典推导式
my_dict = {i: i * i for i in range(10)}
print(my_dict)