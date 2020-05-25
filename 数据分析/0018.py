### ================== 正则表达式② ============================
# -*- coding: UTF-8 -*-
import re
## 匹配有效数字(含0的有小数的有正负的数字)
s='3.1415936'
i='^[+-]?(\d|([1-9]\d+))(\.\d+)?$'
r=re.match(i,s)
print(r.group())
### 验证密码：数字、字母、下划线 6-16位数字
r=re.match('^\w{6,16}$','124_gd456')
print(r.group())
### 验证汉字，如姓名：尼古拉斯·赵四  \u4E00:中文第一个汉字编码；\u8FA5:最后一个汉字编码
r=re.match('^[\u4E00-\u8FA5]+(·[\u4E00-\u8FA5]+)?$','尼')
print(r.group())
## 汉语名字最少两个字
r=re.match('[\u4E00-\u8FA5]{2,10}(·[\u4E00-\u8FA5]{2,10})?$','尼古拉斯·赵四')
print(r.group())
## 验证邮箱
s='lcq21-3h.jg_f2_g.9-678@zhufeng-office.cmp_gbk-frg.ner.com'
i='^[0-9a-zA-Z]+((-\w+)|(\.\w+))*@[0-9a-zA-Z]+((-\w+)|(\.\w+))*\.\w+$'
r=re.match(i,s)
print(r.group())

## 验证身份证号码:分组捕获详细信息
s='342427199006048971'
i='^(\d{6})(\d{4})(\d{2})(\d{2})(\d{2})(\d)(\d|X)$'
r=re.match(i,s).group()
print(r)
## 打印\需要添加转义符\,在字符串或者规则中都需要.写两个\
r=re.match(r'\\','\\').group()
print(r)
r=re.match(r'\d+','8').group()
print(r)
r=re.match(r'\d+','8909').group()
print(r)
### 注：r'\\d+':错误表达。程序会认为 \\转义为\ d+没有自带的\,报错，只有自带的\d:才会有含义。所以 r'\\\d'：可以转义为 \\d+ 带有\的数字 如：\89, 当然目标数据也需要加\\转义成\才能匹配上。
#r=re.match(r'\\d+','\8909').group()
#print(r)
# r=re.match(r'\\d+','\8909').group()
# print(r)
r=re.match(r'\\\d+','\\8909').group()
print(r)
r=re.match(r'\\\\\d+','\\\\8909').group()
print(r)
r=re.match(r'\\\\\\\d+','\\\\\\8909').group()
print(r)
#### 综上：要输出带有斜杠的字符串，规则里的斜杠数加上标识符自带的斜杠数是奇数（即总斜杠数是奇数），目标字符串的斜杠数=总斜杠数-1，即为偶数，因为，程序会默认规则里除了自带一个斜杠，剩下偶数个斜杠数可以两两转义成一个斜杠，即偶数个斜杠自减一半成奇数个斜杠，该奇数个斜杠即为打印出的斜杠数。和斜杠位置无关。
r=re.match(r'\d+\\\\','8909\\\\').group()
print(r)

### 注意：findall()提取所有符合条件的信息的列表。
r=re.findall(r'\d+','zhufeng123zhu345feng875')
print(r)
## search():提取第一个符合条件的字符串
r=re.search(r'\d+','zhufeng123zhu345feng875').group()
print(r)
print('------------------------','\n')

s='abc##qwe###jklllll1232222bcd####abcccc3440123324'
reg='(.)\\1+'
r=re.split (reg,s)
print(r,'\n')
print('==========================================','\n')
#######  多行匹配 re.MULTILINE
s="""
001 苹果 75
002 香蕉 34
003 栗子 24
"""
i='^\d+'
r=re.compile(i,re.MULTILINE)
for a in r.findall(s):
	print(a,'\n')
i='\D+'
r=re.compile(i,re.MULTILINE)
for a in r.findall(s):
	print(a.strip(),'\n')


print('==========================================')

s='<br>◎主　　演　伍迪·哈里森 Woody Harrelson<br>&nbsp;&nbsp;　帕特里克·威尔森 Patrick Wilson<br>&nbsp;&nbsp;　卢克·伊万斯 Luke Evans<br>&nbsp;&nbsp;　艾德·斯克林 Ed Skrein<br>&nbsp;&nbsp;　丹尼斯·奎德 DennisQuaid<br>&nbsp;&nbsp;　曼迪·摩尔 Mandy Moore<br>&nbsp;&nbsp;　亚历山大·路德韦格 Alexander Ludwig<br>&nbsp;&nbsp;　艾伦·艾克哈特 Aaron Eckhart<br>&nbsp;&nbsp;　达伦·克里斯 Darren Criss<br>'
r=re.split(r'<br>',s)
#print(r)
i=''.join(r).strip().replace('&nbsp;&nbsp;','')
#print(i)
a=re.search(r'(◎主　　演)(.*)',i).group(2)
# print(a.strip(),'\n')
# print('-----------------------------')


s='''<br>◎译　　名　决X中途岛/中途岛战役/中途岛海战<br>◎片　　名　中间的way<br>◎年　　代　2019<br>◎产　　地　中国/美国<br>◎类　　别　战争/历史<br>◎语　　言　<strong><font color="Red">英语</font></strong><br>◎字　　幕　中文字幕<br>◎IMDb评分&nbsp;&nbsp;6.9/10 from 12377 用户<br>◎文件格式　X264 + AC3<br>◎视频尺寸　1920 x 798<br>◎文件大小　3 GiB<br>◎片　　长　138 Mins<br>◎导　　演　罗兰·艾默里奇 Roland Emmerich<br>◎主　　演　伍迪·哈里森 Woody Harrelson<br>&nbsp;&nbsp;　帕特里克·威尔森 Patrick Wilson<br>&nbsp;&nbsp;　卢克·伊万斯 Luke Evans<br>&nbsp;&nbsp;　艾德·斯克林 Ed Skrein<br>&nbsp;&nbsp;　丹尼斯·奎德 DennisQuaid<br>&nbsp;&nbsp;　曼迪·摩尔 Mandy Moore<br>&nbsp;&nbsp;　亚历山大·路德韦格 Alexander Ludwig<br>&nbsp;&nbsp;　艾伦·艾克哈特 Aaron Eckhart<br>&nbsp;&nbsp;　达伦·克里斯 Darren Criss<br>

'''
# r=re.split(r'<br>',s)
#
# a=''.join(r).strip().replace('&nbsp;&nbsp;','')
# print(a)
# print('==============','\n')
# i=re.search(r'(.*◎主　　演)(.*)',a).group(2)
# print(i.strip())

######  常见模式修正符：
## I : 匹配时忽略大小写
a='Python'
b='pyt'
r=re.search(b,a,re.I)
print(r.group())

## M：多行匹配
a="""
101 苹果 75
302 香蕉 34
503 栗子 24
"""
b='\d+$'
## findall 返回字符串,由于遍历列表，输出字符串
r=re.compile(b,re.M)
for i in r.findall(a):
	print(i)
print(type(i),'\n')

## findall 返回列表
r=re.compile(b,re.M).findall(a)
print(type(r))
print(r)



### S:让 . 匹配包括换行符
	






