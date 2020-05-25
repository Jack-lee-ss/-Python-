# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-

'''
# import pandas as pd
# import pandas_profiling
# df=pd.read_csv(r'F:\python代码\数据分析\统计与计数\ant-learn-pandas-master\datas\heart\heart.csv')
# print(pandas_profiling.ProfileReport(df))

读取pdf文件
import os
from pdfdocx import read_pdf
os.chdir(r'F:\python代码\数据分析\pdf\test')
pdf=read_pdf('ts1234.pdf')
print(type(pdf))   # 字符串


# 读取doc文件
import os
from pdfdocx import read_docx
import docx
os.chdir(r'F:\python代码\数据分析\pdf\test')
doc=read_docx(r'F:\python代码\数据分析\pdf\\test\测量软件显示及校正解决.doc')
print(type(doc))
print(doc)

# 读取doc文件
import os
from pdfdocx import read_docx
from  docx import Document
os.chdir(r'F:\python代码\数据分析\pdf\test')
#doc=read_docx(r'F:\python代码\数据分析\pdf\\test\测量软件显示及校正解决.doc')
doc=Document('《大河之源——史前美术和古埃及美术》教案.docx')
for i in doc.paragraphs:
	print(i.text)

'''
