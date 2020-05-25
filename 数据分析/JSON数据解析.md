================================  pandas处理json数据 ================================
将json串解析为DataFrame的方式主要有三种：
	利用pandas自带的read_json直接解析字符串
	利用json的loads和pandas的json_normalize进行解析
	利用json的loads和pandas的DataFrame直接构造(这个过程需要手动修改loads得到的字典格式)

一、pandas.read_json()函数的参数如下：简单数据的处理

	path_or_buf=None: json文件的路径
	orient=None:这个参数有多种选择状态，orient的设置有以下几个值：
	(1).'split'：字典形式，有索引，有列字段,和数据矩阵构成的json格式。key名称只能是index,columns和data。
	s='{"index":[1,2,3],"columns":["a","b"],"data":[[1,3],[2,8],[3,9]]}'
	print(pd.read_json(s,orient='split'))
	   a  b
	1  1  3
	2  2  8
	3  3  9
	(2).'records'：多个字典构成的列表，构成是列字段为键,值为键值,每一个字典成员就构成了dataframe的一行数据。
	s='[{"name":"xiaomaimiao","age":20},{"name":"xxt","age":18},{"name":"xmm","age":1}]'
	print(pd.read_json(s,orient='columns'))
			  name  age
	0  xiaomaimiao   20
	1          xxt   18
	2          xmm    1
	
	(3). 'index': 以索引为key,以列字段构成的字典为键值
	i='{"city":{"guangzhou":"20","zhuhai":"20"},"home":{"price":"5W","data":"10"}}'
	df=pd.read_json(i,orient='index')  # 行索引是 key
	df1=pd.read_json(i,orient='columns')  ## 列索引是 key 同 orient='records'
	print(df)
			data  	guangzhou 	price  zhuhai
	city   	NaN       20.0   	NaN    20.0
	home  	10.0       NaN    	5W     NaN
	--------------------
	print(df1)
				city home
	guangzhou  20.0  NaN
	zhuhai     20.0  NaN
	price       NaN   5W
	data        NaN   10
	--------------------
		
	i='{"city":["guangzhou","20","zhuhai","20"],"home":["price","5W","data","10"]}'
	print(pd.read_json(i,orient='columns'))
			city   home
	0  guangzhou  price
	1         20     5W
	2     zhuhai   data
	3         20     10
	-----------------------
	print(pd.read_json(i,orient='index'))
				0    1       2   3
	city  guangzhou  20  zhuhai  20
	home      price  5W    data  10

	(4). 较复杂数据解析：
	data = [{'id': 1, 'name': {'first': 'Coleen', 'last': 'Volk'}},
              {'name': {'given': 'Mose', 'family': 'Regner'}},
              {'id': 2, 'name': 'Faye Raker'}]

	print(pd.read_json(json.dumps(data),orient='columns'))
		id                                   name
	0  1.0    {'first': 'Coleen', 'last': 'Volk'}
	1  NaN  {'given': 'Mose', 'family': 'Regner'}
	2  2.0                             Faye Raker
	
	(5).复杂数据
	pd.set_option('display.max_rows',500)
	pd.set_option('display.max_columns',500)
	pd.set_option('display.width',1000)
	data = [{'state': 'Florida',
               'shortname': 'FL',
               'info': {
                    'governor': 'Rick Scott',
					'area':'China',
               },
               'counties': [{'name': 'Dade', 'population': 12345},
                           {'name': 'Broward', 'population': 40000},
                           {'name': 'Palm Beach', 'population': 60000}]},
			{'state': 'Ohio',
               'shortname': 'OH',
               'info': {
                    'governor': 'John Kasich',
					'area':'English',
               },
               'counties': [{'name': 'Summit', 'population': 1234},
                            {'name': 'Cuyahoga', 'population': 1337}]}
			]

	print(pd.read_json(json.dumps(data),orient='columns')) # 将列表变成json数据


	(6). 'values'嵌套的列表。里面的成员也是列表，2层的
	s='[["1",2,3],["str",[6,9]]]'
	print(pd.read_json(s,orient='value'))
		 0       1    2
	0    1       2  3.0
	1  str  [6, 9]  NaN
	
=============================================================

二、 json_normalize(): 复杂数据的处理，导入：from pandas.io.json import 			
	 json_normalize:对字符串进行解析，得到DataFrame格式，以便于存储于Excel中
	 格式：json_normalize(源文件，键名....)
	 1，先解析复杂标签，即带有列表的键，可以得到内部复杂数据；
	 2，在解析同级键名，即不带字典内容的键，用列表括住；
	 3，最后解析带字典内容的键名，至于最内层。需要用列表分开，字典键+值作为一个列表。
	data = [{'state': 'Florida',
               'shortname': 'FL',
               'info': {
                    'governor': 'Rick Scott',
					'area':'China',
               },
               'counties': [{'name': 'Dade', 'population': 12345},
                           {'name': 'Broward', 'population': 40000},
                           {'name': 'Palm Beach', 'population': 60000}]},
			{'state': 'Ohio',
               'shortname': 'OH',
               'info': {
                    'governor': 'John Kasich',
					'area':'English',
               },
               'counties': [{'name': 'Summit', 'population': 1234},
                            {'name': 'Cuyahoga', 'population': 1337}]}
	]
					源文件 含列表的键    同级键  同级键     含字典的键 对应值  
	print(json_normalize(data,'counties',['state','shortname',['info','governor'],['info', 'area']]))
		     name  population    state shortname info.governor info.area
	0        Dade       12345  Florida        FL    Rick Scott     China
	1     Broward       40000  Florida        FL    Rick Scott     China
	2  Palm Beach       60000  Florida        FL    Rick Scott     China
	3      Summit        1234     Ohio        OH   John Kasich   English
	4    Cuyahoga        1337     Ohio        OH   John Kasich   English
	
	
	s=[
		{
			"writer": "mark Ross",
			"nationality": "USA",
			"books": [
			{
				"title": "XML Cookbook",
				"price": 23.56
			},
			{
				"title": "Python Fundamentals",
				"price": 50.7
			},
			{
				"title": "The Numpy library",
				"price": 12.3
			}
					]
		},
		{
		"writer": "Barbara Bracket",
		"nationality": "UK",
		"books": [
			{
				"title": "Java Enterprise",
				"price": 28.6
			},
			{
				"title": "HTML5",
				"price": 31.35
			},
			{
				"title": "Python for Dummies",
				"price": 28.0
			}
				]
		}
	  ]
				   源文件   含列表的键    同级键    同级键
	print(json_normalize(s,'books',["writer","nationality"]))
	
	## 特殊json数据格式
	json1=[{"events": [{"schedule": {"date": "2015-08-27",
		 "location": {"building": "BDC", "floor": 5},
		 "ID": 815},
		"group": "A"},
	   {"schedule": {"date": "2015-08-27",
		 "location": {"building": "BDC", "floor": 5},
	 "ID": 816},
	"group": "A"}]}]
	
	f=json_normalize(json1[0]["events"])
	print(f)
		group schedule.date schedule.location.building  schedule.location.floor  schedule.ID
	0     A    2015-08-27                        BDC                        5          815
	1     A    2015-08-27                        BDC                        5          816
	---------------------------------------
	# 转置
	print(f.unstack())
		group                       0         A
								1             A
	schedule.date               0    2015-08-27
								1    2015-08-27
	schedule.location.building  0           BDC
								1           BDC
	schedule.location.floor     0             5
								1             5
	schedule.ID                 0           815
								1           816
	dtype: object

	
	
三、 手动解析与保存Excel：
	  对于复杂的json数据，不同列表，字典嵌套以及缺失值的存在，需要具体情况具体分析
	  步骤：
			先 json_normalize():分清数据缺失部分，含字典或者列表部分，需要单独处理部分。
			将数据转化为字符串格式，json.loads()将数据转化为字符串，
			遍历列表或字典，将获取的数据存放于新列表中，构成DataFrame()的数值，
			构建DataFrame()，设定columns()值，并且保存Excel中
	
	
	'''
		### zip()函数:
		用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
		s=[0, '思维齐', '软件开发', '北京全民星彩科技有限公司']
		w=[0, 'XCHaa', '数据分析师', '百融金融信息服务有限公司']
		a=[1,2,3,4]
		print(zip(s,w,a))
		<zip object at 0x000001FFABE379C8>

		print(tuple(zip(s,w,a)))
		((0, 0, 1), ('思维齐', 'XCHaa', 2), ('软件开发', '数据分析师', 3), ('北京全民星彩科技有限公司', '百融金融信息服务有限公司', 4))

		print(list(zip(s,w,a)))
		[(0, 0, 1), ('思维齐', 'XCHaa', 2), ('软件开发', '数据分析师', 3), ('北京全民星彩科技有限公司', '百融金融信息服务有限公司', 4)]

		for s1,w1,a1 in zip(s,w,a):
			print(s1,w1,a1)
				0 0 1
			思维齐 XCHaa 2
			软件开发 数据分析师 3
			北京全民星彩科技有限公司 百融金融信息服务有限公司 4
			
			
		for s1,w1,a1 in list(zip(s,w,a)):
			print(s1,w1,a1)
				0 0 1
			思维齐 XCHaa 2
			软件开发 数据分析师 3
			北京全民星彩科技有限公司 百融金融信息服务有限公司 4
			
		s=[[0,'思维齐'], ['软件开发','北京全民星彩科技有限公司']]
		w=[[0, 'XCHaa'], ['数据分析师','百融金融信息服务有限公司']]
		a=[[1,2],[3,4]]
		for s1,w1,a1 in list(zip(s,w,a)):
			print(s1,w1,a1)
	[0, '思维齐'] [0, 'XCHaa'] [1, 2]
	['软件开发', '北京全民星彩科技有限公司'] ['数据分析师', '百融金融信息服务有限公司'] [3, 4]
	
	'''
	
		实例：
		import json
		import numpy as np
		import pandas as pd
		import os
		os.chdir(r'F:\python代码\数据分析\统计与计数')
		# open().read():读取文件，解析文件。pd.read_json():只能读取一级文件，无法解析复杂数据
		fp=open(r'ne123.txt',encoding='utf-8').read()
		print(type(fp))  # 字符串格式
		# 转化为列表
		df=json.loads(fp)
		print(type(df))
		
		'''
			两个函数式与文件是否 .json 格式无关。
			json.dumps():字典,列表转化为字符串
			json.loads():字符串转化为字典,列表
		'''
		# 遍历列表内容，将列表中字典键对应值提取并且存放于列表中
		# data_s_all：遍历存放是源文件中没缺失值的数据，一起存放
		# data_Location_all data_University_all data_MajorTag_all 含有缺失值
		data_s_all=[[d["StudentFlag"], d["Name"],d["Avatar"],d["Job"],d["Company"]] for d in df]
		data_Location_all = [d["Location"] for d in df]
		data_University_all = [d["University"] for d in df]
		data_MajorTag_all = [d["MajorTag"] for d in df]
		# 设置空列表，构造DataFrame()的数值。
		col_data=[]
		# zip():返回是各个列表聚合的，for i,j in list(zip(a,b)): 遍历列表中
		for data_s,data_University,data_Location,data_MajorTag in list(zip(data_s_all,data_University_all,data_Location_all,data_MajorTag_all)):
			## 分别遍历处列表中第几个数据
			StudentFlag = data_s[0]
			Name = data_s[1]
			Avatar=data_s[2]
			Job = data_s[3]
			Company = data_s[4]
			# 由于有的数据没有值，所以先将以下三个标签的值设为空值
			Location_result=''         
			University_result=''
			Major=''
			
			# try:用于捕获缺失值：
			try: 
				# 判断字典中是否存在第一个子标签
				if 'L1' in data_Location:
					s=[]
					# 记录字典长度,获取子标签个数
					lens=len(data_Location) # 记录字典长度
					# 获取每个子标签的值
					for i in range(lens):
						if i==lens-1:
							data=str(data_Location).split(',')[i].split(':')[1].replace("'",'').replace("}",'')

						else:
							data = str(data_Location).split(',')[i].split(':')[1].replace("'", '').replace("'", '')
						# 合并字符串
						s.append(data)
					# 列表转字符串
					Location_result=''.join(s)
			# 出现缺失值补None
			except Exception as e:
				None

			try:
				if 'Country' in data_University:
					s = []
					lens = len(data_University)  # 记录字典长度
					for i in range(lens):
						if i == lens - 1:
							data = str(data_University).split(',')[i].split(':')[1].replace("'", '').replace("}", '')
						else:
							data = str(data_University).split(',')[i].split(':')[1].replace("'", '').replace("'", '')
						s.append(data)
					University_result = ''.join(s)
			except Exception as e:
				None

			try:
				if 'Major' in data_MajorTag:
					s = []
					lens = len(data_MajorTag)  # 记录字典长度
					for i in range(lens):
						if i == lens - 1:
							data = str(data_MajorTag).split(',')[i].split(':')[1].replace("'", '').replace("}", '')
						else:
							data = str(data_MajorTag).split(',')[i].split(':')[1].replace("'", '').replace("'", '')
						s.append(data)
					Major = ''.join(s)
			except Exception as e:
				None
			## 将遍历的值至于列表中，在添加到col_data列表中，每一个列表代表DataFrame一行数据
			col_data.append([StudentFlag,Name,Avatar, Job, Company,  Location_result, University_result, Major])
		## 将所有总列表作为值构成DataFrame的值，根据值，补上列标签	
		f=pd.DataFrame(col_data,columns=['StudentFlag','Name','Avatar', 'Job', 'Company',  'Location_result', 'University_result', 'Major'])
		print(f.head())
		# 保存至Excel中
		f.to_excel('123excel.xlsx')  
		
		
		## 对于存储在Excel中一些数据聚集在一格的处理方法：一行变多行 Location_result
			Job		Company		Location_result
		soyotec		总经理	 	北京 北京市 
		White T		 			天津 天津市 
		
		## 读取数据
		os.chdir(r'F:\python代码\数据分析\统计与计数')
		df=pd.read_excel('excel_pd2.xlsx',encoding='utf-8')
		# 对该数据 Location_result 部分字符串处理，去空间，分割
		df['new']=df['Location_result'].str.strip().str.split(' ')
		# 一行变多行
		d=df.explode('new')
		print(d)
			 Unnamed: 0                                 Name  ...       Major          new
		0           0  //cdn.kesci.com/images/avatar/4.jpg  ...         NaN            北京
		0           0  //cdn.kesci.com/images/avatar/4.jpg  ...         NaN            北京市
		1           1  //cdn.kesci.com/images/avatar/1.jpg  ...   光电信息科学与工程  天津
		1           1  //cdn.kesci.com/images/avatar/1.jpg  ...   光电信息科学与工程  天津市


+++++++++++++++++ pandas 获取 html()网站表格数据 ++++++++++++++++++++++++++
import pandas as pd
import csv
'''
	在写入csv文件中，出现了乱码的问题-------utf-8 改为utf-8-sig
   ”utf-8“ 是以字节为编码单元,它的字节顺序在所有系统中都是一样的,没有字节序问题,因此它不需要BOM,所以当用"utf-8"编码方式读取带有BOM的文件时,它会把BOM当做是文件内容来处理, 也就会发生乱码的错误.
   “uft-8-sig"中sig全拼为 signature 也就是"带有签名的utf-8”, 因此"utf-8-sig"读取带有BOM的"utf-8文件时"会把BOM单独处理,与文本内容隔离开,也是我们期望的结果.
'''
url='https://www.aqistudy.cn/'
## 观察需要的表数据在该网页的第几个，数组计数
tb=pd.read_html(url)[0]
tb.to_csv(r'31.csv', mode='a', encoding='utf_8_sig', header=1, index=0)


<img src="https://seaborn.apachecn.org/docs/img/edfd168858231883b7e55e685f2f4e0d.jpg" data-origin="img/edfd168858231883b7e55e685f2f4e0d.jpg" alt="http://seaborn.pydata.org/_images/introduction_1_0.png">


https://seaborn.apachecn.org/docs/img/edfd168858231883b7e55e685f2f4e0d.jpg















