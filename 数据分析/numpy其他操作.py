# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-

## CSV文件：CSV是一种常见的文件格式，用来存储批量数据，存储一维，二维数据
'''
	一、写入数据文件
	np.savetxt(fname,array,fmt='%.18e',delimiter=None)

	frame : 文件、字符串或产生器,可以是.gz 或.bz2的压缩文件
	
	array : 存入文件的数组
	
	fmt : 写入文件的格式,例如：%d %.2f %.18e
	
	delimiter :分割字符串,默认是任何空格。 例如: a = np.arange(100).reshape(5,20)
	
	np.savetxt('a.csv',a,fmt='%d',delimiter=',')
	
	
	二、读取文件，加载文件
	np.loadtxt(fname,dtype=np.float,delimiter=None,unpack=False)
	
	frame : 文件、字符串或产生器,可以是.gz 或.bz2的压缩文件

	dtype : 数据类型,可选
	
	delimiter :分割字符串,默认是任何空格。
	
	unpack :读入数据写入一个数组 如果是True,读入属性将分别写入不同变量
	
'''

### 存储数据------------------- numpy pandas csv 存储数据（列表，字典）
# import numpy as np
# import pandas as pd
#
# s=np.arange(20).reshape(2,10)
# w=np.savetxt('s.csv',s,fmt='%d',delimiter=',')
# print(s)
#
# s=np.arange(30).reshape(5,6)
# df=pd.DataFrame(s,columns=['one','two','three','four','five','six'])
# df.to_excel('s1.xlsx',index=False)
# print('Done!')
#
#
# # 读取数据
# r=np.loadtxt('s.csv',delimiter=',')
# print(r)
#
# r=np.loadtxt('s.csv',delimiter=',',dtype=int)   ## 数据整型读取
# print(r)
#
#
# ## 多维数据读取：三维及以上
# '''
#     a.tofile(frame,sep='',format='%s')
#     frame:文件、字符串。
#     sep:数据分割字符串，如果是空串，写入文本时二进制，',':文本文件
#     format:写入数据的格式
# '''
# a=np.arange(100).reshape(5,10,2)
# a.tofile('a.dat',sep=',',format='%d')
# print('+++++')
#
# # 不写 sep=','  生成二进制文件
# a=np.arange(100).reshape(5,10,2)
# a.tofile('b.dat',format='%d')
#
# '''
# 	np.fromfile(frame,dtype=float,count=-1,sep='')
# 	frame:文件，字符串
# 	dtype:数据类型
# 	count；读入元素个数，-1表示读取整个文件
# 	sep:数据分割字符串，如果空串，写入二进制；',':文本文件
#
# '''
# ## np.fromefile():读取文本信息,与写入数据类型和数组维度保持一致
# a=np.fromfile('a.dat',dtype=int,sep=',').reshape(5,10,2)
# print(a)
#
# # 读取非文本文件
# a=np.fromfile('b.dat',dtype=int).reshape(5,10,2)
# print(a)
#
#
# # np.save(文件名(.npy)，数据) 和 np.load(文件名)
# a=np.arange(100).reshape(20,5)
# np.save('a1.npy',a)
#
# print(np.load('a1.npy'))
#
#
# ### 字符串存储----- np.savetxt
#
# s=['str','sgds','中国','sdg','美国','英国']
# a=np.reshape(s,(3,2))
# np.savetxt('ss.txt',a,fmt='%s',encoding='utf-8',delimiter=',')
#
# ## np.savetxt 保存字符串,列表名加在列表开始
# s=['one','two','three','four',"Name", "StudentFlag", "Job", "Company", "Location_result", "University_result", "Major", '班级', '学号', '语文成绩', '数学成绩', '英语成绩']
# a=np.reshape(s,(4,4))
# np.savetxt('s2.csv',a,fmt='%s',delimiter=',',encoding='utf-8-sig')
#
# ## pandas 保存，加列表名
# s=["Name", "StudentFlag", "Job", "Company", "Location_result", "University_result", "Major", '班级', '学号', '语文成绩', '数学成绩', '英语成绩']
# a=np.reshape(s,(3,4))
# df=pd.DataFrame(a,columns=['one','two','three','four'])
# df.to_excel('s3.xlsx',index=False)
#
#
# ## 添加列标名 header='string,string,....'
# s=["Name", "StudentFlag", "Job", "Company", "Location_result", "University_result", "Major", '班级', '学号', '语文成绩', '数学成绩', '英语成绩']
# a=np.reshape(s,(3,4))
# #columns=['one','two','three','four']
# np.savetxt('s233.csv',a,fmt='%s',delimiter=',',encoding='utf-8-sig',header='one,two,three,four')
#
#
# #### csv.writer()
# ## csv 模块：主要由两种方式存取csv文件：函数方法；类方法。
# '''
# 	一、函数方法（list方法）
# 	csv.reader(f [, dialect='excel'][optional kwargs]) ：返回csv阅读器（本质是一个迭代器，具有__next__()、__iter__()方法），可通过迭代读取	csv文件内容。f为打开csv文件的文件对象，实测文件应该用text模式（r或rt）打开。
#
# 	csv.writer(f [, dialect='excel'][optional kwargs]) #返回csv写入器，其可将序列对象（list等）写入到csv文件中，写入方法为writerow()、writerows()。f为被写入的csv文件对象，同样地，实测文件应该用text模式（w或wt）打开
#
# import csv
#
# l = []
# with open('test1.csv','rt') as f:
#    cr = csv.reader(f)
#    for row in cr:
#        print(row)
#        l.append(row) #将test.csv内容读入列表l，每行为其一个元素，元素也为list
# with open('1.csv','wt') as f2:
#    cw = csv.writer(f2)
#    #采用writerow()方法
#    for item in l:
#       cw.writerow(item) #将列表的每个元素写到csv文件的一行
#    #或采用writerows()方法
#    #cw.writerows(l) #将嵌套列表内容写入csv文件，每个外层元素为一行，每个内层元素为一个数据
# '''
# import csv
#
# ### 读取按行文件
# l=[]
# with open('s2.csv','r',encoding='utf-8') as f:
# 	csv_read=csv.reader(f)
# 	for line in csv_read:
# 		l.append(line)
# print(l)
#
#
# # ## 写入文件中
# ## 列表存储
#
# # 将列标在列表中
# s=['one', 'two', 'three', 'four',"Name", "StudentFlag", "Job", "Company", "Location_result", "University_result", "Major", '班级', '学号', '语文成绩', '数学成绩', '英语成绩']
#
# l=np.reshape(s,(4,4))
# with open('111.csv','w',encoding='utf-8-sig')as f:
# 	w=csv.writer(f,lineterminator = '\n')
# 	for line in l:
# 		w.writerow(line)
# print('Done!')
#
# # 注意：如果不在open()中加入 newline=''；或者 csv.writer()中加入
# #lineterminator = '\n'，会出现生成文件每行之间有空白行
#
#
# ## 单独设置列标
# s=["Name", "StudentFlag", "Job", "Company", "Location_result", "University_result", "Major", '班级', '学号', '语文成绩', '数学成绩', '英语成绩']
# col=['one', 'two', 'three', 'four']
# l=np.reshape(s,(3,4))
# with open('1113.csv','w',encoding='utf-8-sig')as f:
# 	w=csv.writer(f,lineterminator = '\n')
# 	w.writerow(col)   ## 写入列标
# 	for line in l:
# 		w.writerow(line)
# print('Done!')
#
#
# #### 字典存储  csv.DictWriter（）
# s=[{'actor':'Bob','money':123,'area':'China','money1':1233},{
# 	'actor':'Bob1','money':1231,'area':'China1','money1':12331},{
# 	'actor':'Bob12','money':12313,'area':'China13','money1':123313}]
# col = ['actor', 'money', 'area', 'money1']
# with open('1112.csv','w',encoding='utf-8-sig',newline='')as f:
# 	w=csv.DictWriter(f,fieldnames=[i for i in col]) # 遍历列标
# 	w.writeheader()   ## 写入列标
# 	for line in s:
# 		w.writerow(line)
# print('Done!')
#
# '''
# 		二、类方法（dict方法）
# 		csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds) #建立类字典方式的csv阅读器（迭代器）。f为打开csv文件的文件对象，同样地，实测文件应该用text模式（r或rt）打开。fieldnames（list等）为字典的key值（相当于列标题），每个key对应csv文件中的一列，如不指定，则默认读取的文件第一行元素为key。
# 		csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds) #建立类字典方式的csv写入器，具有writeheader()，writerrow(rowdict)，writerows(rowdicts)方法。f为文件类型对象，可为打开csv文件的文件对象（w或wt模式打开）。fieldnames（list等）为字典的key值（列标题），每个key对应csv文件中的一列，必须指定。
#
# 		l = []
# 		with open('test2.csv','rt') as f:
# 		   cr = csv.DictReader(f)
# 		   for row in cr:
# 			   print(row)
# 			   l.append(row) #将test2.csv内容读入列表l，每行为其一个元素，元素为dict
# 							 #key为标题（未指定时为读取的第一行），value为对应列的数据
#
# 		with open('2.csv','wt') as f2:
# 	   cw = csv.DictWriter(f2,fieldnames=['标题%d' % i for i in range(1,7)])
# 	   cw.writeheader() #将fieldnames写入标题行
# 	   #采用writerow()方法
# 	   for rowdict in l:
# 		  cw.writerow(rowdict) #将列表的每个元素（dict）按照对应的键值对写到csv文件的一行
# 	   #或采用writerows()方法
# 	   #cw.writerows(l) #将dict组成的list整体写入csv文件，每个dict为一行，每个value为一个数据
#
# '''

### 数组和列表的转化
import numpy as np
import pandas as pd

s=[1,2,3,4,5,6,'str','gg']
print(type(np.array(s)))   ## 数组
print(np.array(s),'\n')

a=[2,3,4,5]
print(np.array(a))           ## 列表---》数组
print(np.array(a).tolist())  ## 数组---》列表
print('*******')

s=[1,2,3,4,5,6,'str','gg']
l=[2,3,4,5,6,'sfd','ggh','ddd']
y=[34,45,5,6,7,'dg','dddg','gter']
print(np.array([s,l,y]))           ## 两个列表转化为数组


print('========= 转置 ========')
##### 数组转置
print(np.array([s,l,y]).T)         ## 数组转置

###### 数组取值
data=np.array([[[1,2],[3,4]],
				[[5,6],[7,8]]])
print(data.shape)
print(data[1,0,0])   ## 5
print(data[0,1,0])    # 3


print('======= transpose() ======')
### transpose()
'''
	三维数组的转置：
		创建的新数组 np.arry(x,y,z) x === 0 轴（宽）；y ==== 1 轴（高）； z === 2 轴（长）
						原索引(0,1,2)
		
		np.arry().transpose(0,2,1) : 转置的是索引，即 1,2 索引 ---》2,1索引 等价 高，长---》长，高
		0轴：二维数组个数，即一个三维数组
		1轴：二维数组的行数；
		2轴：二维数组的列数
		
		np.arange(12).reshape(2,3,2) ：由2个分别是3行，2列的二维数组组成的3维数组。
		
		### 数组个数，行列数的变化：
		eg1：（0,1,2）--》（0,2,1）
		 	  0轴不变，依然是两个2维数组。数量不变，均为 2
			  1轴变2轴 : 二维数组行列互换，一个二维数组是3行，2列，变化后应为2行，3列。每一个二维数组均适用该相同规律。
		
		eg2: (0,1,2) --> (2,0,1)
			 0轴变2轴：0轴：2个二维数组，2轴：2列    二维数组个数不变 均为 2
			 1轴变0轴：1轴：3行；0轴：2个数组        数组行数改变，3行变成2行
			 2轴变1轴：2轴：2列；1轴：3行            数组2列变成3列
		
		eg3: (0,1,2) --> (1,0,2)
			 0轴变1轴： 0轴数量是2； 1轴数量是3    二维数组个数由2变成3个
			 1轴变0轴： 1轴数量是3； 0轴数量是2    数组行数由3变成2
			 2轴不变：  列数量为2
		
		### 数组变化后数据的填充：
			np.arange(12).reshape(2,3,2) ：由2个分别是3行，2列的二维数组组成的3维数组。
			每一个数组变化规律均作用多个数组，数字填充有多个数组个数字组成
		
'''
s=np.arange(12).reshape(2,3,2)  ## 索引（0,1,2）
print(s)

print(s.transpose(1,0,2))
## 注：（0,1,2）--》（0,2,1） 0轴不变，即变化前后各有两个二维数组组成的一个三维数组，
## 1轴变2轴 : 二维数组行列互换，一个二维数组是3行，2列，变化后应为2行，3列


