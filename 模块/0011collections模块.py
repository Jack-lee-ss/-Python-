# -*- coding: utf-8 -*-
from collections import namedtuple, deque, OrderedDict, defaultdict, Counter  # 具名元组,双端队列
def main():
	point=namedtuple('point',['x','y'])
	p1=point(1,2)
	p2=point(3,5)
	print(p1,p2)
	print(p2.x)
	
	Card=namedtuple('card',['suit','num'])
	c1=Card('红桃',5)
	print(c1)
	print(c1.num)
	
	dq=deque([1,2])
	dq.append('a')  # 从后面放入数据
	print(dq)
	
	dq.appendleft('b') # 从前面放入数据
	print(dq)
	
	dq.insert(5,'h') # 在前面字符后添加一个字符
	print(dq)
	
	print(dq.pop()) # 从后面获取数据          删除插入影响效率
	print(dq.popleft()) # 从前面获取数据
	print(dq) # 返回Pop 后的数据
	
	
	d=dict([('a',1),('b',2),('c',3)])  ## 无序字典
	print(d)
	
	od=OrderedDict([('a',1),('b',2),('c',3)])  ## 有序字典
	print(od)
	print(od['b'])
	for i in od:          ## 遍历字典，得到键
		print(i)
		
	
	values=[11,33,55,77,88,99,100]   ## 将列表元素分类成字典
	my_dict=defaultdict(list)        ## 默认可以调用的类型，然后分成字典形式
	for value in values:
		if value> 50:
			my_dict['k1'].append(value)  ## 返回字典键对应值
		else:
			my_dict['k2'].append(value)
	print(my_dict)
	
	my_dict=defaultdict(lambda :7) ## 一般默认不能是数字，或者字符串，因为无法调用，所以用匿名函数返回
	print(my_dict['k'])            ## 返回字典键对应的值
	my_dict=defaultdict(lambda :'gndf')
	print(my_dict['444'])
	
	c=Counter('afdgghhfsadfh') ## 输出一个字符串中元素的个数，并以字典形式表示
	print(c)
	

if __name__ == '__main__':
	main()