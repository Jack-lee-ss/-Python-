# -*- coding: utf-8 -*-
## 多态：不同子类对象调用父类方法，产生不同结果
class Dog(object):
	def __init__(self,name):
		self.name=name
	
	def game(self):
		print('%s 蹦跳玩耍。。'% self.name)

class xiaotianquan(Dog):
	def game(self):
		print('%s 飞到天上去玩耍'%self.name)

class Person(object):
	def __init__(self,name):
		self.name=name
	
	def game_with_dog(self,dog):
		print('%s 和 %s 快乐的玩耍。。。'%(self.name,dog.name))
		dog.game()  ##

wangcai=Dog('旺财')
#wangcai=xiaotianquan('飞天旺财')
xiaoming=Person('小明')
xiaoming.game_with_dog(wangcai)

#####  类属性
class Tool(object):
	count=0
	def __init__(self,name):
		self.name=name
		Tool.count+=1  ## 让类属性值加一

# 创建工具对象
tool1=Tool('斧头')
tool2=Tool('榔头')
tool3=Tool('水桶')
tool4=Tool('飞刀')
tool4.count=45         ### 对象.类属性 不推荐
# 输出工具对象总数
#print(Tool.count)
print('类属性值：%d'% Tool.count)
print(tool4.count)