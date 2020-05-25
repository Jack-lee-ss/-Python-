# 生活不会突变，你要做的只是耐心和积累。人这一辈子没法做太多的事情，所以每一件尽力而为。
# -*- coding: utf-8 -*-
## 定时器

'''
	在while True死循环中，schedule.run_pending()是保持schedule一直运行，去查询上面那一堆的任务，在任务中，就可以设置不同的时间去运行

	单一任务：
		import schedule
		import time

		def job():
			print("I'm working...")

		schedule.every(10).minutes.do(job)
		schedule.every().hour.do(job)
		schedule.every().day.at("10:30").do(job)
		schedule.every(5).to(10).days.do(job)
		schedule.every().monday.do(job)
		schedule.every().wednesday.at("13:15").do(job)

		while True:
			schedule.run_pending()
			time.sleep(1)

	多任务：
		import datetime
		import schedule
		import time

		def job1():
			print("I'm working for job1")
			time.sleep(2)
			print("job1:", datetime.datetime.now())

		def job2():
			print("I'm working for job2")
			time.sleep(2)
			print("job2:", datetime.datetime.now())

		def run():
			schedule.every(10).seconds.do(job1)
			schedule.every(10).seconds.do(job2)

			while True:
				schedule.run_pending()
				time.sleep(1)

'''
# '''
# #采集网页打印成pdf文档输出
# # -*- coding: UTF-8 -*-
# import pdfkit
# import requests
# from lxml import etree
# import re
#
# confg = pdfkit.configuration(wkhtmltopdf=r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\wkhtmltox\bin\wkhtmltopdf.exe')
#
#
# #获取链接
# def get_listurl():
#     url="https://www.dusaiphoto.com/article/detail/2/"
#     list_url = [url,]
#     html=requests.get(url).content.decode('utf-8')
#     con=re.findall(r'<div class="card-text" style="overflow: hidden">(.+?)<div class="container-fluid">',html,re.S)[0]
#     listurls=re.findall(r'<p class="mb-0">.+?<a href="(.+?)".+?style="color: #b8b8b8;"',con,re.S)
#     for listurl in listurls:
#         listurl=f'https://www.dusaiphoto.com{listurl}'
#         list_url.append(listurl)
#     print(list_url)
#     return list_url
#
# #获取正文内容
# def get_content(url):
#     #url='https://www.dusaiphoto.com/article/detail/4/'
#     html=requests.get(url).content.decode('utf-8')
#     content=re.findall(r'<div class="mt-4">(.+?)<div class="mt-4 mb-4">',html,re.S)[0]
#     return content
#
# #保存html为pdf文档
# def dypdf(contents):
#     contents=etree.HTML(contents)
#     s = etree.tostring(contents).decode()
#     print("开始打印内容！")
#     pdfkit.from_string(s, r'out.pdf',configuration=confg)
#     print("打印保存成功！")
#
#
# if __name__ == '__main__':
#     contents=''
#     urls=get_listurl()
#     for url in urls:
#         print(url)
#         content=get_content(url)
#         contents='%s%s%s'%(contents,content,'<p><br><p>')
#
#     dypdf(contents)
# '''

'''

# 注意：部分网页中的图像在浏览器中可以显式出来，但是在抠出来的代码中需要对图片地址进行分析，有些
缺少域名，则需要在notepad++等编辑器中加上，构成完整的图片地址才可以显式在PDF中，有些要解密的则
要对其解密等。然后再将修改好的 html 文档放入 test.html 中，转化为PDF文件

import pdfkit
# test.html:将需要的内容的部分或者全部html复制下来，粘贴于 test.html中
path=pdfkit.configuration(wkhtmltopdf=r'D:\Python 3.6.6版\pdfkit\wkhtmltopdf\bin\wkhtmltopdf.exe')
pdfkit.from_file('test.html','ts1234.pdf',configuration=path)


## 将字符串写入pdf中：
import pdfkit
def create_pdf(str_data, to_file):
	'将字符串生成pdf文件'
	# （需下载wkhtmltox）将程序路径传入config对象
	config = pdfkit.configuration(wkhtmltopdf=r'D:\Python 3.6.6版\pdfkit\wkhtmltopdf\bin\wkhtmltopdf.exe')
	# 生成pdf文件，to_file为文件路径
	pdfkit.from_string(str_data, to_file, configuration=config)


create_pdf('Hello!', 'out.pdf')
'''

# yagmail 实现发邮件

'''

github项目地址: https://github.com/kootenpv/yagmail

安装

pip install yagmail
简单例子

import yagmail

#链接邮箱服务器
yag = yagmail.SMTP( user="user@126.com", password="1234", host='smtp.126.com')

# 邮箱正文
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']

# 发送邮件
yag.send('taaa@126.com', 'subject', contents)


总共四行代码搞定，是不是比上面的例子简单太多了。

给多个用户发送邮件

# 发送邮件
yag.send(['aa@126.com','bb@qq.com','cc@gmail.com'], 'subject', contents)
只需要将接收邮箱 变成一个list即可。

发送带附件的邮件

# 发送邮件
yag.send('aaaa@126.com', '发送附件', contents, ["d://log.txt","d://baidu_img.jpg"])
'''



L = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
# [11, 1, 2, 3, 5]
s=[]
for i in L:
	if i  not in s:
		s.append(i)
print(list(set(s)))
f=list(set(s))
l=[]
print(f[-1])
f.insert(0,f[-1])
f.pop()
print(f)
print('============')


print(set(L))
print(sorted(list(set(L))[::-1], key=lambda v: str(v)[0]))
print(sorted(list(set(L))[::-1]))

import requests
#定义url
url = 'https://fanyi.baidu.com/sug'
#发送一个请求
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
data = {'kw':'机械'}
res  = requests.post(url,headers=headers,data=data)
code = res.status_code
if code == 200:
    print('请求成功')
    #print(res.text)
    print(res.json())
    resdata = res.json()['data'][0]['v']
    print(resdata)