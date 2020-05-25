###### 数据清洗  缺失值（通过describe与len,通过0数据）与异常值处理（散点图）。处理方式：删除，插补，不处理。
from numpy import nan as NA
import pandas as pda
string_data=pda.Series(['avd','dgd','nan','ert'])
print(string_data)
print(string_data.isnull()) ## 返回哪些值是缺失的值得布尔值，false:代表不缺失

### 过滤缺失值
from numpy import nan as NA
import pandas as pda
i=pda.Series([1,NA,3.5,NA,5.7])
print(i.dropna()) #### Series中使用dropna 可以返回其所有的非空数据及其索引值 i.dropna 等价 i.notnull notnull:代表返回非缺失值。

### dropna 处理 dataframe时，会默认删除所有包含缺失值得行
import pandas as pda
from numpy import nan as NA
a=pda.DataFrame([[1,2,3],[1,4,NA],[NA,NA,NA]])
print(a.dropna()) ### 只保留不含na的一行
print(a.dropna(how='all')) ### 删除所有值均为NA的行
a[4]=NA ## 再添加一个NAN列作为第四列
print(a)
print(a.dropna(axis=1,how='all')) ## 删除全是NAN的一列



