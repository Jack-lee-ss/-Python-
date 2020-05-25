import numpy
#创建一维数组,注意：创建文件名称不能是 numpy.py 否则无法调用 numpy函数
x=numpy.array(['1','5','4'])
i=max(x)
j=x.sort()
print(x[2])
print(j)
print(i)

##创建二维数组
y=numpy.array([["a","b","c"],[1,2,3],["你好""数字""文化"]])
print(y[1][2])

import pandas as pda
# Series(左侧为索引，从0开始，右边为创建的数据) DataFrame
a=pda.Series([8,9,2,1])
print(a)
## 创建索引
b=pda.Series([8,3,6,7],index=["a","b","c","d"])
print(b)
## 自带索引的数据框
c=pda.DataFrame([[5,6,2,3],[3,5,8,1],[6,4,3,9]])
print(c)
## 创建列号
d=pda.DataFrame([[5,6,2,3],[3,5,8,1],[6,4,3,9]],columns=["one","two","three","four"])
print(d)
## 字典创建数组，数值不够自动填充。
e=pda.DataFrame({"one":4,"two":[6,3,7],"three":list(str(123))})
print(e)
## d.head():取d数组的头部数据，前五行，默认，不够则全部取出，也可以指定取几行
f=d.head()
print(f)
g=d.head(2)
print(g)
## d.tail():取尾部数据，默认后五行
## d.describe() 展示数据每一列的信息
h=d.describe()
print(h)
### 数据转置 d.T 行列转置
j=d.T
print(j)
#===============================================================

### 导入数据

#导入CSV文件
#import pandas as pda
#a=pda.read_csv("F:/Java课程代码/pycharm.py文稿/数据分析/DEMO-4-思考题-根据部门列创建工作表.csv")
#b=a.describe()
#print(b)

#导入Excel
#import pandas as pda
#a=pda.read_excel("F:/Java 课程代码/pycharm.py 文稿/数据分析/DEMO-4-思考题-根据部门列创建工作表.xls")
#b=a.describe()
#print(b)
#a=pda.read_html("https://book.douban.com")
#print(a)

## 导入文本数据时注意另存为 utf-8
import pandas as pda
a= pda.read_table("D:/data/cbac.txt")
print(a)

#================== numpy 多维数组对象 ==================
import numpy as np
a=np.random.randn(2,3)
print(a.shape)



