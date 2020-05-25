# -*- coding: utf-8 -*-
## 豆瓣滑动验证码处理：
'''
## 模拟上下滑动
import random
from random import randint

from selenium import webdriver
import time

def swipe_down(v,driver):
	driver.maximize_window()
	h = driver.get_window_size()['height']
	# for x in range(1, 5):
	# 	js = "var q=document.documentElement.scrollTop=" + str((h / 2) * x)
	# 	driver.execute_script(js)
	# 	time.sleep(1)
	# time.sleep(3)
	
	## 模拟上下滑动
	for x in range(int(v/0.1)):
		if (x % 2 == 0):
			js = "var q=document.documentElement.scrollTop=" + str(300 + 400 * x)
		else:
			js = "var q=document.documentElement.scrollTop=" + str(200 * x)
		driver.execute_script(js)
		time.sleep(0.1)
	js = "var q=document.documentElement.scrollTop=100000"
	driver.execute_script(js)
	time.sleep(0.1)
	driver.find_element_by_xpath('//*[@id="jobList"]/div[1]/ul/li[5]/div[1]/div[1]/div/h2/a').click()
	#driver.find_element_by_xpath('//div[class="position_name fl"]//a/@href').click()
	time.sleep(1)

	
	
def main():
	a = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
	driver = webdriver.Chrome(executable_path=a)
	# driver.get('https://www.douban.com/')
	# driver.save_screenshot('douban.png') # 页面截图
	driver.get('https://www.lagou.com/')
	driver.maximize_window()
	time.sleep(1)
	box = driver.find_element_by_id('cboxClose').click()
	time.sleep(2)
	v=random.randint(1,3)
	swipe_down(v,driver)
	
if __name__ == '__main__':
	main()
'''


## 豆瓣滑动验证码处理：重复多次输入错误密码与账号，激活滑动验证码显现。
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_track(distance):
	# 模拟距离=175(distance)，加速4/5，加速度a=1; 减速1/5，加速度=-2，初始位移:current=0,初速度v=0
    # 加速距离 mid=(4/5)*distance; 时间间隔 t=1 track=[]
	current=0
	track = []
	mid=distance*4/5
	t=1
	v=0
	while current<distance:  # 模拟距离不大于135
		if current<mid:  	 # 加速阶段 a=1,否则 b=-2
			a=1
		else:
			a=-2
		v0=v
		v=v0+a*t             # 当前速度
		x=v0*t+1/2*a*t*t     # 滑动距离
		#print(x)
		current=current+x    # 当前位移
		track.append(x)      # 记录每0.2秒滑行距离，存入列表中
		print(track)
	return track			 # 返回列表，所有加速，减速距离和应该小于135
	

def main():
	a = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
	driver = webdriver.Chrome(executable_path=a)
	driver.get('https://www.douban.com/')
	time.sleep(1)
	#driver.switch_to.frame(0) 该代码指主网页中第一个内嵌网页
	iframe=driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe') #先进入
	driver.switch_to.frame(iframe)
	time.sleep(1)
	driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
	time.sleep(2)
	driver.find_element_by_id('username').send_keys(123)
	driver.find_element_by_id('password').send_keys(1224555)
	time.sleep(3)
	driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
	time.sleep(3)

	iframe=(By.XPATH,'//*[@id="TCaptcha"]/iframe')  # 再次进入滑动验证码所在页面
	WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located(iframe)) # 判断是否加载
	iframe = driver.find_element_by_xpath('//*[@id="TCaptcha"]/iframe')
	driver.switch_to.frame(iframe)     # 再次进入滑动验证码所在页面
	
	a=driver.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]') # 定位拖拽按钮
	# 由于豆瓣拖拽按钮横向滑行距离几乎不变，所以可以先截图获取 xoffset=188 滑行距离，引入动作链，在拖拽即可。如果不行或者尝试几次均无法成功，可以添加加速度，模拟真人动作。
	# 方法一：截图可知滑行距离 188 恒量。该方法一般容易被检测为机器，速度过快。
	'''
	# ActionChains(driver).drag_and_drop_by_offset(a,xoffset=188,yoffset=0).perform()
	# time.sleep(3)
	'''
	# 方法二：
	# 加速度滑行：模拟一种相对真实的人的滑动过程：刚开始先加速，到后面开始减速。
	ActionChains(driver).click_and_hold(a).perform() # 按住拖拽按钮
	
	# 模拟真人 先加速，在减速。 move_by_offset：从当前位置开始滑动
	tracks=get_track(175)
	for track in tracks:
		ActionChains(driver).move_by_offset(xoffset=track,yoffset=0).perform()
	#time.sleep(0.5)
	ActionChains(driver).release().perform()
	time.sleep(3)
	
if __name__ == '__main__':
	main()