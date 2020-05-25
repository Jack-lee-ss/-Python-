# -*- coding: utf-8 -*-
 ### 参数扩展
 ## 参数设置默认参数
def f(name,age=0):
	print(f'name={name},age={age}')
f('老王',19)
f('小李')

def f(a,b,c=0,d=1):  ## 默认值只能从后向前设置
	print(f'{a},{b},{c},{d}')
f(1,2,4,6)  # 都有值的原样打印
f(1,2,3)    # 没有的用默认值填充
f(1,2)
print('==================')
## 关键词参数
def f(a,b=4,c=9):
	print(a,b,c,'\n')
f(12,c=6)  ## 关键词参数需要先将可以确定的值和参数对应。如果使用了关键词参数，后面都使用

l=[1,2,3,4]
def f(a):
	a.append(6)   ## a=l
	a=[8,7,9]
	a.append(34)
	print(a)      ## a 发生变化，l 不变
f(l)
print(l,'\n')


l=[1,2,3,4]
def f(a):
	a.append(6) ## a=l 实参和形参一致，没有给 a 赋值
f(l)
print(l)
print('----------------')
#### 可变参数 args 元组类型,可以指任意多个参数
def f(*args):
	print(args)
f(1,2,3)        ## 打印出元组


def sum(*args):   ## 不支持关键词赋值
	s=0
	for i in args:  ## 遍历 args 中数据
		s+=i
	return s
s=sum(1,2,4,6,7)  ## 求和
print(s)


def f(a,b,*args):  ## 只能在最后出现一个可变参数，
	print(a)
	print(b)
	print(args)   ## 元组类型
f('heii',1,5,8,0)


def f(a,b,*args,d,g):  ## 可变参数与其他值一起使用。
	print(a)
	print(b)
	print(args)   ## 元组类型
	print(d)      # 可变参数后可用关键词参数
	print(g)      # 同上
f('heii',1,5,8,0,d='g',g=99) ## 使用关键词参数
print('==================')

### 可变关键词参数 **kwargs
def f(**kwargs):
	print(kwargs,'\n')  ## 字典
	print(type(kwargs)) ## 字典类型
	for k,v in kwargs.items():
		print(f'{k}:{v}') # 遍历字典
f(a=1,b=3,c=9)

def f(a,b,c,**kwargs):  ## 只能出现在参数列表最后
	for k,v in kwargs.items():
		print(f'{k}:{v}','\n') # 遍历字典
f(1,3,x='hi',y='wo',c=9)


def f(a,b,c,*args,**kwargs):  ## 只能出现在参数列表最后
	print(args)
	print(a,b,c)
	for k,v in kwargs.items():
		print(f'{k}:{v}') # 遍历字典
f(1,3,4,99,'gbjk',x='hi',y='wo')
print()


## 元组解包
a,b,*c,d=(1,2,3,4,5,6)
print(a)
print(b)
print(c)
print(d)

a,b,*c,d=[1,2,3,4,5,6] ## 列表解包
print(a)
print(b)
print(c)
print(d)
print()

a,b,*c,d='123456' ## 解包为字符串
print(a)
print(b)
print(c)
print(d)
print()

a,b,*c,d=range(10)
print(a)
print(b)
print(c)
print(d)
print()

a,*b={'a':1,'b':2,'c':8} # 字典对键解包
print(a)
print(b)
print()

a,*b={'a':1,'b':2,'c':8}.values() # 字典对值解包
print(a)
print(b)
print()

a,*b={'a':1,'b':2,'c':8}.items() # 字典对键值解包 元组对象
print(a)
print(b)
print()

def f(*args):       ## 元组解包
	print(args)
l=[1,2,3,4,5,6]
f(*l)
print()

def f(**kwargs):       ## 字典解包
	print(kwargs)
l={'a':1,'g':'98'}
f(**l)
print()

###### 字典列表转化
## 方法一
list1=["a","b","c"]
list2=[1,2,3]
d={}
for i in range(len(list1)):
	d[list1[i]]=list2[i]
print(d,'\n')

## 方法二
list1=["a","b","c"]
list2=[1,2,3]
d=dict(zip(list1,list2))
print(d)
print('***************************')

### 列表，字符串转化
## 列表内容 --》字符串
l=['a','b','n','g']
s=''.join(l)
print(s)

## 列表中的值转化为字符串
l=['a',1,'b',3,'c',4]
s=[str(i) for i in l]
print(s,'\n')

## 列表数字转化为字符串
l=[1,2,3,4,5]
s=[str(i)for i in l]
print(s,'\n')

## 字符串转为列表
## eval() 字符串中有列表 ---》列表
s="['s','b','a']"
l=eval(s)
print(l,'\n')

s="{'a':1,'d':3,'g':99}"
l=eval(s)
print(l,'\n')

## 字符串每个字符转化为列表中的值
s='1234ghj'
l=list(s)
print(l,'\n')

## 嵌套列表转换为字典
l=[['a',1],['b',2],['c',3]]
s=dict(l)
print(s,'\n')

## 字典中键值转化为列表
d={'a':1,'d':3,'g':99}
print(list(d.keys()))
print(list(d.values()))
print()

### 含字符串，数字的列表转化为字符串
## 均转化为字符串，在将字符串连接

l1=['紫菜','神棍','gnk',9876]
s=[str(i)for i in l1]
s=''.join(s)
print(s,'\n')

## 列表合成字典
s1=['紫菜','神棍','gnk',9876,'987']
s2=['a','b','876',874,[1,2,3]]
s=dict(zip(s1,s2))
print(s)
print('++++++++++++++++++++++')

### 去除列表中空格符
## split():split方法中不带参数时，表示分割所有换行符、制表符、空格
## join()：连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串

s=[' ','','我们的 书包 是\xa0\u3000蓝色\u3000\u3000的']
for i in s:
	i=''.join(i).replace('\xa0','').replace('\u3000','').replace(' ','')
	print(i)

for i in s:
	i=''.join(i.split())
	print(i)
print()
print('===== 遍历列表会出现行与行之间的间隔,因为会将遍历的空格符打印出来，采用字符串操作=======')
print()
s=[' ','','我们的 书包 是\xa0\u3000蓝色\u3000\u3000的']
s=[str(i)for i in s]
s=''.join(s).strip()   ### 去列表中空字符串或者空白符
s=''.join(s.split())   ##  去除字符串中空格
print(s)
s=[str(i)for i in s]
s=''.join(s).strip()   ### 去列表中空字符串或者空白符
s=''.join(s.split())   ##  去除字符串中空格
print(s,'\n')

s=['我们的大中国啊,',  '0\u3000 9月27日\xa0发布.',' ','\u3000\u3000你好么!',123345 ]
## 列表转化为字符串
## 方法一：
a=[str(i) for i in s] ## 均转化为字符串
b=''.join(a)

b=list(b)             ## 字符串转列表
print(b)

s=''.join(b)          ## 合并列表中字符串
print(s)

s=''.join(s.split())  ## 去除字符串中空格
print(s)
print('===============================')

## 方法二
s=[' ','','我们的 书包 是\xa0\u3000蓝色\u3000\u3000的',' ','','我们的 书包 是\xa0\u3000蓝色\u3000\u3000的',986]

s=[str(i)for i in s]    ## 转字符串
a=''.join(s).strip()    ## 去除空格符并连接字符串
print(a)
b=''.join(a.split())    ## 去除字符串内空白符
print(b,'\n')

###  删除；列表中空格和空字符串
s=['据印度快报报道','','海外网/爱扎大 实习编译/林嘉敏',' ','未经授权严禁转载']
### 字符串整合成一行
a=''.join(s).strip()
print(a,'\n')

## 按字符串一行一行打印
s=[i for i in s if i!=' 'and i!='']
for i in s:
	print(i)

### 方法三：
s=[' ','','我们的 书包 是\xa0\u3000蓝色\u3000\u3000的',' ','','我们的 书包 是\xa0\u3000蓝色\u3000\u3000的',988]
s=[str(i) for i in s]
s=[i for i in s if i!=''and i!=' ']
s=''.join(s)
s=''.join(s.split())
print(s)

######### 斗鱼直播地址获取
import requests


def header():
	headers = {
		"Host": "playweb.douyucdn.cn",
		"Referer": "https://www.douyu.com/directory/myFollow",
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML: like Gecko) Chrome/68.0.3440.84 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded",
		"rid": "7032776",
		"time": "1582335104602",
		"auth": "55e455300a056206949e12459524e81b",
	}
	return headers


def get_addr(rid):
	ret = requests.post(
		"http://playweb.douyucdn.cn/lapi/live/hlsH5Preview/{}?rid={}&did=2dfd02149496030e407b1e3900031501"
			.format(rid, rid), headers=header())
	try:
		addr = "http://tx2play1.douyucdn.cn/" + ret.json()['data']['rtmp_live'].split("_")[0] + ".flv"
		return addr
	except:
		return ret.json()['msg']


print(get_addr(12313))  # 12313  312212