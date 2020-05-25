 =========================== Pandas数据分析系列 ================================
一、什么是Pandas?
	一个开源的Python类库：用于数据分析、数据处理、数据可视化

	高性能
	容易使用的数据结构
	容易使用的数据分析工具
	很方便和其它类库一起使用：

	numpy：用于数学计算
	scikit-learn：用于机器学习

二、Pandas数据结构
	1 Series:一种类似数组的对象，它由一组数据以及数据标签（索引）组成
	
	1.1 数据列表是最简单的Series.
	    s1 = pd.Series([1,'a',5.2,7])  s1.index # 获取索引（自带）；  s1.values #获取数值
		
	1.2 创建一个具有标签索引的Series
		s2 = pd.Series([1, 'a', 5.2, 7], index=['d','b','a','c'])
		
	1.3 使用Python字典创建Series
		s3=pd.Series({'Ohio':35000,'Texas':72000,'Oregon':16000,'Utah':5000})索引是键，数据是值
			
	1.4 根据标签索引查询数据   s2['a']  等价于 s2.a
		s2['a']      s2[['b','a']]  
		5.2   			b      a
						a    5.2
						dtype: object
	
	1.5 复杂数据：
		b=pd.Series({"w":2,2:4,3:3,"o":5,"r":6,'key':{1:2,'ad':[1,2,4,'grt']}})
		w                                   2
		2                                   4
		3                                   3
		o                                   5
		r                                   6
		key    {1: 2, 'ad': [1, 2, 4, 'grt']}
		dtype: object
	
	
	2. DataFrame：DataFrame是一个表格型的数据结构每列可以是不同的值类型（数值、字符串、
	布尔值等）既有行索引index,也有列索引columns可以被看做由Series组成的字典。
	
			pandas.DataFrame( data, index, columns, dtype, copy) 格式：
			
			data表示要传入的数据 ，包括 ndarray，series，map，lists，dict，constant和另一个DataFrame

			index和columns 行索引和列索引  格式['x1','x2']

			dtype:每列的类型

			copy: 查了api，才知道意思是从input输入中拷贝数据。默认是false，不拷贝。

	
	
	2.1 根据多个字典序列创建dataframe
	   data={
        'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]
		}
		df = pd.DataFrame(data)
			state	year	pop
		0	Ohio	2000	1.5
		1	Ohio	2001	1.7
		2	Ohio	2002	3.6
		3	Nevada	2001	2.4
		4	Nevada	2002	2.9
	
		df.dtypes   ## 数据类型查询
		state     object
		year      int64
		pop       float64
		dtype: object
		
		df.columns  ## 数据类型列查询 
		Index(['state', 'year', 'pop'], dtype='object')
		df.index    ## 索引查询
		RangeIndex(start=0, stop=5, step=1)
		
		# 数据框构成
		b=pd.Series({"w":2,2:4,3:3,"o":5,"r":6})#通过序列生成数据框
		pd.DataFrame(b,columns=['data'])
			data
		w	2
		2	4
		3	3
		o	5
		r	6
		
		# 转置
		b=pd.Series({"w":2,2:4,3:3,"o":5,"r":6})#通过序列生成数据框
		pd.DataFrame([b],index=['data']) ## 注意这里转置了
	
				w	2	3	o	r
		data	2	4	3	5	6
		
		
		## 数据之间交、并集：
		s=pd.Series([2,1,4,5],index=["a","b","c","d"])
		h=pd.Series([3,1,4,2,1],index=["a","b","c","j","p"])
		# 交集：行标和值的匹配
		s&h
		a    False
		b     True
		c    False
		d    False
		j    False
		p    False
		dtype: bool
		
		
		# 并集：匹配行标
		s|h
		a     True
		b     True
		c     True
		d     True
		j    False
		p    False
		dtype: bool
		
		# 先取并集，在获取对应值
		s[s|h] 
		a    2
		b    1
		c    4
		d    5
		dtype: int64
		
		s[s&h]
		b    1
		dtype: int64
	
		# 数据框的比较过滤：比较都是以列为基础的，大于小于，与或非，等于也是==
		str=pd.DataFrame(np.random.randn(5,3),index=range(2,7), columns=["a","b","c"])
		# 输出值大于0的数据
		str[str>0]
			a	          b	        c
		2	NaN	         NaN	    NaN
		3	NaN	         NaN	    NaN
		4	1.372226	0.639913	2.019606
		5	1.984924	NaN	        NaN
		6	0.209648	NaN	        0.502853
	
		str[str>0].values
		
		array([[       nan,        nan,        nan],
       [       nan,        nan,        nan],
       [1.3722261 , 0.6399132 , 2.01960625],
       [1.98492394,        nan,        nan],
       [0.20964765,        nan, 0.50285343]])
	   
	   # 取a列数据大于-1和b列数据小于0的交集数据
	   str[(str.a>-1)&(str.b<0)]
			   a	       b	       c
		3	-0.851979	-0.845512	-1.093687
		5	1.984924	-0.850480	-0.117204
		6	0.209648	-0.100032	0.502853
		
	   # 取符合条件的c列的数据
		str[(str.a>-1)&(str.b<0)]['c']
		3   -1.093687
		5   -0.117204
		6    0.502853
		Name: c, dtype: float64
		
	   # 取符合条件的a,b列的数据
	   str[(str.a>-1)|(str.c>1)][['a','b']]
				a	        b
		3	-0.851979	-0.845512
		4	1.372226	0.639913
		5	1.984924	-0.850480
		6	0.209648	-0.100032
		
	   # 取符合条件的a,c列数据运算：
	   p=str[(str.a>1)&(str.b<1)]
	   p['a']+p['c']
	   3    1.247894
	   dtype: float64
	   
	   # 取出b,c列和大于5 的数据
	   str[str.b+str.c>5]
	   
	   
	
	3. 从DataFrame中查询出Series如果只查询一行、一列，返回的是pd.Series
	   如果查询多行、多列，返回的是pd.DataFrame。ataframe可以看成一系列有相同索引的series
	   数据框的三个部分：元素，行标，列表。
		df
		   state	year	pop
		0	Ohio	2000	1.5
		1	Ohio	2001	1.7
		2	Ohio	2002	3.6
		3	Nevada	2001	2.4
		4	Nevada	2002	2.9
		
		df['year']            type(df['year'])   pandas.core.series.Series
		0    2000
		1    2001
		2    2002
		3    2001
		4    2002
		Name: year, dtype: int64
		
		df[['year', 'pop']]   type(df[['year', 'pop']]) pandas.core.frame.DataFrame
		year	pop
		0	2000	1.5
		1	2001	1.7
		2	2002	3.6
		3	2001	2.4
		4	2002	2.9
		
	3.1 查询一行，结果是一个pd.Series
		df.loc[1]              type(df.loc[1]) pandas.core.series.Series
		state    Ohio
		year     2001
		pop       1.7
		Name: 1, dtype: object
	
	3.2 查询多行，结果是一个pd.DataFrame
		df.loc[1:3]            type(df.loc[1:3]) pandas.core.frame.DataFrame
			state	year	pop
		1	Ohio	2001	1.7
		2	Ohio	2002	3.6
		3	Nevada	2001	2.4
	
	3.3 loc 和 iloc
	s=pd.DataFrame(np.random.randn(5,3),index=range(2,7), columns=["a","b","c"])
			a	             b	        c
		2	1.480583	-0.679918	0.407060
		3	0.209382	-1.103633	0.192797
		4	-0.523839	-0.009658	0.085058
		5	-0.086303	-0.145322	1.827278
		6	-0.690281	0.191259	-0.955432
	# 数组型：	
	s.iloc[2:4] 
			a	            b	        c
		4	0.115306	1.336463	1.571511
		5	0.609090	-0.645559	0.699919
	# 行标型：
	s.loc[2:4]
			a				b			c
		2	0.979173	0.137159	0.236540
		3	-1.742702	0.876601	0.682438
		4	0.115306	1.336463	1.571511
	# 数组型：	
	s[2:4] ==== s.iloc[2:4]
			a	            b	        c
		4	0.115306	1.336463	1.571511
		5	0.609090	-0.645559	0.699919
	
	# 列索引：
	s['a'] 或者 s.a ========单列
	2    0.979173
	3   -1.742702
	4    0.115306
	5    0.609090
	6    0.455991
	Name: a, dtype: float64
	
	s[['a','b']] 等价 s.loc[:,['a','b']] ========== 不连续多列
		a	           b
	2	0.979173	0.137159
	3	-1.742702	0.876601
	4	0.115306	1.336463
	5	0.609090	-0.645559
	6	0.455991	-0.394967
	
	s.loc[:,'a':'c'] ========== 连续切片多列
		a				b			c
	2	0.979173	0.137159	0.236540
	3	-1.742702	0.876601	0.682438
	4	0.115306	1.336463	1.571511
	5	0.609090	-0.645559	0.699919
	6	0.455991	-0.394967	0.909161
	
	
	# 行索引：
	s.loc[2] ============单行
	a    0.979173
	b    0.137159
	c    0.236540
	Name: 2, dtype: float64
	
	s.loc[[2,3]] ============= 多行不连续
		a				b			c
	2	0.979173	0.137159	0.236540
	3	-1.742702	0.876601	0.682438
	
	s.loc[3:5] ============= 多行连续
			a			b			c
	3	-1.742702	0.876601	0.682438
	4	0.115306	1.336463	1.571511
	5	0.609090	-0.645559	0.699919
	
	# 行列索引：
	s.loc[[2,3],['a','c']]
		a				c
	2	0.979173	0.236540
	3	-1.742702	0.682438
	
	# 行列切片索引：
	s.loc[2:4,'a':'c']
			a			b			c
	2	0.979173	0.137159	0.236540
	3	-1.742702	0.876601	0.682438
	4	0.115306	1.336463	1.571511
	
	# 行列不连续索引：
	s.loc[[2,3,4],["a","b"]]
			a			b
	2	0.979173	0.137159
	3	-1.742702	0.876601
	4	0.115306	1.336463
	
	# 定位一个数据:
	s.loc[2:4].a[3]  ==============行区间+列
	-1.7427016309189551
	
	s.loc[3,'a']
	-1.7427016309189551
	
	s['a'][3]
	-1.7427016309189551
	
	# 定位列方向两个数
	s['a'][[3,4]] ===========连续
	3   -1.742702
	4    0.115306
	Name: a, dtype: float64
	
	s['a'][3:5]   ===========不连续
	5    0.609090
	6    0.455991
	Name: a, dtype: float64
	
	# 定位行方向两个数据;
	s.loc[2:3,'a'] ===========连续
	2    0.979173
	3   -1.742702
	Name: a, dtype: float64
	
	s.loc[[2,4],'a']
	2    0.979173
	4    0.115306
	Name: a, dtype: float64
	
	
	# 行标：
	s.index[3] 数组型
	5
	
	s.loc[5] =========== 单行索引
	a    0.609090
	b   -0.645559
	c    0.699919
	Name: 5, dtype: float64
	
	s.loc[s.index[3]]
	a    0.609090
	b   -0.645559
	c    0.699919
	Name: 5, dtype: float64
	
	## 逐层定位数据：
	s.loc[:,["a","b"]].loc[2:4].a[2] # a[2]：行标是2
	0.9791731190559286
	等价：s.loc[2,'a'] （s.loc[行标,列]）           
		  s['a'][2]    （s[列][行标]）  切片不灵活
	
	# s.iloc(行,列) 数组型，行列标均是切片---切片灵活
	s.iloc[:,0]  ============== 
	2    0.979173
	3   -1.742702
	4    0.115306
	5    0.609090
	6    0.455991
	Name: a, dtype: float64
	
	s.iloc[[2,4],:]
	s.iloc[2:4,:]
	s.iloc[[2,4],[0,2]]
	s.iloc[2:5,0:2] 
	
	
================================ DataFrame 数据结构 ======================================

# f=pd.read_excel('James_Harden.xlsx',encoding='utf-8')

	Unnamed	对手  胜负	主客场	命中 投篮数	投篮命中率	3分命中率	篮板	助攻	得分
0	   0	勇士	胜	客	      10	23	0.435	    0.444	     6	     11	    27
1	   1	国王	胜	客	       8	21	0.381	    0.286	     3	      9	    27
2	   2	小牛	胜	主	      10	19	0.526	    0.462	     3	      7	    29
3	   3	灰熊	负	主	       8	20	0.400	    0.250	     5	      8	    22
4	   4	76人	胜	客	      10	20	0.500	    0.250	     3	      13	27

# 列标名： 
f.columns
Index(['Unnamed: 0', '对手', '胜负', '主客场', '命中', '投篮数', '投篮命中率', '3分命中率', '篮板','助攻', '得分'],dtype='object')

# 列表切片： 
f.columns[2:5]
Index(['胜负', '主客场', '命中'], dtype='object')

# 遍历列表名：
for i in f.columns[3:6]:
    print(i)
主客场
命中
投篮数

# 迭代序列： 元组
for i in f['对手'].iteritems():
    print(i)
(0, '勇士')
(1, '国王')
(2, '小牛')
(3, '灰熊')
(4, '76人')
(5, '黄蜂')
(6, '灰熊')
'''''''''''''
'''''''''''''


# 切片定位特定位置： 
f.loc[f.index[2:5],f.columns[2:5]]  行列均用切片定位
	胜负	主客场	命中
2	胜		主		10
3	负		主		8
4	胜		客		10

# f.loc[f.index[4:8]]：定位行，列全部  || f.loc[:,f.columns[1:5]]：定位列，行全部，注意：:,


# 定位不连续多列： 
f[['篮板','助攻','命中']].apply([np.min,np.mean]) 不连续多列
		篮板	助攻	命中
amin	1.00	3.00	6.0
mean	5.08	9.48	9.8

# 定位连续多列： 
f[f.columns[5:7]].apply([np.min,np.mean]) 连续多列
		投篮数	投篮命中率
amin	15.00	0.31600
mean	21.16	0.46116

#  定位特定行列数据的指标：
f.loc[f.index[4:9],f.columns[5:7]].apply([np.min,np.mean]) 定位特定行列数据的指标
投篮数	投篮命中率
amin	18.0	0.3160
mean	20.2	0.4064



Pandas 的Categorical数据类型可以降低数据存储提升计算速度:

f=pd.read_excel('James_Harden.xlsx',encoding='utf-8')
Unnamed	对手  胜负	主客场	命中 投篮数	投篮命中率	3分命中率	篮板	助攻	得分
0	   0	勇士	胜	客	      10	23	0.435	    0.444	     6	     11	    27
1	   1	国王	胜	客	       8	21	0.381	    0.286	     3	      9	    27
2	   2	小牛	胜	主	      10	19	0.526	    0.462	     3	      7	    29
3	   3	灰熊	负	主	       8	20	0.400	    0.250	     5	      8	    22
4	   4	76人	胜	客	      10	20	0.500	    0.250	     3	      13	27

# 数据表基本信息（维度、列名称、数据格式、所占空间等）
f.info() 
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 25 entries, 0 to 24
Data columns (total 11 columns):
Unnamed: 0    25 non-null int64
对手            25 non-null object --------
胜负            25 non-null object --------
主客场           25 non-null object -------
命中            25 non-null int64
投篮数           25 non-null int64
投篮命中率         25 non-null float64
3分命中率         25 non-null float64
篮板            25 non-null int64
助攻            25 non-null int64
得分            25 non-null int64
dtypes: float64(2), int64(6), object(3)
memory usage: 2.3+ KB ----------------------->指针内存量，非全部内存

f.info(memory_usage="deep")
‘’‘’‘’‘’
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 25 entries, 0 to 24
Data columns (total 11 columns):
Unnamed: 0    25 non-null int64
对手            25 non-null object -------- 字符串
胜负            25 non-null object -------- 字符串
主客场           25 non-null object ------- 字符串
命中            25 non-null int64
投篮数           25 non-null int64
投篮命中率         25 non-null float64
3分命中率         25 non-null float64
篮板            25 non-null int64
助攻            25 non-null int64
得分            25 non-null int64
dtypes: float64(2), int64(6), object(3)
memory usage: 7.9 KB -------------------------> 全部内存 7.9K

## 复制数据，耗内存，低效率
df_cat = df.copy()

df_cat.head()
	Unnamed	对手  胜负	主客场	命中 投篮数	投篮命中率	3分命中率	篮板	助攻	得分
0	   0	勇士	胜	客	      10	23	0.435	    0.444	     6	     11	    27
1	   1	国王	胜	客	       8	21	0.381	    0.286	     3	      9	    27
2	   2	小牛	胜	主	      10	19	0.526	    0.462	     3	      7	    29
3	   3	灰熊	负	主	       8	20	0.400	    0.250	     5	      8	    22
4	   4	76人	胜	客	      10	20	0.500	    0.250	     3	      13	27

### categorical类型降低存储量 ：将字符串储存转变为数字中间储存，降低内存
df_cat = df.copy() 数据先复制

df_cat.head()

df_cat[['对手','胜负','主客场']]=df_cat[['对手','胜负','主客场']].astype("category")#转格式
df_cat.info(memory_usage="deep") # 查看内存
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 25 entries, 0 to 24
Data columns (total 11 columns):
Unnamed: 0    25 non-null int64
对手            25 non-null category -----------格式改变
胜负            25 non-null category
主客场           25 non-null category
命中            25 non-null int64
投篮数           25 non-null int64
投篮命中率         25 non-null float64
3分命中率         25 non-null float64
篮板            25 non-null int64
助攻            25 non-null int64
得分            25 non-null int64
dtypes: category(3), float64(2), int64(6)
memory usage: 4.5 KB ----------------------------内存减小

%timeit df_cat.groupby(['对手','胜负','主客场']).size()
1.96 ms ± 24.9 µs per loop (mean ± std. dev. of 7 runs, 100 loops each) 计算速度减小


==============================================================================================
三、Pandas定位数据
		df.loc方法，根据行、列的标签值查询 
		df.iloc方法，根据行、列的数字位置查询
		df.where方法
		df.query方法
		
	1 df.loc(A,B): # A:行标； B:列标
			ymd			bWendu	yWendu	tianqi		fengxiang	fengli	aqi	aqiInfo	aqiLevel
		0	2018-01-01	3℃		-6℃	晴~多云		东北风		1-2级	59		良		2
		1	2018-01-02	2℃		-5℃	阴~多云		东北风		1-2级	49		优		1
		2	2018-01-03	2℃		-5℃	多云		北风		1-2级	28		优		1
		3	2018-01-04	0℃		-8℃	阴			东北风		1-2级	28		优		1
		4	2018-01-05	3℃		-6℃	多云~晴		西北风		1-2级	50		优		1
		
	1.1 查询单个值
		df.loc['2018-01-03', 'bWendu']     2℃
	
	1.2 查询 Series和DataFrame
		df.loc['2018-01-03', ['bWendu', 'yWendu']]  ## 注意：列表的使用
		df.loc[['2018-01-03','2018-01-04','2018-01-05'], ['bWendu', 'yWendu']] 
		df.loc['2018-01-03':'2018-01-05', 'bWendu'：'yWendu'] #切片区间取值,包含首尾,不加列表
	
	1.3 字符串处理：
	
		使用方法：先获取Series的str属性，然后在属性上调用函数；
		只能在字符串列上使用，不能数字列上使用；
		Dataframe上没有str属性和处理方法
		Series.str并不是Python原生字符串，而是自己的一套方法，不过大部分和原生str很相似；
		Series.str字符串方法列表参考文档:
		https://pandas.pydata.org/pandas-docs/stable/reference/series.html#string-handling
		
		'''
				获取Series的str属性，然后使用各种字符串处理函数
			使用str的startswith、contains等bool类Series可以做条件查询
			需要多次str处理的链式操作
			使用正则表达式的处理
		'''
		
		1.3.1 获取Series的str属性，使用各种字符串处理函数
			  df["bWendu"].str   <pandas.core.strings.StringMethods at 0x1af21871808>
			  df["bWendu"].str.replace("℃", "")  
			  0       3
			  1       2
			  2       2
			  3       0
			  4       3
			  Name: bWendu, Length: 365, dtype: object
			   
			  # 判断是不是数字
			  df["bWendu"].str.isnumeric()    False or True
			  
			  # 列数据个数
			  len(df["aqi"])
			  
			  # 字符串列的每一个字符串长度
			  df["fengxiang"].str.len()
			  
			  # 截取几行字符串个数，数组型
			  df["fengxiang"].str[2:4]
			  
			  # 字符串替换，将空字符串替换 风 字,取3,4,5行的数据
			  df["fengxiang"].str.replace('风',"")[3:6] 
			  
			  # 按条件分割字符串
			  df["fengli"].str.split('-')    df["fengli"].str.split('-')[0]
			  
			  # 替换后，截取字符串,并取每一个字符串前几位数字
			  df["ymd"].str.replace("-", "").str.slice(0, 4)
			
			  # 替换后，截取每一个字符串前几位，打印所有行
			  df["ymd"].str.replace("-", "").str[0:3]
			  
		1.3.2 使用str的startswith、contains等得到bool的Series可以做条件查询
			  
			  # 判断以某个字符串开头的数据，返回布尔值。
			  df["ymd"].str.startswith("2018-03") 
			  df["fengxiang"].str.startswith("东北")
			    ## 查询符合天剑数据所在位置
				df.fengxiang[df["fengxiang"].str.startswith("东北")]
			
			
			  # 判断包含某个字符串的数据，返回布尔值。
			  df["ymd"].str.contains("18")
				## 查询符合天剑数据所在位置
				df[df["ymd"].str.contains("18")]；df["ymd"][df["ymd"].str.contains("18")]
			
			
			  # 字符替换后，改变其数据属性 astype
			  df["bWendu"].str.replace("℃", "").astype('int32')
			  
			  # 分割字符串后expand=True（将分割的数据单独并为一列），转为整型
			  df['yWendu'].str.split('℃',expand=True)[0].astype(int)
			  
			  # 统计符合条件的数据数字和，非数据个数和
			  df['yWendu'].str.split('℃',expand=True)[0].astype(int).sum()
			  
			  # 整数型添加字符串，转化为字符串后添加
			  df['aqi'].astype(str)+'万'
			  
			  
		1.3.3 正则表达式的处理：
			  # 添加新列，自定义函数，编年月日
			  def get_nianyueri(x):
				 year,month,day = x["ymd"].split("-")  ## 元组一一对应
				 return f"{year}年{month}月{day}日"
			  df["中文日期"] = df.apply(get_nianyueri, axis=1) ## axis=1 数据作用到行上
			  
			  问题：怎样将“2018年12月31日”中的年、月、日三个中文字符去除？
			  df["中文日期"].str.replace("年", "").str.replace("月","").str.replace("日", "")
			  
			  Series.str默认就开启了正则表达式模式
			  df["中文日期"].str.replace("[年月日]", "")## 空字符串自动替换列表中三个字
			  
			  
	1.4 条件查询   
		组合条件用&符号合并，每个条件判断都得带括号.
		df.loc[df["aqi"]>10] 
		
		# 查询最高温度小于30度，并且最低温度大于15度，并且是晴天，并且天气为优的数据
		df.loc[(df["bWendu"]<=30) & (df["yWendu"]>=15) & (df["tianqi"]=='晴') & (df["aqiLevel"]==1)]
		
		# 计算整列数据差值
		df['温差']=df['bWendu']-df['yWendu'] # 将两列数据相减
		
		# 计算列中特定数据差值
		'''
		链式操作其实是两个步骤，先get后set，get得到的dataframe可能是view也可能是copy，pandas发出警告

		官网文档： https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

		核心要诀：pandas的dataframe的修改写操作，只允许在源dataframe上进行，一步到位
		
		'''
		
		解决方法1：
		contains = df["ymd"].str.startswith("2018-03") ## 定位需要计算的行区间
		df.loc[condition, "wen_cha"] = df["bWendu"]-df["yWendu"] # 定位数据区间，加上新增列
		df[condition] #打印特定出行区间
		
		解决方法2：
		contains = df["ymd"].str.startswith("2018-03") ## 定位需要计算的行区间
		df_month3 = df[contains].copy() #将需要计算的行先复制出来
		df_month3['温差2']=df['bWendu']-df['yWendu']
		df_month3.head()
		
		解决多行计算问题
		cont=df['ymd'].str.startswith(('2018-02','2018-04')) ## 元组形式，多行不相连数据
		dfs=df[cont].copy()
		dfs['wencha']=df['bWendu']-df['yWendu']
		dfs.head()
		
		
		
四、Pandas对缺失值,重复值,排序，axis，index的处理

	1 缺失值：
	'''
			isnull和notnull：检测是否是空值，可用于df和series
			dropna：丢弃、删除缺失值
			axis : 删除行还是列，{0 or ‘index’, 1 or ‘columns’}, default 0
			how : 如果等于any则任何值为空都删除，如果等于all则所有值都为空才删除
			inplace : 如果为True则修改当前df，否则返回新的df
			fillna：填充空值
			value：用于填充的值，可以是单个值，或者字典（key是列名，value是值）
			method : 等于ffill使用前一个不为空的值填充forword fill；等于bfill使用后一个不为空的值填充backword fill
			axis : 按行还是列填充，{0 or ‘index’, 1 or ‘columns’}
			inplace : 如果为True则修改当前df，否则返回新的df
	'''
	
	1.1 读取excel的时候，忽略前几个空行，从第三行开始  skiprows=2
		studf = pd.read_excel("./datas/student_excel/student_excel.xlsx", skiprows=2)从第三行开
		
		## 检测空值
		studf.isnull() 返回布尔值 ，true：存在；false：不存在
		df['姓名'].isnull()
		
		# 筛选没有空分数的所有行
		studf.loc[studf["分数"].notnull(), :]
		
		# 定位分数是空值的行
		df.loc[df['分数'].isnull()]
	
	1.2 删除掉全是空值的列和行,通过labels来控制删除行或列的个数
		df.dropna(axis=1, how='all')# inplace=True ：加上则作用在原数据上
		df.dropna(axis=0,how='all')
		
	1.3 删除任一行存在空值的列和行
		df.dropna(axis=0,how='any')
		df.dropna(axis=1,how='any')
	
	1.4 删除一行或者一列
		1.4.1 删行
			df.drop(labels=2,axis=0) ##删除特定行，标签是2，默认axis=0
			df.drop(labels=[2,7],axis=0) ## 删除不连续多行
			df.drop(labels=range(2,7),axis=0) ## 删除连续行数2-6
			df.drop(df.index[range(2,7)],axis=0) ## 同上
			df.drop(df.index[1:5]) ## 连续删除
			
			
		1.4.2 删列
			df.drop(['分数'],axis=1) # 删特定列 或者 df.drop(labels=['分数'],axis=1)
			df.drop(['姓名',"科目"],axis=1) # 删除不连续多列
			df.drop(df.columns[range(1,3)],axis=1) ## 删除连续多列
	
	1.5 缺失值填充，用ffill：forward fill
		## 前项填补和后项填补，将缺失值前一项或者后一项数据填补到缺失值上
		df['姓名']=df['姓名'].fillna(method='ffill') #前项填补
		df['科目']=df['科目'].fillna(method='bfill') # 后项填补
		
	1.6 填充缺失值：
		df.fillna({"分数":0}) ## 特定项填充为0  
		df['分数'].fillna(0)  
		df.a.fillna(df.a.mean()) ## 特定项填充为均值
		df.sex.fillna(df.sex.mode()[0]) ## 将缺失值改为出现次数较多的众数，众数可能不止一个
		df['分数'].fillna(df['分数'].mode()[0])
		df.fillna(value={'a':df.a.mode()[0],'b':df.b.mean(),'c':df.c.sum()}) ##多数据填充
		df.fillna(value={df['a'].mode()[0],df['b'].mean(),df['c'].sum()})
		
		
	2，重复值：
	'''
		A.subset：对应值是列名，表示只考虑写的列，将列对应值相同的行进行去重，默认值None，即考虑所有列；
		B.keep='first/last/False’：first：默认值，除了第一次出现外，其余相同的被标记为重复；last：除了最后一次出现外，其余相同的被标记为重复；False：即所有相同的都被标记为重复；
		第一个为对照组，其余为实验组。
		C.使用duplicated()函数检测标记Series中的值、DataFrame中的记录行是否是重复，重复为True，不重复为False；

	'''
	
	2.1 df.duplicated().head() ## 判断前五行是否有重复值，有则是ture,没有则是false
		df[df.duplicated()].head() ## 查看位置
		
		df.duplicated().tail() ## 后五行是否有重复值
		df[df.duplicated()].tail() ## 位置
		
		df.duplicated(subset=['a','b'],keep='first') ## 第一行a,b为对照组，其余为实验组
		df[df.duplicated(subset=['a','b'],keep='first')]#找位置
		
		df.duplicated().sum() # 重复值数量
		df.drop_duplicates() # 删除所有重复值，使每一行数据都不等
		
		
	3，排序的处理：
		df["aqi"].sort_values() 默认升序
		df["aqi"].sort_values(ascending=False) 降序
		
	3.1 DataFrame的排序
		单列排序：
		df.sort_values(by="aqi")
		多列排序：
		df.sort_values(by=['aqiLevel','bWendu']) # 先排'aqiLevel'；在排'bWendu'；默认升序
		# 分别指定升序和降序
		df.sort_values(by=["aqiLevel", "bWendu"], ascending=[True, False])
		
	4，axis理解：
		'''
			axis=0或者"index"：
			如果是单行操作，就指的是某一行
			如果是聚合操作，指的是跨行cross rows
			axis=1或者"columns"：
			如果是单列操作，就指的是某一列
			如果是聚合操作，指的是跨列cross columns
			按哪个axis，就是这个axis要动起来(类似被for遍历)，其它的axis保持不动
		'''
		
		按axis=0/index执行mean聚合操作:
		df.mean(axis=0)  ## 求每一列的均值
		
		按axis=1/index执行mean聚合操作:
		df.mean(axis=1)  ## 求每一行的均值
		
		def get_sum_value(x):
			return x["A"] + x["B"] + x["C"] + x["D"]

		df["sum_value"] = df.apply(get_sum_value, axis=1) ## 按行相加
		
	5，index理解：
		'''
			更方便的数据查询；
			使用index可以获得性能提升；
			自动的数据对齐功能；
			更多更强大的数据结构支持；
		'''
	5.1 重置索引：
		#drop==False，让索引列还保持在column
		df.set_index("userId", inplace=True, drop=False)#保留索引列
		
		df.set_index("userId", inplace=True) #去掉索引列
		
		# 使用column的condition查询方法
		df.loc[df["userId"] == 500].head()
		
		'''
			使用index会提升查询性能
			如果index是唯一的，Pandas会使用哈希表优化，查询性能为O(1);
			如果index不是唯一的，但是有序，Pandas会使用二分查找算法，查询性能为O(logN);
			如果index是完全随机的，那么每次查询都要扫描全表，查询性能为O(N);
		'''
		
		完全随机的顺序查询:
		# 将数据随机打散
		from sklearn.utils import shuffle
		df_shuffle = shuffle(df)

五、数据拼接
	1、merge():
		'''
			merge的语法：
			
			pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=True, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)
			left，right：  要merge的dataframe或者有name的Series
			how：          join类型，'left', 'right', 'outer', 'inner'
			on：           join的key，left和right都需要有这个key
			left_on：      left的df或者series的key
			right_on：     right的df或者seires的key
			left_index，right_index：使用index而不是普通的column做join
			suffixes：     两个元素的后缀，如果列有重名，自动添加后缀，默认是('_x', '_y')
			
			文档地址：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html

			本次讲解提纲：
			电影数据集的join实例
			理解merge时一对一、一对多、多对多的数量对齐关系
			理解left join、right join、inner join、outer join的区别
			如果出现非Key的字段重名怎么办
		
		'''
	数量的对齐关系:
		'''
		left/right：左/右位置的dataframe。
		how：数据合并的方式。left：基于左dataframe列的数据合并；right：基于右dataframe列的数据合并；outer：基于列的数据外合并（取并集）；inner：基于列的数据内合并（取交集）；默认为'inner'。
		on：用来合并的列名，这个参数需要保证两个dataframe有相同的列名。
		left_on/right_on：左/右dataframe合并的列名，也可为索引，数组和列表。
		left_index/right_index：是否以index作为数据合并的列名，True表示是。
		sort：根据dataframe合并的keys排序，默认是。
		suffixes：若有相同列且该列没有作为合并的列，可通过suffixes设置该列的后缀名，一般为元组和列表类型。
		'''
	
	one-to-one：一对一关系，关联的key都是唯一的
		比如(学号，姓名) merge (学号，年龄) 结果条数为：1*1
		
		left = pd.DataFrame({'sno': [11, 12, 13, 14],
				  'name': ['name_a', 'name_b', 'name_c', 'name_d']
						})
		right = pd.DataFrame({'sno': [11, 12, 13, 14],
						  'age': ['21', '22', '23', '24']
						})
		pd.merge(left, right, on='sno')
			
			
	one-to-many：一对多关系，左边唯一key，右边不唯一key
		比如(学号，姓名) merge (学号，[语文成绩、数学成绩、英语成绩])结果条数为：1*N
		
		left = pd.DataFrame({'sno': [11, 12, 13, 14],
				  'name': ['name_a', 'name_b', 'name_c', 'name_d']
				})
		right = pd.DataFrame({'sno': [11, 11, 11, 12, 12, 13],
				   'grade': ['语文88', '数学90', '英语75','语文66', '数学55', '英语29']
				 })
		# 数目以多的一边为准,数据会被复制
		pd.merge(left, right, on='sno')
			
				
	many-to-many：多对多关系，左边右边都不是唯一的
		比如（学号，[语文成绩、数学成绩、英语成绩]） merge (学号[篮球、足球、乒乓球])
		结果条数为：M*N
		left = pd.DataFrame({'sno': [11, 11, 12, 12,12],
				  '爱好': ['篮球', '羽毛球', '乒乓球', '篮球', "足球"]
				})
		
		right = pd.DataFrame({'sno': [11, 11, 11, 12, 12, 13],
				   'grade': ['语文88', '数学90', '英语75','语文66', '数学55', '英语29']
				 })
		# 结果数量会出现乘法
		pd.merge(left, right, on='sno')
		
	1.1 理解left join、right join、inner join、outer join的区别:
		left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

		right = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5'],
                      'C': ['C0', 'C1', 'C4', 'C5'],
                      'D': ['D0', 'D1', 'D4', 'D5']})
					  
		pd.merge(left, right, how='inner') ## 交集：左边和右边的key都有，才会出现在结果里
		
		pd.merge(left, right, how='left') # 左边的都会出现在结果里，右边的如果无法匹配则为Null
		
		pd.merge(left, right, how='right')# 右边的都会出现在结果里，左边的如果无法匹配则为Null
		
		pd.merge(left, right, how='outer')# 左边、右边的都会出现在结果里，如果无法匹配则为Null
		
	
	1.2 非Key的字段重名：
		left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

		right = pd.DataFrame({'key': ['K0', 'K1', 'K4', 'K5'],
                      'A': ['A10', 'A11', 'A12', 'A13'],
                      'D': ['D0', 'D1', 'D4', 'D5']})
		
		pd.merge(left, right, on='key') ？？？？
			key	A_x	B	A_y	D
		0	K0	A0	B0	A10	D0
		1	K1	A1	B1	A11	D1
		
		pd.merge(left, right, on='key', suffixes=('_left', '_right'))
			key	A_left	B	A_right	D
		0	K0	A0	B0	A10	D0
		1	K1	A1	B1	A11	D1
	
	1.3 多列取交集,并集：
		df1 = pd.DataFrame({'alpha':['A','B','B','C','D','E'],'beta':['a','a','b','c','c','e'],'feature1':[1,1,2,3,3,1],'feature2':['low','medium','medium','high','low','high']})
		df2 = pd.DataFrame({'alpha':['A','A','B','F'],'beta':['d','d','b','f'],'pazham':['apple','orange','pine','pear'],'kilo':['high','low','high','medium'],'price':np.array([5,6,5,7])})
		pd.merge(df1,df2,on=['alpha','beta'],how='inner')
		pd.merge(df1,df2,on=['alpha','beta'],how='outer')
	
	
	2 concat方法:
	
	2.1 拼接函数，有行拼接和列拼接，默认是行拼接，拼接方法默认是外拼接（并集）
		
		#### series类型的拼接方法
		## 行拼接：

		df1 = pd.Series([1.1,2.2,3.3],index=['i1','i2','i3'])
		df2 = pd.Series([4.4,5.5,6.6],index=['i2','i3','i4'])
		pd.concat([df1,df2]) 索引会重复，机械相加

		## 行拼接若有相同的索引，为了区分索引，我们在最外层定义了索引的分组情况。
		f=pd.concat([df1,df2],keys=['fea1','fea2']) ## 分层索引
		print(f)

		## 列拼接：默认以并集的方式拼接：
		f=pd.concat([df1,df2],axis=1,keys=['第一列','第二列'],sort=True) ## 设置列名
		print(f)

		# 列拼接的内连接（交）
		f=pd.concat([df1,df2],axis=1,join='inner',keys=['第一列','第二列'],sort=True)
		print(f)

		# 指定索引[i1,i2,i3]的列拼接
		# f=pd.concat([df1,df2],axis=1,join_axes=[['i1','i2','i3']],keys=['第一列','第二列'])
		# print(f)  该种形式将被淘汰
		f=pd.concat([df1,df2.reindex(['i1','i2','i3'])],axis=1,keys=['第一列','第二列'])
		print(f)

		### dataframe类型的拼接方法
		df1 = pd.DataFrame({'alpha':['A','B','B','C','D','E'],'feature1':[1,1,2,3,3,1],
					'feature2':['low','medium','medium','high','low','high']})
		df2 = pd.DataFrame({'alpha':['A','A','B','F'],'pazham':['apple','orange','pine','pear'],
					'kilo':['high','low','high','medium'],'price':np.array([5,6,5,7])})
		print(pd.concat([df1,df2],sort=True)) ##默认纵向合并,取并集
		print(pd.concat([df1,df2],sort=True,join='inner'))
		print(pd.concat([df1,df2],sort=True,axis=1,join='inner')) ## 横向拼接行标相同部分
		print(pd.concat([df1,df2],sort=True,axis=1,join='inner'))
		print('************************')
		
	2.2 
	'''
			一句话说明concat语法：
		使用某种合并方式(inner/outer)
		沿着某个轴向(axis=0/1)
		把多个Pandas对象(DataFrame/Series)合并成一个。
		
		
		concat语法：pandas.concat(objs, axis=0, join='outer', ignore_index=False)
		objs：一个列表，内容可以是DataFrame或者Series，可以混合
		axis：默认是0代表按行合并，如果等于1代表按列合并
		join：合并的时候索引的对齐方式，默认是outer join，也可以是inner join
		ignore_index：是否忽略掉原来的数据索引
		
		
		append语法：DataFrame.append(other, ignore_index=False)
		append只有按行合并，没有按列合并，相当于concat按行的简写形式
		other：单个dataframe、series、dict，或者列表
		ignore_index：是否忽略掉原来的数据索引
		
		pandas.concat的api文档：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
		pandas.concat的教程：https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html
		pandas.append的api文档：https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html
		
	'''
		默认的concat，参数为axis=0、join=outer、ignore_index=False:数据往下排，取并集，索引号分别是每一个数据的索引号
			A	B	C	D	E	F
		0	A0	B0	C0	D0	E0	NaN
		1	A1	B1	C1	D1	E1	NaN
		2	A2	B2	C2	D2	E2	NaN
		3	A3	B3	C3	D3	E3	NaN
		0	A4	B4	C4	D4	NaN	F4
		1	A5	B5	C5	D5	NaN	F5
		2	A6	B6	C6	D6	NaN	F6
		3	A7	B7	C7	D7	NaN	F7
		
		使用ignore_index=True可以忽略原来的索引：索引从新排序0-。。。
		pd.concat([df1,df2], ignore_index=True)
			A	B	C	D	E	F
		0	A0	B0	C0	D0	E0	NaN
		1	A1	B1	C1	D1	E1	NaN
		2	A2	B2	C2	D2	E2	NaN
		3	A3	B3	C3	D3	E3	NaN
		4	A4	B4	C4	D4	NaN	F4
		5	A5	B5	C5	D5	NaN	F5
		6	A6	B6	C6	D6	NaN	F6
		7	A7	B7	C7	D7	NaN	F7
	
		pd.concat([df1,df2], ignore_index=True, join="inner")：取交集，排序
		
		
		添加一列Series：
		axis=1
		s1 = pd.Series(list(range(4)), name="F")
		pd.concat([df1,s1], axis=1)	
			A	B	C	D	E	F
		0	A0	B0	C0	D0	E0	0
		1	A1	B1	C1	D1	E1	1
		2	A2	B2	C2	D2	E2	2
		3	A3	B3	C3	D3	E3	3
		
		
		添加多列DataFrame：
		axis=1
		s2=pd.DataFrame([[1,2],[1,4]],columns=['tom','ale'])
		pd.concat([df2,s2],axis=1)
		
		=======================================
		s5=pd.DataFrame(df1.apply(lambda x:x["A"]+"12_GG",axis=1),index=list(range(4)),columns=['TF'])
		pd.concat([df1,s5],axis=1)
		   ### 解析：df1.apply(lambda x:x["A"]+"12_GG",axis=1)：构造新序列
			## index对象包括index和columns,必须要是集合类型的，可以是{}，[]
		
			A	B	C	D	E	TF
		0	A0	B0	C0	D0	E0	A012_GG
		1	A1	B1	C1	D1	E1	A112_GG
		2	A2	B2	C2	D2	E2	A212_GG
		3	A3	B3	C3	D3	E3	A312_GG	
			
		# 列表可以只有Series
		s1=df1.apply(lambda x:x["A"]+"12_GG",axis=1)
		s2=pd.Series(list(range(4)), name="F")
		pd.concat([s1,s2], axis=1)	
		
		
		# 列表是可以混合顺序的
		df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3'],
                    'E': ['E0', 'E1', 'E2', 'E3']
                   })
		s1=df1.apply(lambda x:x["A"]+"12_GG",axis=1)
		s2=pd.Series(list(range(4)), name="F")
		pd.concat([s1,df1,s2], axis=1)
		
	3 append():
	
	3.1 给1个dataframe添加另一个dataframe，忽略原来的索引ignore_index=True
		df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
		df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
		df1.append(df2,ignore_index=True) df2加在df1下面
		
	3.2 可以一行一行的给DataFrame添加数据
		# 一个空的df,无数据，只有列表名
		df = pd.DataFrame(columns=['A'])
		
		A：低性能版本
		for i in range(5):
			# 注意这里每次都在复制
			df = df.append({'A': i}, ignore_index=True)
			
			
		B：性能好的版本
		# 第一个入参是一个列表，避免了多次复制
		pd.concat(
			[pd.DataFrame([i], columns=['A']) for i in range(5)],
			ignore_index=True
		)

六、groupby分组统计：
	groupby：先对数据分组，然后在每个分组上应用聚合函数、转换函数
	
	df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
	
	1.1 单个列groupby，查询所有数据列的统计：
		df.groupby('A').sum()  B列不是数字，所以被自动忽略掉
	
	1.2 多个列groupby，查询所有数据列的统计:
		df.groupby(['A','B']).mean()
						C	        D
		A	   B		
		bar	  one	 -0.375789	   -0.345869
		     three	 -1.564748	    0.081163
		      two	 -0.202403	    0.701301
		foo	  one   -0.061143	   -0.358197
		     three	 -0.498339	    0.534438
		      two 	 -0.998504	    0.632690
		
		df.groupby(['A','B'], as_index=False).mean() 补全索引
		
		    A	B	    C	              D
		0	bar	one	-0.375789	-0.345869
		1	bar	three	-1.564748	0.081163
		2	bar	two	-0.202403	0.701301
		3	foo	one	-0.061143	-0.358197
		4	foo	three	-0.498339	0.534438
		5	foo	two	-0.998504	0.632690
	
	1.3 分组后查看数据特征：
		同时查看多种数据统计，多列数据的结果（C,D列）
		df.groupby('A').agg([np.sum, np.mean, np.std])
		
						               C				                    D
			  sum	      mean	       std	       sum	     mean	       std
		A						
		bar	-2.142940	-0.714313	0.741583	0.436595	0.145532	0.526544
		foo	-2.617633	-0.523527	0.637822	1.083423	0.216685	0.977686
		
		
	1.4 查看单列的结果数据统计：
		# 方法1：预过滤，性能更好（C列）
		df.groupby('A')['C'].agg([np.sum, np.mean, np.std])	
		
				sum	       mean	     std
		A			
		bar	-2.142940	-0.714313	0.741583
		foo	-2.617633	-0.523527	0.637822
		
		
		# 不同列使用不同的聚合函数
		df.groupby('A').agg({"C":[np.sum,np.mean], "D":np.mean})
		
						     C	      D
				sum     	mean	  mean
		A			
		bar	2.213050	0.737683	0.079646
		foo	2.765199	0.553040	0.864363
		
	1.5 遍历groupby的结果理解执行流程：
		for循环可以直接遍历每个group：
		name，group:分别代表按A分的两个索引bar和foo,group代表分类后的数据
		
		for name,group in df.groupby('A'):  单列分组遍历
			print(name)
			print(group)
			print()
		
		bar
			 A      B         C         D
		1  bar    one  2.362359  0.901756
		3  bar  three -0.001780  0.050572
		5  bar    two -0.147530 -0.713391

		foo
			 A      B         C         D
		0  foo    one -1.017283  0.625038
		2  foo    two  1.655907  0.039762
		4  foo    two  0.633972  1.394077
		6  foo    one  1.441604  1.704482
		7  foo  three  0.050999  0.558456
		
		# 可以获取单个分组的数据
		df.groupby('A').get_group('bar') # 只获得分组后bar的数据
			A	B	      C	        D
		1	bar	one	   2.362359	    0.901756
		3	bar	three	-0.001780	0.050572
		5	bar	two	   -0.147530	-0.713391
		
		g.get_group(('foo', 'one')) ## （）一行
			A	B	   C	      D
		0	foo	one	  0.542903	 0.788896
		6	foo	one	 -0.665189	-1.505290
		
		## 可以直接查询group后的某几列，生成Series或者子DataFrame
		for name, group in df.groupby('A')['C']:
			print(name)
			print(group)
			print(type(group))
			print()
		
				bar
		1    2.362359
		3   -0.001780
		5   -0.147530
		Name: C, dtype: float64

		foo
		0   -1.017283
		2    1.655907
		4    0.633972
		6    1.441604
		7    0.050999
		Name: C, dtype: float64

		
		for i ,j in df.groupby(['A','B']):   多列分组遍历
			print(i)
			print(j)
			print()
				
		('bar', 'one')
			 A    B         C         D
		1  bar  one  2.362359  0.901756

		('bar', 'three')
			 A      B        C         D
		3  bar  three -0.00178  0.050572

		('bar', 'two')
			 A    B        C         D
		5  bar  two -0.14753 -0.713391

		('foo', 'one')
			 A    B         C         D
		0  foo  one -1.017283  0.625038
		6  foo  one  1.441604  1.704482

		('foo', 'three')
			 A      B         C         D
		7  foo  three  0.050999  0.558456

		('foo', 'two')
			 A    B         C         D
		2  foo  two  1.655907  0.039762
		
		4  foo  two  0.633972  1.394077
		
	1.6	迭代与groupby：
	'''
		序列与数据框的迭代:
		基于python的数据分析通常都希望通过函数完成对多个元素的操作，而避免直接通过python的循环来进
		运算，这主要是考虑到python循环效率不高，通常函数底层都用c实现的循环。
		但是有时确实要做一些非常特殊的统计必须要通过python进行循环。
		
		iterrows(): 将DataFrame迭代为(index, Series)对。
		itertuples(): 将DataFrame迭代为元祖。
		iteritems():将DataFrame迭代为(列名, Series)对
	'''
		s=pd.DataFrame({"a":["i","j","k","i","j","k"],"b":[2,1,4,1,2,4],"c":[3,2,2,1,2,3]})
		for i in s.a.iteritems():
			## 迭代出元组（索引，值）
			print(i)  
			(0, 'i')
			(1, 'j')
			(2, 'k')
			(3, 'i')
			(4, 'j')
			(5, 'k')
	
		for i in s.a.iteritems():
			# 元组按数组取值：可以遍历每一个数值
			print(i[0],i[1])  
			0 i
			1 j
			2 k
			3 i
			4 j
			5 k
	
		for i in s.iteritems():
			# 数据框迭代，按列分三组，元组（列名，索引+值）
			print(i)
			('a', 0    i
				1    j
				2    k
				3    i
				4    j
				5    k
				Name: a, dtype: object)
			# 遍历列标
			print(i[0])
			a
			b
			c
			# 遍历索引+值
			print(i[1])
			0    i
			1    j
			2    k
			3    i
			4    j
			5    k
			Name: a, dtype: object
			# 遍历每一行数值
			print(i[1][0])   i 2 3  
			print(i[1][1])
			print(i[1][2])
			''''''''''
		
		# 遍历列标：
		for i in s.iteritems():
			for j in i[0]:
				print(j) a,b,c
		
		# 遍历每一个数据：
		for i in s.iteritems():
			for j in i[1]:
				print(j)
		
		for i in s.iterrows():
			   for j in i[1]:
					print(j)
			
		# 遍历行标和每一行内容：
		for i in s.iterrows():
		        # 遍历行标
				print(i[0])
				# 每一行内容 数组
				print(i[1].values)
				
		for i in s.iterrows(): ## 迭代行
				print(i[1].loc['a':'b'])		
				print(i[1].loc[['a','b']])
				print(i[1].loc['a'])
				print(i[1].values)
				
		## 遍历计算：
	    for i in s.iterrows():
			if i[1].loc[["b","c"]].sum()>5: # b+c 和 大于5 则输出该行的元组
				print(i[0]) # 输出符合条件行号
				print(i[1]) # 输出对应数值元组
		2
		a    k
		b    4
		c    2
		Name: 2, dtype: object
		5
		a    k
		b    4
		c    3
		Name: 5, dtype: object	
		
		# 每行特定不连续列计算
		for i in s.iterrows():
			if i[1].b+i[1].c>5:  ## 同上
			print(i[1])
				
		# 每行连续列计算：切片形式连续取值
		for i in s.iterrows():
			if i[1].loc['b':'c'].sum()>5: # b+c 和 大于5 则输出该行的元组
				print(i[0]) # 输出符合条件行号
				print(i[1]) # 输出对应数值元组	
		cc
		a    k
		b    4
		c    2
		Name: cc, dtype: object
		ff
		a    k
		b    4
		c    3
		Name: ff, dtype: object	
	
	1.7 条件判断：
	
		# 每行计算：输出数据框
		s[s.b+s.c>5]		
			a	b	c
		cc	k	4	2
		ff	k	4	3	
		
		# 输出b列数据大于1的数据框
		s[s.b>1]
			a	b	c
		aa	i	2	3
		cc	k	4	2
		ee	j	2	2
		ff	k	4	3
		
		# 先条件在分组：
		for i in s[s.b>1].groupby("a"):
			print(i[1])
			a  b  c
		aa  i  2  3
			a  b  c
		ee  j  2  2
			a  b  c
		cc  k  4  2
		ff  k  4  3
		
		# 先分组后条件：
		'''
			for i in s.groupby('a'): 按a分组后有三个数据框
				print(i[1])
				print()
				a  b  c
			aa  i  2  3
			dd  i  1  1
			
				a  b  c
			bb  j  1  2
			ee  j  2  2
			
				a  b  c
			cc  k  4  2
			ff  k  4  3
		
		'''
		
		def gl(x):  ================>这里x是分组后的每组数据框
			return x[x['b']>1]
		s.groupby('a').apply(gl)
		
		s.groupby('a').apply(lambda x:x[x.b>1]) =====》同上
		
				a	b	c
		a				
		i	aa	i	2	3
		j	ee	j	2	2
		k	cc	k	4	2
			ff	k	4	3
		
		
		# 按a列分组，再将b列数据求和
		s.groupby("a").b.sum()
		a
		i    3
		j    3
		k    8
		Name: b, dtype: int64
		
		# 取出和大于3的数据
		s.groupby("a").b.sum()[s.groupby("a").b.sum()>3]
		a
		k    8
		Name: b, dtype: int64
		
		
		# 请过滤出所有c列中值为偶数的记录
		s[s.c%2==0]
			a	b	c
		bb	j	1	2
		cc	k	4	2
		ee	j	2	2
		
		for i in s.groupby('c'):
			print(i[1])				
			a  b  c
		dd  i  1  1
			a  b  c
		bb  j  1  2
		cc  k  4  2
		ee  j  2  2
			a  b  c
		aa  i  2  3
		ff  k  4  3
		
		s.groupby('c').size()
		c
		1    1
		2    3
		3    2
		dtype: int64
		
		s.groupby('c').size()[s.groupby('c').size()>2]
		c
		2    3
		dtype: int64
		
		
		
	1.8 groupby():分组迭代：
	
		# 单列数据分组：
		for i in s.groupby('a'): 按字符串分组迭代
			print(i[1])
			a  b  c
		aa  i  2  3
		dd  i  1  1
			a  b  c
		bb  j  1  2
		ee  j  2  2
			a  b  c
		cc  k  4  2
		ff  k  4  3
		
		
		for i in s.groupby('b',sort=False): 按数字分组迭代,不排序
			print(i[1])
			a  b  c
		aa  i  2  3
		ee  j  2  2
			a  b  c
		bb  j  1  2
		dd  i  1  1
			a  b  c
		cc  k  4  2
		ff  k  4  3
		
		### 多列数据分组迭代：计算出数值，非数据框。
		for i in s.groupby(["a","c"]):
				print(i[1])
			a  b  c
		dd  i  1  1
			a  b  c
		aa  i  2  3
			a  b  c
		bb  j  1  2
		ee  j  2  2
			a  b  c
		cc  k  4  2
			a  b  c
		ff  k  4  3
		
		# 先分组，在计算：
		for i in s.groupby('c'):
		    # 分组后，计算b列和与c列数据和
			print(i[1].b+i[1].c) 
			dd    2
			dtype: int64
			bb    3
			cc    6
			ee    4
			dtype: int64
			aa    5
			ff    7
			dtype: int64	
		
		for i in s.groupby('c'):
			## 求b列和
			print(i[1].b.sum()) ## 求b列和
			1
			7
			6
			## b列和与c列和
			print(i[1].loc[:,['b','c']].sum())
			b    1
			c    1
			dtype: int64
			b    7
			c    6
			dtype: int64
			b    6
			c    6
			dtype: int64
		
		### 多数据分组计算,输出数据框。
		# 
		s.groupby("c").sum() 
			b
		c	
		1	1
		2	7
		3	6
		
		s.groupby('a').sum()   
			b	c
		a		
		i	3	4
		j	3	4
		k	8	5
		
		s.groupby("a").size() #分组后，每一行数据个数
		a
		i    2
		j    2
		k    2
		dtype: int64
		
		s.groupby("a").b.var() # 分组后，b列数据方差
		
		s.groupby('a').get_group('k') # 分组后，只获取k列数据
			a	b	c
		cc	k	4	2
		ff	k	4	3
		
		
	1.9 series与dataframe的运算:
		'''
			数据框和序列的运算本质上是一种自动遍历，用来避免直接python循环的好方法
			
			运算函数：sub;add;div
			
			与常数的运算
		'''	
		f=pd.Series([2,1,4,5],index=["a","b","c","d"])
		print(f+3)
		print(np.exp(f))
		print(f**2+6)
		print(a.sub(3))
		
		def w1(x):#还是自定义函数
			return x-9+2

		print(w1(a))  ## 将序列中的值带入函数中运算
		
		## 索引对齐:索引会取并集，找不到相同索引匹配进行运算的则为nan
		s=pd.Series([2,1,4,5],index=["a","b","c","d"])
		h=pd.Series([3,1,4,2,1],index=["a","b","c","j","p"])
		print(s+h) 
		a    5.0
		b    2.0
		c    8.0
		d    NaN
		j    NaN
		p    NaN
		dtype: float64
		
		'''
			#如果你希望缺失值用其他值来替代而不是空缺，则需要用函数来运算并加入fill_value参数
			a.add(b,fill_value=0)
			#上面没找到匹配值的时候则用0来替代
			#注意加法运算之后数据类型都变为了float

		'''
		
		s.add(h,fill_value=0) #h加到s上去，缺失值补0，在计算：
		a    5.0
		b    2.0
		c    8.0
		d    5.0
		j    2.0
		p    1.0
		dtype: float64
		
		## 数据集的运算
		# np.random.randint(0,10,size=(3,2))：3×2，共计随机的6个数，大小在0-10之间
		## 该例子中两个数据集行标数不同，没有匹配的，自动填充2
		d=pd.DataFrame(np.random.randint(0,10,size=(3,2)),columns=["a","b"])
		c=pd.DataFrame(np.random.randint(0,10,size=(4,3)),columns=["a","b","c"])
		print(d.div(c,fill_value=2)) ## div:除法。
		## div:除法，缺失值补2
				a			b			c
		0	1.200000	0.666667	0.285714
		1	0.333333	0.285714	1.000000
		2	1.000000	0.666667	0.500000
		3	0.666667	0.500000	1.000000
		
				
七、分层索引：
	'''
			分层索引：在一个轴向上拥有多个索引层级，可以表达更高维度数据的形式；
		可以更方便的进行数据筛选，如果有序则性能更好；
		groupby等操作的结果，如果是多KEY，结果是分层索引，需要会使用
		一般不需要自己创建分层索引(MultiIndex有构造函数但一般不用)
	'''
	
	1.1 数据通览：
	df.shape:数据(行，列)
	df.index:数据行标内容
	df.columns：数据列标内容
	df['公司'].unique() : 查看一列的类别
	df.groupby('公司')["收盘"].mean():按一列数据分组后，获取分组后另一维度数据的均值
	
	## 数据框常用统计函数及其方向性
	str=pd.DataFrame(np.random.randn(5,3),index=range(2,7), columns=["a","b","c"])
	len(str.columns) ==== 数据宽度（列个数）
	len(str.index) ====== 数据长度（行个数）
	str.b.size == str['b'].size ========== b列的数据个数
	str.size ====== 总数
	str.shape =====维度 (5,3)
	'''
		统计函数：
		平均（mean）,求和（sum），最大值(max)，最小值(min)，中位数(median)，方差（var），标		准差（std），累乘（prod），first,last,mean,median（中位数）,mad（均值绝对偏差）

		describe
	
	'''
	
	
	
	1.2 Series的分层索引MultiIndex
	df.groupby(['公司', '日期'])['收盘'].mean()
			日期          公司  
		2019-10-01  BABA    165.15
					BIDU    102.00
					IQ       15.92
					JD       28.19
		2019-10-02  BABA    165.77
					BIDU    102.62
					IQ       15.72
					JD       28.06
		2019-10-03  BABA    169.48
					BIDU    104.32
					IQ       16.06
					JD       28.80
		Name: 收盘, dtype: float64
		
	df.groupby(['日期','公司'])['收盘'].mean().index ：获取双层索引元组	
		
		
	df.groupby(['公司', '日期'])['收盘'].mean().unstack()
	
	# unstack把二级索引变成列
	
			公司	BABA	BIDU	 IQ	     JD
		日期				
		2019-10-01	165.15	102.00	15.92	28.19
		2019-10-02	165.77	102.62	15.72	28.06
		2019-10-03	169.48	104.32	16.06	28.80
	
	# 重置索引，加上索引序列
	ser.reset_index()
			日期	公司	收盘
		0	2019-10-01	BABA	165.15
		1	2019-10-01	BIDU	102.00
		2	2019-10-01	IQ	15.92
		3	2019-10-01	JD	28.19
		4	2019-10-02	BABA	165.77
	
	
	1.3 Series有多层索引MultiIndex筛选数据
		# 筛选二级索引
		ser.loc['BIDU']
			日期
		2019-10-01    102.00
		2019-10-02    102.62
		2019-10-03    104.32
		Name: 收盘, dtype: float64
	
		# 多层索引，可以用元组的形式筛选
		ser.loc[('BIDU', '2019-10-02')]    102.62
		
		ser.loc[:, '2019-10-02']
				公司
		BABA    165.77
		BIDU    102.62
		IQ       15.72
		JD       28.06
		Name: 收盘, dtype: float64
	
	1.4 DataFrame的多层索引MultiIndex
		## 重新设置行标，多级索引
		stocks.set_index(['公司', '日期'], inplace=True)
							收盘	 开盘	 高	     低	  交易量	涨跌幅
		公司	日期						
		BIDU	2019-10-03	104.32	102.35	104.73	101.15	2.24	0.02
				2019-10-02	102.62	100.85	103.24	99.50	2.69	0.01
				2019-10-01	102.00	102.80	103.26	101.00	1.78	-0.01
		BABA	2019-10-03	169.48	166.65	170.18	165.00	10.39	0.02
				2019-10-02	165.77	162.82	166.88	161.90	11.60	0.00
				2019-10-01	165.15	168.01	168.23	163.64	14.19	-0.01
		IQ		2019-10-03	16.06	15.71	16.38	15.32	10.08	0.02
				2019-10-02	15.72	15.85	15.87	15.12	8.10	-0.01
				2019-10-01	15.92	16.14	16.22	15.50	11.65	-0.01
		JD		2019-10-03	28.80	28.11	28.97	27.82	8.77	0.03
				2019-10-02	28.06	28.00	28.22	27.53	9.53	0.00
				2019-10-01	28.19	28.22	28.57	27.97	10.64	0.00
	
	1.5 【重要知识】在选择数据时：

		元组(key1,key2)代表筛选多层索引，其中key1是索引第一级，key2是第二级，比如key1=JD, 	key2=2019-10-02
		列表[key1,key2]代表同一层的多个KEY，其中key1和key2是并列的同级索引，比如key1=JD, 	    key2=BIDU
		
		## 获取第一层索引：
		df.loc['JD']
							收盘	开盘	高		低		交易量	涨跌幅
		公司	日期						
		JD		2019-10-01	28.19	28.22	28.57	27.97	10.64	0.00
				2019-10-02	28.06	28.00	28.22	27.53	9.53	0.00
				2019-10-03	28.80	28.11	28.97	27.82	8.77	0.03
				
		
		# 两层索引
		df.loc[('JD', '2019-10-02')]  
		收盘     28.19
		开盘     28.22
		高       28.57
		低       27.97
		交易量    10.64
		涨跌幅     0.00
		Name: (JD, 2019-10-01), dtype: float64
		
	
		df.loc[('JD','2019-10-01'),'交易量'] 两层索引+特定列
		10.64
		
		## 获取第一级同列索引
		df.loc[['JD','IQ']] 
							收盘	开盘	高		低		交易量	涨跌幅
		公司	日期						
		IQ		2019-10-01	15.92	16.14	16.22	15.50	11.65	-0.01
				2019-10-02	15.72	15.85	15.87	15.12	8.10	-0.01
				2019-10-03	16.06	15.71	16.38	15.32	10.08	0.02
		JD		2019-10-01	28.19	28.22	28.57	27.97	10.64	0.00
				2019-10-02	28.06	28.00	28.22	27.53	9.53	0.00
				2019-10-03	28.80	28.11	28.97	27.82	8.77	0.03
	
		## 获取第一层同列索引+第二层索引特定值
		df.loc[(['BIDU', 'JD'], '2019-10-03'),:]
							收盘	开盘	高		低		交易量	涨跌幅
		公司	日期						
		BIDU	2019-10-03	104.32	102.35	104.73	101.15	2.24	0.02
		JD		2019-10-03	28.80	28.11	28.97	27.82	8.77	0.03
		
		
		
		df.loc[(['BIDU', 'JD'], '2019-10-03'), '收盘']
				公司    日期        
		BIDU  2019-10-03    104.32
		JD    2019-10-03     28.80
		Name: 收盘, dtype: float64
		
		
		
		df.loc[('BIDU', ['2019-10-02', '2019-10-03']), '收盘']
				公司    日期        
		BIDU  2019-10-02    102.62
			  2019-10-03    104.32
		Name: 收盘, dtype: float64
		
		
		
		df.loc[(['BIDU','JD'],['2019-10-01','2019-10-03']),['开盘','涨跌幅']]
		
							开盘	涨跌幅
		公司	日期		
		BIDU	2019-10-01	102.80	-0.01
				2019-10-03	102.35	0.02
		JD		2019-10-01	28.22	0.00
				2019-10-03	28.11	0.03
		
		
		# slice(None)代表筛选这一索引的所有内容
		df.loc[(slice(None), ['2019-10-02', '2019-10-03']), :]
		
							收盘	开盘	高		低		交易量	涨跌幅
		公司	日期						
		BABA	2019-10-02	165.77	162.82	166.88	161.90	11.60	0.00
				2019-10-03	169.48	166.65	170.18	165.00	10.39	0.02
		BIDU	2019-10-02	102.62	100.85	103.24	99.50	2.69	0.01
				2019-10-03	104.32	102.35	104.73	101.15	2.24	0.02
		IQ		2019-10-02	15.72	15.85	15.87	15.12	8.10	-0.01
				2019-10-03	16.06	15.71	16.38	15.32	10.08	0.02
		JD		2019-10-02	28.06	28.00	28.22	27.53	9.53	0.00
				2019-10-03	28.80	28.11	28.97	27.82	8.77	0.03
				
		df.reset_index():重置索引
		
			公司	日期	    收盘	开盘	高	     低	  交易量	涨跌幅
		0	BABA	2019-10-01	165.15	168.01	168.23	163.64	14.19	-0.01
		1	BABA	2019-10-02	165.77	162.82	166.88	161.90	11.60	0.00
		2	BABA	2019-10-03	169.48	166.65	170.18	165.00	10.39	0.02
		3	BIDU	2019-10-01	102.00	102.80	103.26	101.00	1.78	-0.01
		
	1.6 Pandas实现groupby聚合后不同列数据统计
		记忆：agg(新列名=函数)、agg(新列名=(原列名，函数))、agg({"原列名"：函数/列表})
		agg函数的两种形式，等号代表“把结果赋值给新列”，字典/元组代表“对这个列运用这些函数”
		
		# 聚合后单列-单指标统计
		df.groupby("MovieID")["Rating"].mean().head()
			 MovieID
		1    4.146846
		2    3.201141
		3    3.016736
		4    2.729412
		5    3.006757
		Name: Rating, dtype: float64
		
		
		## 聚合后单列-多指标统计：
		
		# 方法1： agg函数传入多个结果列名=函数名形式
		df.groupby('MovieID')["Rating"].agg([np.sum,np.mean]).head()
				sum		mean
		MovieID		
		1		8613	4.146846
		2		2244	3.201141
		3		1442	3.016736
		4		464		2.729412
		5		890		3.006757


		# 方法2：agg函数传入字典，key是column名，value是函数列表
		df.groupby("MovieID").agg({"Rating":[np.mean, np.max, np.min]}).head()
				Rating
				mean		amax	amin
		MovieID			
		1		4.146846	5		1
		2		3.201141	5		1
		3		3.016736	5		1
		4		2.729412	5		1
		5		3.006757	5		1
		
		更换列标签：去掉双层列标签
		result=df.groupby("MovieID").agg({"Rating":[np.mean, np.max, np.min]})
		result.columns=['age_mean', 'age_min', 'age_max']
		result.head()
				age_mean  age_min	age_max
		MovieID			
		1		4.146846	5			1
		2		3.201141	5			1
		3		3.016736	5			1
		4		2.729412	5			1
		5		3.006757	5			1
​

		# 方法3：新列=(原列名,'函数名形式') 函数名形式只能有一种
		等号代表“把结果赋值给新列”，字典/元组代表“对这个列运用这些函数”
		df.groupby("MovieID").agg(rating_mean=("Rating", "mean"),
								rating_min=("Rating", "min"),
								rating_max=("Rating", "max")
		
		)
		
		
		## 聚合后多列-多指标统计：
		
		# 方法1：
		
		# 多列同指标：
		df.groupby("UserID")['MovieID','Rating'].agg([np.mean,np.min])
		
		# 多列不同指标：
		df.groupby("UserID").agg({'MovieID':[np.mean,np.max],'Rating':np.min})
		
		df.groupby("MovieID").agg(rating_mean=("Rating", "mean"),
								UserID_min=("UserID", "min"),
								UserID_max=("UserID", "max")
		
		)
		
		# 方法2：函数法（使用groupby之后apply对每个子df单独统计）
		def agg_func(x):
			"""注意，这个x是子DF"""
			
			# 这个Series会变成一行，字典KEY是列名
		return pd.Series({
				"rating_mean": x["Rating"].mean(),
				"rating_min": x["Rating"].min(),
				"rating_max": x["Rating"].max(),
				"user_count": x["UserID"].nunique()
		})

		df.groupby("MovieID").apply(agg_func).head()
		
		
	1.7 groupby分组后的apply():
		os.chdir(r'F:\python代码\数据分析\统计与计数\ant-learn-pandas-master\datas
		\beijing_tianqi')
		df=pd.read_csv('beijing_tianqi_2018.csv')
		df['bWendu']=df['bWendu'].str.replace('℃','').map(int)
		df['month']=df['ymd'].str[:7]
		def function(f,top):
			return f.sort_values(by='bWendu')[['ymd','bWendu']][-top:]
		# 得到每一个月温度最高的两天及其温度	
		d=df.groupby('month').apply(function,top=2)
					
						ymd       bWendu
		month                          
		2018-01 13   2018-01-14       6
				18   2018-01-19       7
		2018-02 53   2018-02-23      10
				56   2018-02-26      12
		2018-03 86   2018-03-28      25
				85   2018-03-27      27
				
				
		
八、Pandas的数据转换函数map、apply、applymap
	'''
		数据转换函数对比：map、apply、applymap：
			map：只用于Series，实现每个值->值的映射；
			apply：用于Series实现每个值的处理，用于Dataframe实现某个轴的Series的处理；
			applymap：只能用于DataFrame，用于处理该DataFrame的每个元素；
	'''
	1.1 map用于Series值的转换(字典键值的映射关系)
	
		### Series.map(dict)
		
		# 公司股票代码到中文的映射，注意这里是小写
		dict_company_names = {
			"bidu": "百度",
			"baba": "阿里巴巴",
			"iq": "爱奇艺", 
			"jd": "京东"
		}
		# str.lower()：大写化为小写
		
		# map(dict_company_names)：映射字典键，输出字典值
		stocks["公司中文1"] = stocks["公司"].str.lower().map(dict_company_names)
		
				日期	公司	收盘	开盘	高		低		交易量	涨跌幅	公司中文1
		0	2019-10-03	BIDU	104.32	102.35	104.73	101.15	2.24	0.02	百度
		1	2019-10-02	BIDU	102.62	100.85	103.24	99.50	2.69	0.01	百度
		
		
		
		## Series.map(function)：function的参数是Series的每个元素的值

		# x.lower()：每一个数据大写该小写
		
		# dict_company_names[x.lower()]：字典取键，输出值
		
		# map(lambda x : dict_company_names[x.lower()])：输出字典值
		stocks["公司中文2"] = stocks["公司"].map(lambda x : dict_company_names[x.lower()])
		
		
	1.2 apply用于Series和DataFrame的转换，等价于 map()
	
		Series.apply(function), 函数的参数是每个值
		DataFrame.apply(function), 函数的参数是Series
		
		
		Series.apply(function):
		stocks["公司中文3"] = stocks["公司"].apply(lambda x : dict_company_names[x.lower()])
		
		DataFrame.apply(function)：
		# 注：函数的参数是Series，stocks.apply和x['公司']
		stocks["公司中文3"] = stocks.apply(lambda x : dict_company_names[x['公司'].lower()])
		
		注意这个代码：
		1、apply是在stocks这个DataFrame上调用；
		2、lambda x的x是一个Series，因为指定了axis=1所以Seires的key是列名，可以用x['公司']获取
		
	1.3 applymap用于DataFrame所有值的转换
	
	？	stocks[['收盘', '开盘', '高', '低', '交易量']].applymap(lambda x:int(x))
		
		stocks.loc[:,['收盘', '开盘', '高', '低', '交易量']]=stocks[['收盘', '开盘', '高', '低', '交易量']].applymap(lambda x:int(x))
		
		
九、pandas 对 excel的操作：
 
	1  explode实现一行变多行统计:
	  # 一个字段包含多个值,怎样将这个值拆分成多行，然后实现统计
		必须是字符串，再使用explode将一行拆分成多行，将按|分割字符串
	
		MovieID			Title										Genres
	0	1				Toy Story (1995)							Animation|Children's|Comedy
	1	2				Jumanji (1995)								Adventure|Children's|Fantasy
	2	3				Grumpier Old Men (1995)						Comedy|Romance
	3	4				Waiting to Exhale (1995)					Comedy|Drama
	4	5				Father of the Bride Part II (1995)			Comedy
	
	# 将分割后的列表添加到新列。
	df['GEN']=df['Genres'].str.split('|')
	MovieID		Title					Genres							GEN
	0	1	Toy Story (1995)	Animation|Children's|Comedy	[Animation, Children's, Comedy]
	1	2	Jumanji (1995)	Adventure|Children's|Fantasy	[Adventure, Children's, Fantasy]
	2	3	Grumpier Old Men (1995)	Comedy|Romance	[		Comedy, Romance]

	# 分割列表，一行变多行
	df_new = df.explode("GEN")
	
	MovieID	Title								Genres				GEN
	0	1	Toy Story (1995)	Animation|Children's|Comedy			Animation
	0	1	Toy Story (1995)	Animation|Children's|Comedy			Children's
	0	1	Toy Story (1995)	Animation|Children's|Comedy			Comedy
	1	2	Jumanji (1995)	Adventure|Children's|Fantasy			Adventure
	1	2	Jumanji (1995)	Adventure|Children's|Fantasy			Children's


	2 一列变多列：
	# 将数据项的一列变成多列数据
	
		学号	数据
	0	S001	怠涵:女:23:山东
	1	S002	婉清:女:25:河南
	2	S003	溪榕:女:23:湖北
	3	S004	漠涓:女:19:陕西
	4	S005	祈博:女:24:山东
	
	# x代表每一行字符串
	def fun_split_columns(x):
		# 元组解包，x['数据'].split(':')代表每一行字符串分割成元组，
		# 不需要写成x.str.split(':')
		x['姓名'],x['性别'],x['年龄'],x['地区']=x['数据'].split(':')
		return x
    # axis=1，横向，
	d=df.apply(fun_split_columns,axis=1)
	
	# 删除数列中多余的数据列
	d.drop(['数据'],axis=1,inplace=True)
	d.head(10)
	
		学号	姓名	性别	年龄	地区
	0	S001	怠涵	女		23		山东
	1	S002	婉清	女		25		河南
	2	S003	溪榕	女		23		湖北
	3	S004	漠涓	女		19		陕西
	4	S005	祈博	女		24		山东
	5	S006	孝冉	女		22		河南
	6	S007	乾名	女		22		湖北
	7	S008	炜然	女		21		陕西
	8	S009	晨阳	男		22		山东
	9	S010	轻涵	男		24		河南
	
	
	3. ①多列变一列：
		df=pd.DataFrame({'year':[2018,2018,2017,2017,2016,2016],'month':[1,2,3,4,5,6],'day':[11,12,13,1,23,15]})
			year	month	day
		0	2018	1		11
		1	2018	2		12
		2	2017	3		13
		3	2017	4		1
		4	2016	5		23
		5	2016	6		15
		
		# map(str)：将数值型转化为字符串，在拼接
		df['merge']=df['year'].map(str)+'/'+df['month'].map(str)+'/'+df['day'].map(str)
		df['merg']=df['year'].astype(str)+'/'+df['month'].astype(str)+'/'+df['day'].astype(str)
		# 取列标切片转化为列表
		lists=list(df.columns[0:3])
		# 去掉不需要的列标
		df.drop(lists,axis=1,inplace=True)
		# 打印结果
		df
				merge
		0	2018/1/11
		1	2018/2/12
		2	2017/3/13
		3	2017/4/1
		4	2016/5/23
		5	2016/6/15
		
	 ② 多列变一列在变成多行：
		df=pd.DataFrame({'year':[2018,2018,2017,2017,2016,2016],'month':[1,2,3,4,5,6],'day':[11,12,13,1,23,15],
		 'Supplier':['MURATA','AVX Corporation','AVX','RATA','Corporation','KEMET'],
		 'Supplier PN':['GRM1555C1H101JA01D',np.nan,'04025A3R9CAT2A','C0402C689C5GACTU',np.nan,'O9BN101'],
		'Supplier.2':[np.nan,'89C5G',np.nan,'Electronics','01JA01J','Murata']})
		
			year	month	day	Supplier	Supplier PN	           Supplier.2
		0	2018	1	11	MURATA	        GRM1555C1H101JA01D	     NaN
		1	2018	2	12	AVX Corporation	 NaN	                 89C5G
		2	2017	3	13	AVX	             04025A3R9CAT2A	          NaN
		3	2017	4	1	RATA	        C0402C689C5GACTU	    Electronics
		4	2016	5	23	Corporation	         NaN	             01JA01J
		5	2016	6	15	KEMET	            O9BN101	              Murata
		
		
		def merge_cols(x):
			x=x[x.notna()] 
			y=x.values
			s=[]
			for i in range(0,len(y)):
				if i==len(y)-1:
					s.append(f"{y[i]}")
					break

				else:
					 s.append(f"{y[i]}|")
			return  ''.join(s)  

		d=df.loc[:,'Supplier':]
		df['merge']=d.apply(merge_cols,axis=1)
		df
		
			Supplier	    Supplier PN	      Supplier.2	                 merge
		0	MURATA	      GRM1555C1H101JA01D	NaN	             MURATA|GRM1555C1H101JA01D
		1	AVX Corporation	   NaN	           89C5G	             AVX Corporation|89C5G
		2	AVX	            04025A3R9CAT2A	     NaN	               AVX|04025A3R9CAT2A
		3	RATA	C0402C689C5GACTU	  Electronics	   RATA|C0402C689C5GACTU|Electronics
		4	Corporation   	NaN	              01JA01J	         Corporation|01JA01J
		5	KEMET	         O9BN101	        Murata	          KEMET|O9BN101|Murata
		
		df['merg']=df['merge'].str.split('|')
		dg=df.explode('merg')
		dg.drop(['merge'],axis=1,inplace=True)
		
			year  month	day	Supplier	Supplier PN	Supplier.2	        merg
		0	2018	1	11	MURATA	GRM1555C1H101JA01D	NaN	           MURATA
		0	2018	1	11	MURATA	GRM1555C1H101JA01D	NaN	        GRM1555C1H101JA01D
		1	2018	2	12	AVX Corporation	NaN	89C5G	AVX            Corporation
		1	2018	2	12	AVX Corporation	NaN	89C5G	                  89C5G
		2	2017	3	13	AVX	04025A3R9CAT2A	NaN	                     AVX
		2	2017	3	13	AVX	04025A3R9CAT2A	NaN	                   04025A3R9CAT2A
		
	
	4 复杂多列到多行转换：
	'''
		首先是字符串类型；
						一行变多行，可以用explode实现；
														要使用explode，需要先将多列变成一列；
														注意有的列为空，需要做空值过滤；
	'''
	# 数据多行多列
	P/N	             Description     Supplier	  Supplier PN	Supplier.1	Supplier PN.1	
0 302-462  CAPCER0402 100pF5%     MURATA     GRM1555C1H101JA01D	YAGEO    CC0402JRNPO9BN101	
  -326	                   50V	
	
	# 取列标切片
	merge_name=list(df.columns[2:8].values) 
		['Supplier',
	 'Supplier PN',
	 'Supplier.1',
	 'Supplier PN.1',
	 'Supplier.2',
	 'Supplier PN.2']
	 
	 def merge_cols(x):
		"""
		x是一个行Series，把它们按分隔符合并
		"""
		# 删除为空的列
		x = x[x.notna()]
		# 使用x.values用于合并
		y = x.values
		# 合并后的列表，每个元素是"Supplier" + "Supplier PN"对
		result = []
		# range的步长为2，目的是每两列做合并
		for idx in range(0, len(y), 2):
			# 使用竖线作为"Supplier" + "Supplier PN"之间的分隔符
			result.append(f"{y[idx]}|{y[idx+1]}")
		# 将所有两两对，用#分割，返回一个大字符串
		return "#".join(result)

	# 添加新列，把待合并的所有列变成一个大字符串
	df["merge"] = df.loc[:, "Supplier":].apply(merge_cols, axis=1)
	
	# 把不用的列删除掉
	df.drop(merge_names, axis=1, inplace=True)
	
	P/N					Description			merge
0	302-462-326	CAP CER 0402 100pF 5% 50V	MURATA|GRM1555C1H101JA01D#YAGEO|CC0402JRNPO9BN...
1	302-462-012	CAP CER 0402 6.8pF 0.25pF 50V	AVX Corporation|04025A6R8CAT2A#KEMET|	

	#explode把一列变多行
	df["merge"] = df["merge"].str.split("#")
	df_explode = df.explode("merge")
		P/N	Description	merge
	0	302-462-326	CAP CER 0402 100pF 5% 50V	MURATA|GRM1555C1H101JA01D
	0	302-462-326	CAP CER 0402 100pF 5% 50V	YAGEO|CC0402JRNPO9BN101
	0	302-462-326	CAP CER 0402 100pF 5% 50V	GRM1555C1H101JA01J|Murata Electronics North Am...
	1	302-462-012	CAP CER 0402 6.8pF 0.25pF 50V	AVX Corporation|04025A6R8CAT2A
	1	302-462-012	CAP CER 0402 6.8pF 0.25pF 50V	KEMET|C0402C689C5GACTU
	2	302-462-009	CAP CER 0402 3.9pF 0.25pF 50V	AVX Corporation|04025A3R9CAT2A

	# 将一列还原成结果的多列
	df_explode["Supplier"]=df_explode["merge"].str.split("|").str[0]
	df_explode["Supplier PN"]=df_explode["merge"].str.split("|").str[1]
	# 把merge列删除掉，得到最终数据
	df_explode.drop("merge", axis=1, inplace=True)
		P/N	Description	Supplier	Supplier PN
	0	302-462-326	CAP CER 0402 100pF 5% 50V	MURATA	GRM1555C1H101JA01D
	0	302-462-326	CAP CER 0402 100pF 5% 50V	YAGEO	CC0402JRNPO9BN101
	0	302-462-326	CAP CER 0402 100pF 5% 50V	GRM1555C1H101JA01J	Murata Electronics North America
	1	302-462-012	CAP CER 0402 6.8pF 0.25pF 50V	AVX Corporation	04025A6R8CAT2A
	1	302-462-012	CAP CER 0402 6.8pF 0.25pF 50V	KEMET	C0402C689C5GACTU
	2	302-462-009	CAP CER 0402 3.9pF 0.25pF 50V	AVX Corporation	04025A3R9CAT2A
	
	df_explode.to_excel("./course_datas/c39_explode_to_manyrows/读者提供的数据-输出.xlsx", index=False)
	
	
	5 Pandas批量拆分Excel与合并Excel
	
	  1.1 将一个大Excel等份拆成多个Excel
		id	           title	                       tags
	0	2585	Tensorflow怎样接收变长列表特征	  python,tensorflow,特征工程
	1	2583	Pandas实现数据的合并concat	      pandas,python,数据分析
	2	2574	Pandas的Index索引有什么用途？	  pandas,python,数据分析
	‘’‘’‘’
	‘’‘’‘’
	
	df=pd.read_excel('crazyant_blog_articles_source.xlsx')
	
	# 获取总行数
	row_num=df.shape[0] 258
	
	# 将表格拆分成6份，每一份用下列名称命名文件，共6个文件，即将大表分成6份
	user_names = ["xiao_shuai", "xiao_wang", "xiao_ming", "xiao_lei", "xiao_bo", "xiao_hong"]
	# 如果不能均分，则总量+1，最后一个小文件少一行内容
	if row_num%len(user_names)!=0:
		row_num+=1
	# 注：分数一定要是整数 int()
	slices=int(row_num/len(user_names))
	slices     
	43 行
	
	# 将每一个文件下标对应其文件名，构成字典，便于取下标，得到文件名，
	s=[]
	l=[]
	for i ,j in enumerate(user_names):
		s.append(i)
		l.append(j)
	ds=dict(zip(s,l))
	{0: 'xiao_shuai',
	 1: 'xiao_wang',
	 2: 'xiao_ming',
	 3: 'xiao_lei',
	 4: 'xiao_bo',
	 5: 'xiao_hong'}
	
	# 共6次循环，一次取43行，iloc ():切片定位
	for i in range(0,6):
    new_sheet=df.iloc[i*slices:(i+1)*slices,:] new_sheet.to_excel(r'F:/python代码/数据分析/统计与计数/ant-learn-pandas-master/course_datas/c15_excel_split_merge/dir_split/'+ds[i]+'.xlsx',index=False)
	
	
		1.2 将一个大Excel不等份拆成多个Excel
	
	
	
		
		
		
		2.1 合并多个Excel表格：
		# 指定路径，切换路径
		fp=r'F:\python代码\数据分析\统计与计数\ant-learn-pandas-master\
		course_datas\c15_excel_split_merge\splits'
		os.chdir(fp)
		# 将遍历的文件名添加到列表中
		namelists=[]
		for name in os.listdir(fp):
			# 打开各个子文件
			data=pd.read_excel(name)
			# 各个子文件中加一个文件名
			data['source']=name.split('_')[-2]+name.split('_')[-1]
			# 子文件汇总列表
			namelists.append(data)
		
		# 拼接子文件
		f=pd.concat(namelists)
		# 保存并且命名总文件
		f.to_excel(fp+'\\002.xlsx',index=False) 
		# 总文件中查看子文件来源的个数
		f['source'].value_counts()
	
	
	
	6 Pandas实现Excel的vlookup并且在指定列后面输出:
	'''
			有两个excel，他们有相同的一个列；
		按照这个列合并成一个大的excel，即vlookup功能，要求：
		只需要第二个excel的少量的列，比如从40个列中挑选2个列
		新增的来自第二个excel的列需要放到第一个excel指定的列后面；
		将结果输出到一个新的excel.
	'''
		df_grades=pd.read_excel('学生成绩表.xlsx')
		df_grades_list=df_grades.columns.to_list()  ## 序列转化为列表
		print(df_grades_list)

		df_infos=pd.read_excel('学生信息表.xlsx')
		df_infos_list=df_infos.columns.to_list()
		print(df_infos_list)

		f=pd.merge(df_grades,df_infos,on='学号')
		lists=f.columns.to_list()
		print(lists)
		['班级', '学号', '语文成绩', '数学成绩', '英语成绩', '姓名', '性别', '年龄', '籍贯']
		list1=lists[5:]
		l=lists.index('学号')
		j=1
		for i in list1:
			x=lists.index(i)
			y=lists.pop(x)
			lists.insert(l+j,y)
			j+=1
		d=lists
		print(d)
		['班级', '学号', '姓名', '性别', '年龄', '籍贯', '语文成绩', '数学成绩', '英语成绩']
		# 重置列表名：
		g=f.reindex(columns=d)
		print(g.head())
		  班级     学号  姓名  性别  年龄  籍贯  语文成绩  数学成绩  英语成绩
		0  C01    S001    怠涵   女    23  山东        99        84        88
		1  C01    S002    婉清   女    25  河南        66        95        77
		2  C01    S003    溪榕   女    23  湖北        68        68        61
		3  C01    S004    漠涓   女    19  陕西        63        66        82
		4  C01    S005    祈博   女    24  山东        72        95        94
		
	7 Excel数据输出到另一个Excel中：
		df = pd.read_csv('new.csv')

		with open('label.csv', 'r') as f:
			content = f.read()
			cols = content.split(',')
			df.columns = cols

		with open('original_feature_name.csv', 'r') as f:
			content = f.read()
			rows = content.split('\n')
			# 因为长度不一样 做处理:
			if df.values.shape[0] < len(rows):
				rows = rows[:df.values.shape[0]]
			df.insert(0, 'original_feature_name', rows)
	
	
十、style格式：
	1. 针对元素和整行整列：
	import pandas as pd
	import numpy as np
	np.random.seed(24)
	df=pd.DataFrame({'A':np.linspace(1,10,10)})
	df=pd.concat([df,pd.DataFrame(np.random.randn(10,4),columns=list('BCDE'))],
				axis=1)
	
		A	B	C	D	E
	0	1.0	1.329212	-0.770033	-0.316280	-0.990810
	1	2.0	-1.070816	-1.438713	0.564417	0.295722
	‘’‘’‘’‘’‘
	
	df.loc[0,'B']=np.nan  # 给特定值设为空值
	
		A	B	          C        	D	       E
	0	1.0	NaN	      -0.770033	 -0.316280	-0.990810
	1	2.0	-1.070816 -1.438713	 0.564417	0.295722
	
	def red_num(x):
		color='red' if x<0 else 'blue'
		return  f'color:{color}'                     # 等价 'color:%s'%color 
    # applymap:将函数做用于DataFrame中的所有元素(elements)
	def col_row(x):
		return ['background-color:yellow' if s==x.max() else '' for s in x]

		s=df.style.applymap(red_num,subset=['B','C']).apply(col_row,subset=['D','E'],axis=0)
		
	
	# 改变颜色：
		A	B	          C	           D	     E
	0	1	nan	       -0.770033	-0.31628	-0.99081
	1	2	-1.07082	-1.43871	0.564417	0.295722
	''''''''
	
	2. 数据格式:
		# 整体数据：
		df.style.format("{:0.2f}")              
		A		B		  C		D	      E
	0	1.00	nan		-0.77	-0.32	-0.99
	1	2.00	-1.07	-1.44	0.56	0.30
	
		# 部分数据：
		df[1:3,'B':'D'].style.format("{:0.1f}") # 部分数据
		
		B	    C	    D
	1	-1.1	-1.4	0.6
	2	-1.6	0.2	    0.7
	3	1.0	    0.1	   -0.5

		# 不同列数据不同格式化输出：
		style = {'B': "{:0.2%}",
                 'C': '{:+.2f}'}
		df.style.format("{:0.2f}")
		
		
		
		
		
		
		
		
		
		
	