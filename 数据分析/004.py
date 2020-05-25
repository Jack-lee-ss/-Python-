## ===========  python 数据结构 ================
## 元组，列表，字典，集合等概念和常用方法


##----------------  元组 ----------------------

tup= 4,5,6      # 元组长度固定不可变，小括号
print(tup)

tup = (1,2,3),(4,5,6)  # 生成元素是元组的元组
print(tup)

i=tuple([1,2,3]) # tuple函数将任意序列转化为元组
print(i)

j=tuple('string') # 将字符串变成元组并且获取任意字符（数组型）
print(j)
print(j[2])

tup=tuple([1,[1,2],3]) ## 元组可以添加不能修改原数据
tup[1].append(4)   ## 在元组中添加元素 在第二个位置上添加数字，置后。
print(tup)

tup=(1,2)+('string',[1,3]) ## 元组可以通过 + 连接形成新的元组
print(tup)

tup=(1,3)*3 ## 将原来的元组复制成几个相同的元组连在一起
print(tup)

#----------------------  元组拆包-----------------
tup=1,2,3
a,b,c=tup ## 将元组表达式赋给变量，可以获得对应值
print(a)  # a=1  b=2  c=3

tup=3,4,(5,6) #复合嵌套也可以拆包
a,b,c=tup
print(a,b,c)

seq=[(1,2),(3,4),(5,6)]  ## 遍历序列中元组和列表，对应关系
for a,b in seq:
	print('a={0},b={1}'.format(a,b,c))


i= 'a',2,3,4,'string' # 高级拆包：获取任意序列列表
#a,b,*rest=i a=a b=2 *rest 或者 *_ 表示不重要数据
a,b,*_=i
print(a,b)

i=1,2,3,4,2,2
print(i.count(2)) ## 统计 2 在序列中出现次数

#============================================================


## ----------------------- 列表--------------------------
listx=[1,2,3,'string',None] ## 类型是 列表 不能用list做变量，否则和自带函数名重名
print(list)

a=(1,2,3)
a_list= list(a) ## 元组化为列表
print(a_list)

b_list=[2,4,5]
b_list[1]='string'  ## 改变内容，注意：列表函数用[]，元组函数用（）表示
print(b_list)

i=range(0,10)
print(list(i)) ## 将生成器转化为列表

a=[1,2,3,'string']
a.append(4)  ## 注意：列表添加元素后，应该输出原表名，原表名发生改变
print(a)
a.insert(2,'book') # 将元素插入到指定位置
print(a)
a.pop(1) ## 将该位置数值移除并且返回剩下的序列
print(a)
a.append('book')
a.remove('book') ## 移除第一个符合条件值
print(a)

a_list=[1,2,3]+['a','b'] ## 连接表 效率慢，需要重新创建新表
print(a_list)

b_list=[1,2,3]
b_list.extend([1,5,(3,5),'string']) # 添加元素，效率高
print(b_list)

a=[1,2,7,4,5]
a.sort() ## 数字类型才可以相互比较大小
print(a)

b=['key','howe','likiek','ad','he']
b.sort(key=len) ## 根据字符串长度排序
print(b)

### 二分搜索和排序表维护
import bisect
a=[1,2,2,3,4,8]
b=bisect.bisect(a,6) ## 返回 a 列表中 5 应该按顺序排列的位置
print(b) # 输出 5 即应该排在 a 表中数组第五位
bisect.insort(a,7) ##将7排在a列表的第五位
print(a)

## 切片使用：对序列起始位值进行选取其子集 初位置 一直小于 末位置

seq=[1,3,5,7,4,10]
i=seq[1:3] ## 数组形式，第二位到第四位，元素数量=末-初（3-1）=2，初位置包含，但末位置不包含。
print(i) ## 3-1=2 两个元素，从 第二位3开始，7 末位置不包含，3,5
seq[2:4]=[22,55,44,66]## 将序列复制给变量，将seq[2:4]中第2,3项改成[22,55,44,66]
print(seq)
print(seq[:3])## 省略初始位置，默认从初末开始
print(seq[2:])
print(seq[-2:]) ## 从尾部索引后两位到末位置
print(seq[-3:-1]) ## 注意初位置始终小于末位置，截取中间两个字符，且末位置是-1位，往前再数一位，共两位
print(seq[::2]) ## 序列从第一位每各2为取一个数字
print(seq[::-1]) ## 倒序排列
print(seq[::-3]) ## 倒序排列，每隔3位取一个数

## 内建序列的使用

##==================== 字典 ===========================
# 字典是Python数据结构中最重要的。哈希表或者关联数组，拥有键值对，{}是创建字典的方式。逗号将其分开。
a_dict={'a':1,'b':'string'} ## '':代表字符串 a:键；b:值
print(a_dict)
a_dict[5]=(1,2,3) ## 添加一个键值对 [5]:代表键，而不是数组中的下标
print(a_dict)
print(a_dict['a']) ## 访问其中的一个键对应的值
print('b'in a_dict) ## 确定dict中是否存在某一个键。

del a_dict['a'] ## 删除一个键和其对应的值
print(a_dict)

i=a_dict.pop(5) ## pop 删除的同时会返回被删除键对应的值，并删除键
print(i)

b_dict={5:(1,2,3),'t':[1,4,'string'],(3,7):[4,6,'book']}
i=list(b_dict.keys()) ## 提取关键字，即提取键，并将其存放于列表中
print(i)
j=list(b_dict.values()) ## 提取值存放于列表中。
print(j)
k=tuple(b_dict.values()) ## 提取值存放于元组中
print(k)

a_dict.update(b_dict) ## 将两个字典合并，并且覆盖已存在的键和值。
print(a_dict)

### 从序列中生成字典
i=dict(zip(range(4),reversed(range(4)))) ## 两个序列在字典中配对
print(i)

## 哈希化：字典键必须是不可变
# 用元组作为键，元组内部必须可以哈希化，
d={}
d[tuple([1,2,3])]=4 ## [] ()要间隔表示，元组不可变可以作为键，列表是可以变化的所以需要转化为元组装入字典中作为键。
print(d)

## 默认值

##===================== 集合========================
# 集合是一种无序但元素唯一的容器，想字典，有键无值，两种创建方式，大括号
i=set([1, 2, 3]) ## set 函数创建 集合大括号
print(i)
print({'s',2,3,4,5,4,5}) ## 直接输出，覆盖相同元素，从小到大排列

## 集合支持数学上的集合操作
a={1,2,3}
b={'a',6,'bf',3}
i=a.union(b) ## 并集 覆盖相同元素
print(i)
j=a|b  ## 并集，二元操作符
print(j)

k=a.intersection(b) ## 交集
print(k)
l=a&b  ## 交集
print(l)
## 集合元素是不变的，要包含列表型元素，先转化为元组型
d_list=[1,2,3,'s']
d_set={tuple(d_list)} ## 列表元素转化为元组元素
print(d_set)
i={1,2}.issubset(d_list) ## {1,2}是否包含于 d_list
print(i)
j={1,2,4}=={2,4,1} # 内容都一样才相等，返回布尔值
print(j)

#============= 列表，字典，集合的推导式=======================
# 列表推导式：[表达式 for 值 in 列表中 if 条件]
# 集合推导式：{表达式 for 值 in 列表中 if 条件}
a=['a','ab','abc','abcd']
i=[x.upper() for x in a if len(x)>1] ##将字符串长度大于2改大写
print(i)
j=[len(x) for x in a ] ## 遍历字符串长度
print(j)
k={x.upper() for x in a if len(x)>1} ## 改为大括号
print(k)

## 嵌套列表推导式 = for 循环的嵌套，从大循环到小循环
a=[['ab','ac','ad'],['ae','be','ee']] ## 获得含两个e的字符
b=[i for i_s in a for i in i_s if i.count('e')>1]
print(b)

### 将元组列表变成简单列表
a=[(1,2,3),(4,5,6),(7,8,9)]
b=[i for i_s in a for i in i_s ]
print(b)

## 列表推导式中的列表推导式
a=[[i for i in i_s] for i_s in a] #元组列表变成列表元素的列表
print(a)





