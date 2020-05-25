# -*- coding: utf-8 -*-
"""
def 函数名():
	xxx
定义一个类名方式：
Class 类名：
	xxxxxx
类名：规则 大驼峰

给一个对象添加属性方法为：
对象名.新的属性名=值

获取这个对象的属性，2中方法：
1，对象.属性
2. 定义一个方法，使用self.属性

"""

## 定义一个猫类：
class Cat:
	# 属性
	# 方法①: __init__(self) 当创建完一个对象后，立马调用。
	def __init__(self,ab,cb,cf):
		self.a=ab   # 添加创建对象（猫对象）调用的属性，下同
		self.b=cb
		self.c=cf
		print('hahhaha')

	# 方法②: 自定义方法
	def eat(self):
		print('======吃=========')
	def drink(self,a,b):
		print('======喝=========')
		print('----ab=%d,cb=%d----'%(a,b))
	def hight(self):
		print(self.hight)
	
## 创建一个猫对象
# 对象添加属性值（一一对应），默认在__init__
a=Cat('color',4,'hight') # 创建对象，添加需要调用的属性，将会自动默认调用在 __init__ 中
# 对象的方法添加属性。要在属性中传入参数
a.eat() # 让对象调用方法
a.drink(11,22) # 传入属性值

## 对象.属性
a.weiba='有'

## 定义一个方法，使用self.属性
print(a.weiba)
a.hight()

## 定义汽车类
class Car:
	def __init__(self):
		self.a=4        # 自定义添加属性，上个例子中是调用属性
		self.b='蓝色'	# 自定义添加属性，上个例子中是调用属性
	def move(self):
		print('车在跑，目标')
## 创建对象
BWM=Car()
BWM.move()
print('车的颜色：%s'%BWM.b)
print('车的大小：%s'%BWM.a)

## 定义颜色类：换颜色
class Color:
	def __init__(self,color): # 先调用 __init__ 内容。__init__ 方法：创建对象后就执行。
		self.color=color
		print(self.color)
	def changColor(self,newColor): # 在调用 自定义方法
		self.color=newColor
		print(self.color)
a=Color('白') # 传入参数
a.changColor('黑') # 传入参数
print('========================','\n')

## self 含义：（对象自己，也指被赋给的变量）
class Color:
	def __init__(self,color): # 先调用 __init__ 内容。__init__ 方法：创建对象后就执行。
		self.color=color
		print(self.color)
		
	def changColor(self,newColor): # 在调用 自定义方法
		self.color=newColor
		print(self.color)
		
	def newColor(self):
		print('颜色：%s'%self.color)
		
	def color(self):
		print('light')
		
	def __str__(self):      ## 让 print()打印结果更好一点
		return "当前对象颜色为："+self.color
		
def text1():
	a.newColor()
	
def text2():
	a.newColor()

def text3():
	b.changColor('黄')

def text4():
	b.color()
	
a=Color('白') # 首先传入参数，相当于初始化数据
a.changColor('黑') # 改变参数，改变数据a.color(a)

a.newColor() # 该处不写参数，实际传入 a ,相当 a=self，打印出改变后的参数，黑

b=Color('蓝') # 另创建一个对象，初始化对象数据，a 和 b不同对象。

text1() # 自定义函数调用对象，text1（）在调用 a.newColor()函数，打印出 黑

text2() # 自定义函数调用对象，text2（）在调用 a.newColor()函数，打印出 黑

text3() # 自定义函数调用对象，text3() 调用 b.changcolor()函数，改变参数，黄

print(id(a))
print(a)
print('===================','\n')

### -----------------烤地瓜实例-------------------
class SweetPotato:
	def __init__(self):          # 初始化数据
		self.cookedLevel=0
		self.cookedString='生的'
		self.condiments=[]       # 添加配料
		
	def __str__(self):           # 打印规范化
		
		msg="地瓜生熟程度:"+self.cookedString
		msg+='; '+'等级为:'+str(self.cookedLevel)
		if len(self.condiments)>0:
			msg+=";  作料为："
			for temp in self.condiments:
				msg+= temp +','
			msg=msg[:-1]   ## 句尾去符号：方法二：msg=msg.strip(',')
		else:
			msg+='; 暂未添加作料'
		return msg
	
	# 烤地瓜方法
	def cook(self,times):
		self.cookedLevel+=times
		if self.cookedLevel>8:
			self.cookedString="焦了"
		elif self.cookedLevel>5:
			self.cookedString='熟了'
		elif self.cookedLevel>3:
			self.cookedString='半生不熟'
		else:
			self.cookedString='生的'
	# 添加作料
	def addcondiments(self,temp):
		self.condiments.append(temp)
			
diGua=SweetPotato()
print(diGua)

diGua.cook(1)  ## 传入时间参数
diGua.addcondiments('芥末酱')
print(diGua)

diGua.cook(3)
diGua.addcondiments('苹果酱')
print(diGua)

diGua.cook(4)
diGua.addcondiments('孜然')
print(diGua)

diGua.cook(9)
diGua.addcondiments('酱油')
print(diGua)


####### 存放家具实例