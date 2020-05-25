# -*- coding: utf-8 -*-
import re
import time
import openpyxl
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from lxml import etree
a=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

options = webdriver.ChromeOptions()
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver=webdriver.Chrome(executable_path=a,options=options)

headers={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 '
}


def swip_down():
	driver.maximize_window()
	h = driver.get_window_size()['height']
	
	for x in range(1, 10):
		js = "var q=document.documentElement.scrollTop=" + str(h * x)
		driver.execute_script(js)
		time.sleep(1)


def parese_details(ur):
	h = driver.get_window_size()['height']
	html = etree.HTML(driver.page_source)
	
	driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[4]').click()
	jpg=html.xpath('//div[@id="spec-n1"]//img[1]/@src')[0]
	jpg='https:'+jpg
	print(jpg)
	
	infos = html.xpath('//div[@class="m-item-inner"]')[0]
	titles = infos.xpath('.//div[@class="sku-name"]/text()')
	for title in titles:
		title = title.strip()
		print(title)
	prices = infos.xpath('.//div[@class="dd"]/strong/text()')            ## 价格
	for price in prices:
		print(price)
	
	result=driver.find_element_by_xpath('//*[@id="summary-price"]/div[2]/div[1]/span[1]/span').is_displayed()
	print(result)
	
	plus_price=driver.find_element_by_xpath('//*[@id="summary-price"]/div[2]/div[1]/span').text
	print(plus_price)
	# plus_price=infos.xpath('.//span[@class="p-price-fans"]/span/text()') ## 会员价
	# print(plus_price)
	
	print('************************************')
	comments_count = infos.xpath('.//div[@id="comment-count"]//a/text()')[0]
	print(comments_count)                                         ## 累计评价
	print('==================')
	
	result=driver.find_element_by_xpath('//*[@id="summary-order"]/div[2]/font').is_displayed()
	print(result)
	
	rate=driver.find_element_by_xpath('//*[@id="summary-order"]/div[2]/font').text         ## 排名
	print(rate)
	
	
	driver.refresh()
	swip_down()
	time.sleep(2)
	comments = driver.find_element_by_xpath('//*[@id="comment-0"]/div[1]/div[1]/div[1]/img').get_attribute('alt')  ## 用户信息
	for i in comments:
		print(i)
	

	print('-------------------------')
	
	comments = html.xpath('//div[@id="comment-0"]//p[1]/text()')
	for i in comments:                                     ## 评论
		print(i)
	print('-------------------------------------')
	
	


def main():
	base_url = 'https://www.jd.com/'
	driver.get(base_url)
	source = driver.page_source
	html=etree.HTML(source)
	driver.maximize_window()
	driver.find_element_by_id('key').send_keys('python')
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
	time.sleep(1)
	
	html=etree.HTML(driver.page_source)
	urls=html.xpath('//ul[@class="gl-warp clearfix"]//div[@class="p-img"]/a/@href')
	for url in urls:
		ur=url
		if ur.startswith('//'):
			ur='https:'+ur
			driver.execute_script('window.open("%s")' % ur)
			driver.switch_to.window(driver.window_handles[1])
			
			swip_down()
			
			parese_details(ur)
			driver.close()
			driver.switch_to.window(driver.window_handles[0])
			
		# html=etree.HTML(driver.page_source)
		# infos=html.xpath('//div[@class="m-item-inner"]')[0]
		# titles=infos.xpath('.//div[@class="sku-name"]/text()')
		# for title in titles:
		# 	title=title.strip()
		# 	print(title)
		# prices=infos.xpath('.//div[@class="dd"]/strong/text()')
		# for price in prices:
		# 	print(price)
		#
		# comments_count=infos.xpath('.//div[@id="comment-count"]//a/text()')
		# print(comments_count)
		# print('==================')
		#
		#
		# driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[4]').click()
		# for x in range(1, 8):
		# 	js = "var q=document.documentElement.scrollTop=" + str(h * x)
		# 	driver.execute_script(js)
		# 	time.sleep(1)
		# users = html.xpath('//div[@class="tab-con"]//div[@class="user-info"]/text()')
		# users=''.join(users).strip()
		# for user in users:
		# 	print(user)
		# comments = html.xpath('//div[@class="tab-con"]//div[@class="comment-column J-comment-column"]//p[1]/text()')
		# for i in comments:
		# 	print(i)
		# print('-------------------------------------')
		# time.sleep(5)
		#
		# driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[1]').click()
		# for x in range(1, 8):
		# 	js = "var q=document.documentElement.scrollTop=" + str(h * x)
		# 	driver.execute_script(js)
		# 	time.sleep(1)
		# time.sleep(2)
		# infs=html.xpath('//div[@id="J-detail-content"]')[0]
		# content=infs.xpath('.//div[@class="item-mc"]/div/text()')
		# content=''.join(content).strip()
		# print(content)


if __name__ == '__main__':
	main()