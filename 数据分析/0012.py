### ===================高阶pandas===============================
import numpy as np
import pandas as pd
values=pd.Series(['apple','orange','apple','apple']*2)
#print(values)
# 获取序列中的唯一值，即为不重复值
print(pd.unique(values))
# 输出重复值的个数
print(pd.value_counts(values))
print('-------'*10)
# 分类和字典编码的展现
values=pd.Series([0,1,0,0]*2)
dim=pd.Series(['apple','orange'])
# 将根据values值对应dim的值，定义特定的序号
print(dim.take(values))
print('-------'*10)

## Categorical类型：承载整数的类别展示和编码的数据
fruits=['apple','orange','apple','apple']*2
N=len(fruits)
# random.uniform(x, y) 方法将随机生成一个实数 不包括y
df=pd.DataFrame({'fruit':fruits,'basket_id':np.arange(N),'count':np.random.randint(3,15,size=N),'weight':np.random.uniform(0,4,size=N)},columns=['basket_id','fruit','count','weight'])
#print(df)
# df['fruit'] 是python字符串对象组成的数组，调用函数将其转化为Categorical对象。
fruit_cat=df['fruit'].astype('category')
#print(fruit_cat)

# Categorical对象拥有categories和codes属性
#print(type(fruit_cat.values))
# print(fruit_cat.values.categories)
# print(fruit_cat.values.codes)

# 直接生成pandas.categorical，获得分类项和不重复的个数
a=pd.Categorical(['foo','bar','baz','foo','bar'])
# print(a)

# 从数据源获得分类编码数据，使用from_codes构造函数
a=['foo','bar','baz']
b=[0,1,2,2,0,0]
c=pd.Categorical.from_codes(b,a)
#print(c)

# 将数据排序 ordered=True, as_ordered
d=pd.Categorical.from_codes(b,a,ordered=True)
#print(d)

# 效果同上
#print(c.as_ordered())








