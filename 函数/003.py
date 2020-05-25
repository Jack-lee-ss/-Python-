# -*- coding: utf-8 -*-
'''
###  python 基本操作
## print()函数
print('hello','world') # 默认字符串之间空一格，结尾换行。
print('hello','world',sep='') # 将两个字符串之间空格去掉，空字符串。
print('hello','world',end='') # 将自动换行去掉
print('hello','world',end='=') # 将结尾改为 = 而不是换行
print('hello','world',end='\n++') # 先换行，在添加 ++
print('hello','world')
print(input.__name__) # 获取函数名
print('===========','\n')

#### 函数类型的参数----计时器
import datetime

def timer(t,start,finished):
	t_start=datetime.datetime.now()
	if start:    # 判断 start()函数是否有值，有值则执行，None 则不执行。
		start()
	while True:
		t_end=datetime.datetime.now()
		a=t_end - t_start
		if a.seconds>=t:
			break
	if finished:
		finished()
		
def f():
	i=int(input('请输入数字：'))
	print(i)
	
def s():
	print('等3秒钟')
	
timer(3,s,f)

def f2():
	print('hahaha')
	
timer(1,None,f2)


#####  函数嵌套
def f():
	def fn():
		print('fn')
	fn()
f()
print('-------')

def f():
	def fn():
		print('fn')
	return fn
a=f()
a()  ## 返回了 fn 函数 赋给 a 变量，a=fn --> a()=fn()

## 计数器--------闭包
def counting(count):
	def fn():
		nonlocal count   # “nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量”
		count-=1
		if count<0:
			return       # 如果条件成立则返回 None
		return count
	return fn
a=counting(5)
b=counting(3)
print('a',a())
print('b',b())
print('a',a())
print('b',b())
print('a',a())
print('b',b())
print('a',a())
print('b',b())
print('a',a())
print('b',b())
'''
#### 字典基础
# d={'北京':22,'上海':44}
# print(d['北京'])
#
# d['北京']=30
# print(d)
#
# d['广州']=45
# print(d)
#
# d.pop('北京')
# print(d,'\n')
#
# #d={'北京':22,'上海':44}
# a=d.get('合肥',-1) # 返回指定键的值，如果值不在字典中返回默认值None
# print(a)
#
# a=d.setdefault('广州',-1)  # 如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值。
# print(a)
#
# a=d.setdefault('武昌',-1)  # 当‘武昌’不存在字典中时，会将 武昌：-1添加到字典中
# print(d)
#
#
# a=d.update({'武汉':77,'澳门':76,'福建':88}) # 添加多个字典
# print(d)
#
# d.clear() # 删除字典内容
# print(d,'\n')
#
# b={'上海': 44, '广州': 45, '武汉': 77}
# print(len(b))  # 字典长度
#
# print(str(b)+'hahhaa') # 字典转化为字符串
#
# print('广州'in b) # 判断键是否在字典中  等价：print('广州'in d.keys())
# print(44 in d.values()) # 判断值是否在字典中
# print('====')
# v=b.pop('上海',-3) # 返回一个删除键的值
# print(v)
#
# v=b.pop('关东',-3) # 如果删除一个不存在字典的键值，会报错，加上第二参数，保证不存在时，将-3赋给 v
# print(v)
# print('======================')
#
# ## 遍历字典
# s={'上海': 44, '广州': 45, '武昌': -1, '武汉': 77, '澳门': 76, '福建': 88}
# for i in s:
# 	print(i)  # 遍历字典键
# 	print(s[i]) # 遍历值
#
# print()
#
# for k,v in s.items():
# 	print(k,v)
#
# print(list(s.keys()))
# print(list(s.values()))
# print(list(s.items()))
# print()
#
# s=dict(a=1,b=2,c=3)  ## 打印字典
# print(s)
#
# ## 字典嵌套
# s=dict(a=[1,2,3],b={'1':100,'ab':800},c=3)
# print(s)
# print(s['b']['ab'])
# print(s['a'][1])

#####
import time

from selenium.webdriver.chrome import webdriver


class LaGoSpider(object):


	'''
	
	封装为一个类，方便操作
	
	'''


def __init__(self):
	options = webdriver.ChromeOptions()
	
	options.add_argument('--headless')
	
	options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
	
	self.driver = webdriver.Chrome(r'D:\外安装软件\selenium1\chromedriver_win32\chromedriver.exe', options=options)
	
	self.data_list = []


def address_url(self):


	'''
	
	获取目标url（拼接）
	
	'''

	self.citys = ['全国', '北京', '深圳', '广州', '杭州', '成都', '南京', '上海', '厦门', '西安', '长沙']
	
	self.baseurl = 'https://www.lagou.com/jobs/list_python?px=default&city={}'

	for self.city in self.citys:
		
		self.url = self.baseurl.format(quote(self.city))
		
		self.driver.get(self.url)
		
		print('正在爬取<%s>' % self.city)
		
		while True:
			
			source = self.driver.page_source
			
			self.position_url_parse(source)
			
			next_page = self.driver.find_element_by_xpath('//span[@class="pager_next "]')
			
			if 'contains(class, "pager_next")' in next_page.get_attribute('class'):  # 判断一页是否爬取完成
				
				print('<%s爬取完毕>' % self.city)
				
				break
			
			else:
				
				self.driver.execute_script("arguments[0].click()", next_page)
				
				print('----------------爬取下一页--------------')
				
				time.sleep(random.randint(3, 5))


def position_url_parse(self, source):


'''

获取每个职位的url

'''

	html = etree.HTML(source)
	
	lis = html.xpath('//ul[@class="item_con_list"]//li')
	
	for li in lis:
		position_url = li.xpath('.//a[@class="position_link"]//@href')[0]
		
		self.request_urls(position_url)
		
		time.sleep(random.randint(1, 3))
	
	
	def request_urls(self, list_url):
		self.driver.execute_script('window.open("%s")' % list_url)
		
		self.driver.switch_to_window(self.driver.window_handles[1])
		
		source = self.driver.page_source
		
		self.parse_position(source)
		
		time.sleep(random.randint(1, 3))
		
		self.driver.close()
		
		self.driver.switch_to_window(self.driver.window_handles[0])
		
		time.sleep(random.randint(1, 3))


def parse_position(self, source):


'''

抓取每个职位的详情信息

'''

self.data = {}

html = etree.HTML(source)

company = html.xpath('//dl[@class="job_company"]/dt/a/img/@alt')[0]

print(company)

self.data['公司'] = company

name = html.xpath('//div[@class="position-content-l"]//span[@class="name"]/text()')[0]

self.data['名称'] = name

salary = html.xpath('//dd[@class="job_request"]/p[1]/span[1][@class="salary"]/text()')[0]

self.data['薪资'] = salary

city = ''.join(html.xpath('//dd[@class="job_request"]/p[1]/span[2]/text()')[0]).replace('/', '')

self.data['城市'] = city

jinyan = ''.join(html.xpath('//dd[@class="job_request"]/p[1]/span[3]/text()')[0]).replace('/', '')

self.data['经验'] = jinyan

xueli = ''.join(html.xpath('//dd[@class="job_request"]/p[1]/span[4]/text()')[0]).replace('/', '')

self.data['学历'] = xueli

zhihuo = html.xpath('//*[@id="job_detail"]/dd[1]/p/text()')[0]

self.data['职位诱惑'] = zhihuo

zhimiao = ''.join(html.xpath('//div[@class="job-detail"]//p//text()')).replace('岗位职责: ', '').replace('岗位要求：',
																									 '').replace(
	'岗位职责：', '').replace('工作职责：', '').replace('项目背景：', '').replace('-', '').strip()

self.data['职位描述'] = zhimiao

self.data_list.append(self.data)

self.csv_()


def csv_(self):
	'''

	保存数据为csv

	'''
	
	header = ['公司', '名称', '薪资', '城市', '经验', '学历', '职位诱惑', '职位描述']
	
	with open('lagou_quanguo.csv', 'w', encoding='utf-8', newline='')as fb:
		writer = csv.DictWriter(fb, header)
		
		writer.writeheader()
		
		writer.writerows(self.data_list)


if __name__ == '__main__':
	LG = LaGoSpider()
	
	LG.address_url()







