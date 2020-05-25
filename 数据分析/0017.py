##### =========== 正则表达式① ==================
import re
#
# print('-------------------------------.\....')
# a=re.match('1','1fna')
# print(a)
# a=re.match('.','i')
# print(a)
# a=re.match('.','ifdssfs')
# print(a)
# a=re.match('...','advc')
# print(a)
# print('-----------------------------\d\D')
# ## 没有匹配到字符 None
# ## \d 匹配数字
# a=re.match('\d','a')
# print(a)
# a=re.match('\D','d')
# print(a)
# print('----------------------------\s\S')
# ## \s:匹配空白（空格，tab键，制表符）
# # 首字母不是空白符，找不到
# a=re.match('\s','a b')
# print(a)
# # 首字母是空白键
# a=re.match('\s',' b')
# print(a)
# # 首字母是\t
# a=re.match('\s','\tb')
# print(a)
# # 首字母是制表符
# a=re.match('\s','\nb')
# print(a)
# # 匹配非空白，非制表符，非\t
# a=re.match('\S',' b')
# print(a)
# print('------------------------------\w\W')
# ## \w 匹配单词字符，即a-z,A-Z,0-9._
# # 首字母是\n 无法匹配
# a=re.match('\w','\na')
# print(a)
# a=re.match('\w','-a')
# print(a)
# a=re.match('\w','la')
# print(a)
# ## \W:匹配非单词字母
# a=re.match('\W','fa')
# print(a)
# ## 一一对应匹配，错误一个则终止
# a=re.match('\w\W','na')
# print(a)
# a=re.match('\w\w','na3')
# print(a)
# a=re.match('\w\W','fna')
# print(a)
# print('--------------------------[]')
# ####[]:匹配【】中列举的任意字符
# a=re.match('1[2345]','16')
# print(a)
# ### ^:取反
# a=re.match('1[^2345]','16a')
# print(a)
# ## a-z:范围值，4-8范围值
# a=re.match('1[a-z4-8]','12')
# print(a)
# ## 取反范围
# a=re.match('1[^a-z4-8]','12')
# print(a)
# ##### 取反总结：\d==[0-9],\D==[^0-9];\w==[a-zA-Z0-9_],\W==[^a-zA-Z0-9_]
# print('=======================================================')
# #### 表示数量
# ## *:匹配前一个字符出现0次或者无限次  \d*:\d和*合起来解释：*前的\d(数字)出现0次或者多次。
# # 出现数字0次，匹配到空字符
# print('--------------------------------\.')
# a=re.match('\d*','')
# print(a)
# # 数字出现多次
# a=re.match('\d*','123')
# print(a)
# # 只匹配到第一个数字1结束
# a=re.match('\d*','1a2b')
# print(a)
# # 第一个非数字，"a1234"=="""a1234";字符前有一个空字符，所以匹配到空字符
# a=re.match('\d*','a1234')
# print(a)
# # 任意的非数字作为首字母，同上。
# a=re.match('\d*','_a1234')
# print(a)
# print('---------------------------------------------\+')
# ### \+:匹配前一个字符出现1次或者无限次，即至少一次。
# ## 由于首字母非数字，默认匹配到0次，与至少一次相违背，无法匹配
# a=re.match('\d+','_a1234')
# print(a)
# a=re.match('\d+','1234')
# print(a)
# a=re.match('\d+','1234asdf')
# print(a)
# print('----------------------------------\?')
# ### \?:匹配前一个字符出现1次或者0次 [0-1]----最多一次。
# a=re.match('\d?','1ascd')
# print(a)
# # 无数字，匹配到空字符
# a=re.match('\d?','ascd')
# print(a)
# # 只匹配第一个字符
# a=re.match('\d?','1234adf')
# print(a)
# # 第一个字符符合，第二个字符不是[a-z],不匹配，所以综合匹配不到。
# a=re.match('\d?[a-z]','123afvg')
# print(a)
# # [a-z]:指范围内一个字符
# a=re.match('\d*[a-z]','123afvg')
# print(a)
# # 首字母无数字，默认空字符；第二个字母是 [a-z]范围内一个字符
# a=re.match('\d*[a-z]','afvg')
# print(a)
# # 首字母是字母，不是至少一次数字，匹配不到。
# a=re.match('\d+[a-z]','afvg')
# print(a)
# # \d+:至少出现一次数字，1234符合，a符合[a-z]范围。
# a=re.match('\d+[a-z]','1234afvg')
# print(a)
#
# print('------------------------------------------------{}')
# #### \{m}:匹配前一个字符出现m次
# # 数字出现4次
# a=re.match('\d{4}[a-z]','1234dggh')
# print(a)
# # 字符出现4次
# a=re.match('\d{4}[a-z]{4}','1234dggh')
# print(a)
# # 数字部分匹配不正确，终止代码，结果是无法匹配
# a=re.match('\d{3}[a-z]','1234dggh')
# print(a)
# # 数字部分匹配正确，打印出来；字母部分位数不对，所以只打印出数字+正确字母部分
# a=re.match('\d{4}[a-z]{3}','1234dggh')
# print(a)
# # 字母部分多一位，而数据没有。
# a=re.match('\d{4}[a-z]{5}','1234dggh')
# print(a)
# # 数字位数多一位，
# a=re.match('\d{5}[a-z]','1234dggh')
# print(a)
# ### 位数过多或者过少，都无法匹配，返回None
#
# print('-----------------------------------------\,')
# #### \d,至少d次。
# a=re.match('\d{2,}[a-z]','1234dggh')
# print(a)
# ## 要么0或者1次
# a=re.match('\d{0,1}[a-z]','1234dggh')
# print(a)
# ## 数字出现1到3次
# a=re.match('\d{1,3}[a-z]','1234dggh')
# print(a)
# ## 数字出现2到5次
# a=re.match('\d{2,5}[a-z]','1234dggh')
# print(a)
# ###### 手机号匹配
# a=re.match('1[235678]\d{9}','17859727671')
# print(a)
# a=re.match('1[235678]\d{9}','17859727671adgg')
# print(a)
#
# print('-----------------转移字符串------------')
# ## 换行符
# s='\nabc'
# print(s)
# ## 保留\n 转义字符
# s='\\nabc'
# print(s)
# a=re.match('\\\\nabc','\\nabc')
# print(a)
# ## 原生字符串表示
# a=re.match(r'\\nabc','\\nabc')
# print(a)
# print('\n')
# print('======================== 边界性==========================')
# ## ^ $:匹配一个字符串的开始和结尾
# ## 手机号匹配
# a=re.match('^1[235678]\d{9}$','17459827462')
# print(a)
# a=re.match('^1[235678]\d{9}$','17459827462adc')
# print(a)
#
# ### \b:匹配一个单词的边界；\B：匹配非单词边界
# a=re.match(r'\w+ve','hover')
# print(a)
# # 未到边界
# a=re.match(r'\w+ve\b','hover')
# print(a)
# # 未到边界
# a=re.match(r'\w+\bve\b','hover')
# print(a)
# # 空格不是边界，未到边界，加上空格到边界。
# a=re.match(r'\w+ve\b','ho ver')
# print(a)
# # 加上空格到边界
# a=re.match(r'\w+\s\bve','ho ver')
# print(a)
# a=re.match(r'\w+\s\bve\s\b\w','ho ve r')
# print(a)
# a=re.match(r'\w+\s\bve\b\w','ho ve r')
# print(a)
# print('--------------------------------\B')
# ### \B：匹配非单词边界
# ## ve前是空格符，是边界，无法匹配
# a=re.match('^.+ve\B','ho ve r')
# print(a)
#
# ## ve后是字符r,不是边界，可以匹配
# a=re.match('^.+ve\B','ho ver')
# print(a)
# a=re.match('^.+\Bve\B','hover')
# print(a)
# a=re.match('^.+','ho ve r')
# print(a,'\n')
# print('===========匹配分组==============')
# ### 匹配0-100以内数字
# a=re.match('[1-9]?\d$|100$','100')
# print(a)
# ### 网页提取文本
# a=re.match(r'<h1>(.*)</h1>','<h1>匹配分组</h1>')
# print(a)
# ## a.group():返回匹配值（包含非文本内容）
# print(a.group())
# ## 例子中只有一个文本，a.group(1)：代表（）中第一个文本内容
# print(a.group(1))
# a=re.match(r'(<h1>).*(</h1>)','<h1>匹配分组</h1>')
# # 返回第一个（）中内容
# print(a.group(1))
# # 返回第一个（）中内容
# print(a.groups()[0])
# # 返回第二个（）中内容
# print(a.group(2))
# # 返回第二个（）中内容
# print(a.groups()[1])
# ###### 注意group(1)和group()s[1]区别。
#
# ### 多个标签重叠取文本,注意格式
# ## 两种方式提取
# ##直接提取
# s='<html><h1>abcd</h1></html>'
# a=re.match(r'<.+><.+>.+</.+></.+>',s)
# print(a)
# ### 分组提取
# ## （ab）:将括号中字符串作为一个分组，后面可以提取
# ##  \num: 引用分组num匹配到的字符串;最外层为第一组，记为\1,放置匹配规则尾部；第二层是第二组，记为\2.
# a=re.match(r'<(.+)><(.+)>.+<(/\2)><(/\1)>',s)
# print(a)
# print(a.group())
#
# ### 邮箱匹配
# ## 邮箱域名的点. 要加\. 转移符，防止被误认为是字符
# s=r'(\w+)@(163|qq|126|gmail|)\.(com|cn|net)'
# a=re.match(s,'1123435@qq.com')
# print(a)
# print(a.group())
# print(a.group(1))
# print(a.group(2))
#
# ### 当标签过多时，需要给标签从外到内起名，便于引用。
# ## ?P<name>:分组起名；?P=name:引用别名为name分组匹配到中的字符串
# s='<html><h1><a>abcd</a></h1></html>'
# i=r'<(?P<k1>.+)><(?P<k2>.+)>.+</(?P=k2)></(?P=k1)>'
# a=re.match(i,s)
# print(a)
# print(a.group(),'\n')
# print('---------------search 用法----------')
#
# ############# search 用法-------只寻找特定文本，并非从字符串开始进行
# ### 只匹配特定文本
# s='<html><h1><a>abcd</a></h1></html>'
# a=re.search(r'abcd',s)
# print(a)
# s='abcd<a><h1></h1></a>'
# a=re.search(r'abcd',s)
# print(a)
#
# s='abcd<a><h1>abcd<a><h1>'
# a=re.search(r'abcd',s)
# ### search()找到第一个符合规则的内容就不在往后检查了
# print(a.group())
#
# ### findall():找出所有符合规则的内容
# s='abd<a><h1>abd<a><h1>'
# ## 返回列表
# a=re.findall(r'abd',s)
# print(a)
# print(a[1])
#
# ### sub():将匹配的数据进行替换
# print('--------------------sub()替换','\n')
# ## sub():第二个参数，替换第一个参数，第三个参数是目标对象
# a=re.sub(r'php','python','python php why php what')
# print(a)
#
# ### 将数值替换后输出，第二参数可以定义函数
# def replace(i):
# 	print(i.group())
# 	r=int(i.group())+20
# 	return str(r)
# s=re.sub(r'\d+',replace,'a=100,b=20')
# print(s)
#
# #### 注：""" """:三个大引号中的内容（绿色字体）是占用内存可以调用的注释，可以保持原文本格式不变，如果内容过大会影响运行，和 # 注释效果不一样。
# s="""
# <div class="job-detail">
#         <p>职位描述</p>
# <p>- 理解产品需求，设计测试用例，负责Android、iOS软件测试；</p>
# <p>- 对问题进行报告、跟踪、汇总，并协助开发人员定位问题；</p>
# <p>- 搜集用户反馈问题并进行跟踪验证；</p>
# <p>- 编写测试计划、测试报告等各类测试文档；</p>
# <p><br></p>
# <p>职位要求</p>
# <p>- 熟悉软件测试理论知识、app测试方法、了解测试流程等；</p>
# <p>- 工作认真、负责、有耐心、有独立判断力、有主动学习意识；</p>
# <p>- 沟通协调能力、语言及文字表达能力强，团队合作意识强；</p>
# <p>- 计算机或相关专业本科及以上学历；</p>
#         </div>
# """
# ## 获取纯文本，去除标签
# # 字符串中如果出现 . 则要用 \.转义；正则中的点是字符的意思。
# a=re.sub(r'<\w+>|</?\w+>','',s)
# a=re.sub(r'<.*>','',a)
# print(a)
#
# ### split 根据匹配切割字符串,返回列表
# c=re.split(r':|,|_|=|\+','itcas:php,python=java_js+vba')
# print(c)
# print('------贪婪模式--------------------','\n')
# ###### 贪婪模式
# ## python 数量词默认是贪婪的，尝试匹配尽可能多的字符。非贪婪则是尽可能匹配少的字符，在'.+';'+';'{m,n}'等后面加上？，使贪婪变成非贪婪。
# s='this is a apple 345-567-34'
# r=re.match(r'(.+)(\d+-\d+-\d+)',s)
# print(r)
# ## 贪婪模式，\d+:至少一个数字，所以将 345 中 5 留给后面的（），第一个（）可以尽可能多的占用数字，所以 34 归于前面。
# print(r.group(1))
# print(r.group(2))
# ### 获取数字段的方式:s='this is a apple 345-567-34'
# ## split():分隔法
# r=re.split(' ',s)[4]
# print(r)
# ## match():数据短时，逐个匹配法
# r=re.match(r'(.+?)(\d+-\d+-\d+)',s)
# print(r.group(2))
# ## sub():替换法
# s='this is a apple 345-567-34'
# r=re.sub(r'(.*?)(\d.*)',lambda i:i.group(2),s)
# print(r,'\n')
# ##### 案例分析
# print('=================案例分析=============')
# ## 贪婪
# a=re.match(r'aa(\d+)','aa2345ddd').group(1)
# print(a)
# ## 非贪婪
# a=re.match(r'aa(\d+?)','aa2345ddd').group(1)
# print(a)
# ## 贪婪
# a=re.match(r'aa(\d+)ddd','aa2345ddd').group(1)
# print(a)
# ## 非贪婪：该例子中，aa ddd已经被确定，中间只留下2345，所以将全部被选中，而不是只选择 2
# a=re.match(r'aa(\d+?)ddd','aa2345ddd').group(1)
# print(a)
#
# s='<img src="http://ns-strategy.cdn.bcebos.com/ns-strategy/upload/applvyou_banquan2408/part-01032-511.jpg" src="http://ns-strategy.cdn.bcebos.com/ns-strategy/upload/applvyou_banquan2408/part-02343-33.jpg ">'
# ## 关闭贪婪==只获取第一个满足条件的情况及终止。
# r=re.search(r'http.+?\.jpg',s).group()
# print(r)
# r=re.search(r'http.+\.jpg',s).group()
# print(r)
# print('------------------------')
# r=re.search(r'src=.+?\.jpg',s).group()
# print(r,'\n')
# print('----------------匹配网名--------------')
# #### 匹配网址: https://www.bilibili.com/
# ## 几种获得网名的提取方法：
# s='https://www.bilibili.com/video/av42206116?p=15'
# ## match() ：从开始匹配
# r=re.match(r'(https://.*?/)',s)
# print(r.group(1))
# ## sub():替换匹配,运用lambda函数先提取 (https://.+?/) 部分，在将该部分替换整个网址。
# r=re.sub(r'(https://.+?/).*',lambda i:i.group(1),s)
# print(r)
# ## search():从头开始匹配
# r=re.search(r'https://.*?/',s).group()
# print(r)
#
# #### 找所有单词
# s='hello world ha ha'
# r=re.split(r' ',s)
# print(r)
# r=re.findall(r'(\b[a-zA-Z]+\b)',s)
# print(r,'\n')

#### 长文本提取
s='<br>◎译　　名　决X中途岛/中途岛战役/中途岛海战<br>◎片　　名　中间的way<br>◎年　　代　2019<br>◎产　　地　中国/美国<br>◎类　　别　战争/历史<br>◎语　　言　<strong><font color="Red">英语</font></strong><br>◎字　　幕　中文字幕<br>◎IMDb评分&nbsp;&nbsp;6.9/10 from 12377 用户<br>◎文件格式　X264 + AC3<br>◎视频尺寸　1920 x 798<br>◎文件大小　3 GiB<br>◎片　　长　138 Mins<br>◎导　　演　罗兰·艾默里奇 Roland Emmerich<br>◎主　　演　伍迪·哈里森 Woody Harrelson<br>&nbsp;&nbsp;　帕特里克·威尔森 Patrick Wilson<br>&nbsp;&nbsp;　卢克·伊万斯 Luke Evans<br>&nbsp;&nbsp;　艾德·斯克林 Ed Skrein<br>&nbsp;&nbsp;　丹尼斯·奎德 DennisQuaid<br>&nbsp;&nbsp;　曼迪·摩尔 Mandy Moore<br>&nbsp;&nbsp;　亚历山大·路德韦格 Alexander Ludwig<br>&nbsp;&nbsp;　艾伦·艾克哈特 Aaron Eckhart<br>&nbsp;&nbsp;　达伦·克里斯 Darren Criss<br>'
r=re.split(r'<br>',s)
#print(r)
m={}
movie=[]
for i in r:
	a=''.join(i).strip().replace('&nbsp;&nbsp;','')
	#print(a)
	if a.startswith('◎译　　名'):
		m['译名']=re.sub(r'(◎译　　名)(.*)',lambda i:i.group(2),a).strip()
		
		
	elif a.startswith('◎片　　名'):
		m['片名']=re.sub(r'(◎片　　名)(.*)',lambda i:i.group(2),a).strip()
		
	elif a.startswith('◎年　　代'):
		m['年代']=re.sub(r'(◎年　　代)(.*)',lambda i:i.group(2),a).strip()
		

	elif a.startswith('◎产　　地'):
		m['产地']=re.sub(r'(◎产　　地)(.*)',lambda i:i.group(2),a).strip()
		
	elif a.startswith('◎类　　别'):
		m['类别']=re.sub(r'(◎类　　别)(.*)',lambda i:i.group(2),a).strip()
		
	elif a.startswith('◎语　　言'):
		b=re.sub(r'(◎语　　言)(.*)',lambda i:i.group(2),a).strip()
		m['语言']=re.match(r'(<.*?>){2}(.*?)(<.*>)',b).group(2)
		
	elif a.startswith('◎字　　幕'):
		m['字幕']=re.sub(r'(◎字　　幕)(.*)',lambda i:i.group(2),a).strip()
		
	elif a.startswith('◎片　　长'):
		m['片长']=re.sub(r'(◎片　　长)(.*)',lambda i:i.group(2),a).strip()
		

	elif a.startswith('◎导　　演　'):
		m['导演']=re.sub(r'(◎导　　演　)(.*)',lambda i:i.group(2),a).strip()
		

	elif a.startswith('◎视频尺寸'):
		m['视频尺寸']=re.sub(r'(◎视频尺寸)(.*)',lambda i:i.group(2),a).strip()

	elif a.startswith('◎IMDb评分'):
		m['IMDb评分']=re.sub(r'(◎IMDb评分)(.*)',lambda i:i.group(2),a).strip().replace('&nbsp;','')
a=''.join(r).strip().replace('&nbsp;&nbsp;','')
print(a)
m['主演']=re.search(r'(.*◎主　　演)(.*)',a).group(2).replace('\u3000',' ')
movie.append(m)
#print(movie)

















