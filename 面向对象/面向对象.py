# -*- coding: utf-8 -*-
#### 类的定义与初始化
'''
class Bank():
	title='Taipei Bank'
	def __init__(self,username,money):
		self.name=username
		self.balance=money
	
	def get_balance(self):
		return self.balance

hungbank=Bank('hung',1000)
print(hungbank.name.title(),'存款余额是',hungbank.get_balance())
print(hungbank.title)
print('================')

def main():

	class Bank():
		title = 'Taipei Bank'

		def __init__(self, username, money):
			self.name = username
			self.balance = money

		def save_money(self,money):
			self.balance+=money
			print('存款',money,'完成')

		def withdraw_money(self,money):
			self.balance-=money
			print('提款',money,'完成')

		def get_balance(self):
			print(self.name.title(),'目前余额',self.balance)
			return self.balance


	hungbank = Bank('hung', 1000)
	hungbank.get_balance()
	hungbank.save_money(130)
	hungbank.get_balance()
	hungbank.withdraw_money(300)
	#print(hungbank.name.title(), '存款余额是', hungbank.get_balance())
	print(hungbank.title)

if __name__ == '__main__':
	main()
print()

### 私有属性与方法的封装
def main():
	class Bank():
		
		def __init__(self):
			self.__name = 'huang'
			self.__balance = 0
			self.title='Taipei Bank'
			
		def save_money(self, money):
			self.__balance += money
			print('存款', money, '完成')
		
		def withdraw_money(self, money):
			self.__balance -= money
			print('提款', money, '完成')
		
		def get_balance(self):
			print(self.__name.title(), '目前余额', self.__balance)
			
	
	hungbank = Bank()
	hungbank.get_balance()
	hungbank.balance=1000
	hungbank.get_balance()
	
	print(hungbank.title)

if __name__ == '__main__':
	main()
print()


class Bank(object):
	def __init__(self):
		self.name = 'huang'
		self.balance = 1000
	
	def save_money(self,money):
		self.balance+=money
		print('存款',money,'完成')

	def withdraw_money(self,money):
		self.balance-=money
		print('提款',money,'完成')

	def get_balance(self):
		print(self.name.title(),'目前余额',self.balance)
		return self.balance

	def run(self):
		self.get_balance()
		self.save_money(130)
		self.get_balance()
		self.withdraw_money(300)
		self.get_balance()
		
if __name__ == '__main__':
	spider=Bank()
	spider.run()
	
	

from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from PIL import Image

class Blog(object):
	def __init__(self):
		self.path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
		self.url='https://account.cnblogs.com/signin'
		self.driver = webdriver.Chrome(executable_path=self.path)
		
	def login(self):
		self.driver.get(self.url)
		self.driver.maximize_window()
		time.sleep(1)
		self.driver.find_element_by_xpath('//*[@id="LoginName"]').send_keys('3333')
		time.sleep(0.5)
		self.driver.find_element_by_xpath('//*[@id="Password"]').send_keys('65437')
		
		self.driver.find_element_by_xpath('//*[@id="submitBtn"]').click()
		print('-----登录完毕----')
		time.sleep(1)
		
		
	def handle(self):
		
		## 获得图片大小和位置
		img1 = self.driver.find_element_by_xpath(
			'/html/body/div[2]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]/div/canvas[2]')
		print(img1.size, img1.location)
		
		## 保存有缺口图片
		self.driver.save_screenshot(r'F:\python代码\爬虫\boke\snap1.png')
		time.sleep(1)
		## 改变标签，显示无缺口原图。
		self.driver.execute_script(
			"var x=document.getElementsByClassName('geetest_canvas_fullbg geetest_fade geetest_absolute')[0];"
			"x.style.display='block';"
			"x.style.opacity=1"
		)
		## 截完整图
		self.driver.save_screenshot(r'F:\python代码\爬虫\boke\snap2.png')
		img2 = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]/div/canvas[2]')
		print('---处理完毕--')
		return img1
		
	def calculate(self,img1):
		img1_snap = Image.open(r'F:\python代码\爬虫\boke\snap1.png')
		img2_snap = Image.open(r'F:\python代码\爬虫\boke\snap2.png')
		threhold = 60
		for x in range(img1.location['x'] + 60, img1.size['width'] + img1.location['x']):
			for y in range(img1.location['y'], img1.size['height'] + img1.location['y']):
				rgb1 = img1_snap.load()[x, y]
				rgb2 = img2_snap.load()[x, y]
				res1 = abs(rgb1[0] - rgb2[0])
				res2 = abs(rgb1[1] - rgb2[1])
				res3 = abs(rgb1[2] - rgb2[2])
				if not (res1 < threhold and res2 < threhold and res3 < threhold):
					print('阴影x轴位置：%d' % x)
					return x
	
	def slide_distance(self,x):
		l = x - 560
		print('需要滑行距离：%d' % l)
		
		track = []
		s = 0
		v = 5
		t = 1.5
		upl = l * 2 / 3
		a1 = 3
		a2 = -2
		while s < l:
			if s < upl:
				a = 2
			else:
				a = -3
			v0 = v
			v = v0 + a * t
			s1 = v * t + 1 / 2 * a * t * t
			s += s1
			track.append(s1)
		print(track)
		return track
	
	def drage_down(self,track):
		silde = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div[1]/div[2]/div[2]')
		print('滑块的大小和位置',silde.size, silde.location)
		for x in track:
			ActionChains(self.driver).click_and_hold(silde).perform()
			ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=0).perform()
		ActionChains(self.driver).move_by_offset(xoffset=30, yoffset=0).perform()
		ActionChains(self.driver).move_by_offset(xoffset=-30, yoffset=0).perform()
		ActionChains(self.driver).release().perform()
		#time.sleep(1)
		self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div[3]').click()
		#time.sleep(1)
		
	def run(self):
		self.login()
		img=self.handle()
		diatance=self.calculate(img)
		track=self.slide_distance(diatance)
		result=self.drage_down(track)

if __name__ == '__main__':
	spider=Blog()
	spider.run()

'''

### 三代同堂 super()     ========== 继承性
class Grandfather():
	def __init__(self):
		self.grandfatermoney=10000
	
	def get_money1(self):
		print("Grandfather's information")

class Father(Grandfather):
	def __init__(self):
		self.fathermoney=8000
		super().__init__()
	
	def get_money2(self):
		print("Father's information")

class Son(Father):
	def __init__(self):
		self.sonmoney=50000
		super().__init__()
	
	def get_money3(self):
		print("Son's information")
	
	def get_money(self):
		print("\n祖父资产: ",self.grandfatermoney,
			  "\n父亲资产: ",self.fathermoney,
			  "\n儿子资产: ",self.sonmoney,)
Tom=Son()
Tom.get_money1()
Tom.get_money2()
Tom.get_money3()
Tom.get_money()
print('=============')


##### 兄弟属性的取得
## 类名()+属性
class Father(Grandfather):
	def __init__(self):
		self.fathermoney = 8000
		super().__init__()
	
	def get_money(self):
		print("Father's information",self.fathermoney)
		print('--------')


class Son1(Father):
	def __init__(self):
		self.son1_money = 50000
		super().__init__()
	

class Son2(Father):
	def __init__(self):
		self.son2_money = 60000
		super().__init__()
	
	def get_money2(self):
		print("\nSon2's information",self.son2_money,
			  "\nFather's information",self.fathermoney,
			  "\nSon1's information",Son1().son1_money)   ## 注意：son2 引用 son1 属性的写法
Tom=Son2()
Tom.get_money()
Tom.get_money2()