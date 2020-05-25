# -*- coding: utf-8 -*-
### selenium 操作
# import re
# import time
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# from lxml import etree
# a=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
#
# options = webdriver.ChromeOptions()
# # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
# options.add_experimental_option('excludeSwitches', ['enable-automation'])
# driver=webdriver.Chrome(executable_path=a,options=options)
#
# ### 几种JS操作
# url='https://www.baidu.com/'
# driver.get(url)
# img=driver.find_element_by_class_name('index-logo-src')
# ## fadeOut()函数：用于隐藏所有匹配的元素，并带有淡出的过渡动画效果
# driver.execute_script('$(arguments[0]).fadeOut()',img)      ## 不加载指定图片
# time.sleep(4)
# #driver.close()
# time.sleep(2)
#
# url='https://www.jd.com/'
# driver.get(url)
# js='window.scrollTo(400,document.body.scrollHeight-750)'  ## 横竖模拟拉动滚条
# driver.execute_script(js)
# time.sleep(4)
import time

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def main():
	# a = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
	# driver = webdriver.Chrome(executable_path=a)
	
	# b = r'D:\火狐浏览器\Firefox Setup 48.0.2\geckodriver.exe'
	# driver = webdriver.Firefox(executable_path=b)
	# driver.get('https://www.baidu.com/')
	# time.sleep(2)
	
	c=r'D:\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe'
	driver=webdriver.PhantomJS(executable_path=c)
	driver.get('https://www.baidu.com')
	time.sleep(3)

if __name__ == '__main__':
	main()