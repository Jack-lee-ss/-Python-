# -*- coding: utf-8 -*-
## enumerate 对象使用for循环：计数值与元素值一起出现
a=['gadf',987,'+++%','实例化',8.9]
for i in enumerate(a):   # 单个变量，输出元组
	print(i)

for i,j in enumerate(a): # 输出计数值（默认0开始），元素值
	print(i,j)
	
for i ,j in enumerate(a,100): ## 计数值从100开始
	print(i,j)
print('==============')

## enumerate()在元组中使用
a=['gadf',987,'+++%','实例化',8.9]
b=enumerate(a)
print(tuple(b))      ## 将元组转化为 enumerate 对象

b=enumerate(a,90)
print(tuple(b))      ## 再转回元组对象

c=enumerate(a,20)
print(list(c))       ## 列表封装元组

d=enumerate(a,30)
print(dict(d))       ## 形成字典

e=enumerate(a)       ## 集合封装元组，无序
print(set(e))
print('====================')

### 一般情况下 集合{}   集合内不可以有列表，字典，集合
langs={'python','c','java','python',786,0.875,(0.9,'kgdg',999,'+++')}
print(langs,'\n')

## 空集合需要 set（）函数
a={}
print(type(a))
b=set()
print(type(b))

## set（）函数建立与字符串，字典，列表
x=set('python java')         ## 无序，不重复
print(x)

s=['apple','apple','banana']
x=set(s)                     ## 集合输出列表内容
print(x,'\n')

a=(98,'kjh',0.987)
s=set(a)
print(s)

b={1:'ghd','ab':0.98}
s=set(b)
print(s)   #### 打印字典键

## 通过集合删除列表内重复数据
l=[1,2,0.765,'jshg','apple','banab','apple']
s=set(l)
a=list(s)
print(l)
print(a)
print('================')

###### 集合操作
## 交集 &
a={1,2,3,4,5}
b={3,4,5,7,8}
ab=a.intersection(b)  ## 取交集
print(ab)
print(a&b,'\n')

## 并集 |
a={1,2,3,4,5}
b={3,4,5,7,8}
print(a.union(b))
print(a|b,'\n')

## 差集 -
a={1,2,3,4,5}
b={3,4,5,7,8}
print(a.difference(b))
print(a-b)
print(b.difference(a))
print(b-a,'\n')

## 对称差集 ^ :取除两个集合相同元素的剩余元素的集合
a={1,2,3,4,5}
b={3,4,5,7,8}
print(a^b)
print(a.symmetric_difference(b))
print((a-b)|(b-a))
print(a-b|b-a,'\n')

## 是否包含：in ； not in  返回布尔值
a=set('orange')
print('r'in a)

##### 集合方法
## isdisjoint():2个集合没有共同元素会返回 True
a={1,2,33,44,65}
b={3,4,5,7,8}
print(a.isdisjoint(b),'\n')

## issubset(): 如果一个集合是另一个集合的子集合，是则返回 True, 否则 返回 False
a={1,2,3,4,5}
b={1,2,3,4,5,7,8}
c={2,3,9}
print(a.issubset(b))
print(c.issubset(b),'\n')


#### 冻结集合 frozenset()
x=frozenset([1,3,5])
y=frozenset([5,7,9])
print(x)
print(y)
print(x&y)
print(x|y)
print('==============================')


#####  函数小案例---函数内修改列表内容，修改后，主程序列表也将永久修改结果
##  老乡鸡点餐
## pop()函数：返回删除的值
def kitchen(unserved,served):
	"""  将未服务的餐点转为已经服务"""
	print('厨房处理顾客所点的餐点')
	while unserved:
		current_meal=unserved.pop()
		# 模拟出餐过程
		print('菜单： ',current_meal)
		# 将已出的餐点转入已经服务列表
		served.append(current_meal)
def show_unserved_meal(unserved):
	""" 显示尚未服务的餐点 """
	print('==== 下列是尚未服务的餐点 ===')
	if not unserved:
		print('**** 没有餐点 ****','\n')
	for unserved_meal in unserved:
		print(unserved_meal)

def show_served_meal(served):
	""" 显示已经服务的餐点 """
	print('=== 下列是已经服务的餐点 ===')
	if not served:
		print("**** 没有餐点 **** ",'\n')
	for served_meal in served:
		print(served_meal)

unserved=['老乡鸡鸡汤','腊鸡腿','汉堡包鸡块','可乐']
served=[]

## 列出餐厅处理前的点餐内容
show_unserved_meal(unserved)
show_served_meal(served)

## 餐厅服务过程
kitchen(unserved,served)
print('\n',"=== 厨房处理结束 ===",'\n')

## 列出餐厅处理后的点餐内容
show_unserved_meal(unserved)
show_served_meal(served)
print('=======================')

### 匿名函数与其他函数混用
## filter:将后一个参数的内容传给前一个参数里运算
l=[5,10,15,20,25,30]
s=list(filter(lambda x:(x%2==1),l))
print('奇数列表： ',s)
print()

## 匿名函数与map()
l=[5,10,15,20,25,30]
s=list(map(lambda x:x**2,l))
print('奇数列表： ',s)
