# -*- coding: utf-8 -*-
### 验证码滑动

from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from PIL import Image

def main():
	a = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
	options = webdriver.ChromeOptions()
	# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
	options.add_experimental_option('excludeSwitches', ['enable-automation'])
	driver = webdriver.Chrome(executable_path=a, options=options)
	driver.get('https://account.cnblogs.com/signin')
	driver.maximize_window()
	driver.find_element_by_xpath('//*[@id="LoginName"]').send_keys('3333')
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="Password"]').send_keys('65437')
	
	driver.find_element_by_xpath('//*[@id="submitBtn"]').click()
	time.sleep(2)
	
	img1=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]/div/canvas[2]')
	print(img1.size,img1.location)
	
	## 按钮位置
	silde=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div[1]/div[2]/div[2]')
	print(silde.size,silde.location)
	
	driver.save_screenshot(r'F:\python代码\爬虫\boke\snap1.png')  ## 截有缺口图
	
	
	## 改变标签，显示无缺口原图。
	driver.execute_script(
		"var x=document.getElementsByClassName('geetest_canvas_fullbg geetest_fade geetest_absolute')[0];"
		"x.style.display='block';"
		"x.style.opacity=1"
		)
	
	driver.save_screenshot(r'F:\python代码\爬虫\boke\snap2.png')  ## 截完整图
	img2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]/div/canvas[2]')
	

	img1_snap=Image.open(r'F:\python代码\爬虫\boke\snap1.png')
	img2_snap=Image.open(r'F:\python代码\爬虫\boke\snap2.png')
	threhold=60
	for x in range(img1.location['x']+60,img1.size['width']+img1.location['x']):
		for y in range(img1.location['y'],img1.size['height']+img1.location['y']):
			rgb1=img1_snap.load()[x,y]
			rgb2=img2_snap.load()[x,y]
			res1 = abs(rgb1[0] - rgb2[0])
			res2 = abs(rgb1[1] - rgb2[1])
			res3 = abs(rgb1[2] - rgb2[2])
			if not (res1 < threhold and res2 < threhold and res3 < threhold):
				print('阴影x轴位置：%d'%x)
				break
		else:
			continue
		break
	### 加速滑动：
	l = x - 560
	print('需要滑行距离：%d'%l)
	track=[]
	s=0
	v=5
	t=1.5
	upl=l*2/3
	a1=3
	a2=-2
	while s<l:
		if s<upl:
			a=2
		else:
			a=-3
		v0=v
		v=v0+a*t
		s1=v*t+1/2*a*t*t
		s+=s1
		track.append(s1)
	print(track)
	for x in track:
		ActionChains(driver).click_and_hold(silde).perform()
		ActionChains(driver).move_by_offset(xoffset=x,yoffset=0).perform()
	ActionChains(driver).move_by_offset(xoffset=30, yoffset=0).perform()
	ActionChains(driver).move_by_offset(xoffset=-30, yoffset=0).perform()
	ActionChains(driver).release().perform()
	time.sleep(2)
	driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div[3]').click()
	time.sleep(4)
	


if __name__ == '__main__':
	main()