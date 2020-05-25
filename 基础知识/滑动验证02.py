# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from PIL import Image
# def main():
# 	a = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
# 	#options = webdriver.ChromeOptions()
# 	# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
# 	#options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 	driver = webdriver.Chrome(executable_path=a)
# 	driver.get('https://www.iqiyi.com/')
# 	driver.maximize_window()
# 	driver.find_element_by_xpath('//*[@id="block-A"]/div/div/div[4]/div[6]/div[1]/div/a/img').click()
# 	time.sleep(3)
# 	ifram=driver.find_element_by_xpath('//*[@id="login_frame"]')
# 	driver.switch_to.frame(ifram)
#
# 	driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[4]/div[2]/p/span/a[1]').click()
#
# 	driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/input').clear()
#
# 	driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/input').send_keys('1111@163.com')
# 	driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/div[1]/div/div[2]/div/input[1]').send_keys('3333333')
# 	time.sleep(1)
# 	driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[1]/div[1]/div/a[2]').click()
# 	time.sleep(3)
#
# 	driver.execute_script(
# 		"var x=document.getElementsByClassName('fail-msg retry')[0];"
# 		"x.style.display='block';"
# 		"x.style.opacity=0.5"
# 	)
# 	time.sleep(4)
# if __name__ == '__main__':
# 	main()



from selenium import webdriver
import time
a=r'D:\火狐浏览器\Firefox Setup 55.0\geckodriver.exe'
driver=webdriver.Firefox(executable_path=a)
driver.get('https://www.baidu.com')