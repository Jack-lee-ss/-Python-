### ============  自动化测试--selenium ================
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#tps://www.baidu.com')
#print(driver.page_source)
### driver.close():关闭当前页面。driver.quit():关闭所有页面
#time.sleep(5) ## 程序中间插入 time 模块。先写出左式，在出现下划线的字符上用鼠标点中，按住 Alt+enter 出现 import this name 再按住 enter 键 ，选择相应模块即可。
#driver.close()
#driver.quit()
#driver.clear() : 清除输入的数据

####  其他属性
## 定位元素
#inputTag=driver.find_element_by_id('kw') ## 搜索百度首页的关键字
#inputTag=driver.find_element_by_name('wd')
#inputTag=driver.find_element_by_class_name('s_ipt')
#inputTag=driver.find_element_by_xpath("//input[@name='wd']")
#inputTag=driver.find_element_by_css_selector(".quickdelete-wrap > input") ## css选择器 选中元素，加点， > input：表示下方直接子元素。
#inputTag=driver.find_elements_by_css_selector(".quickdelete-wrap > input")[0] ## 获取多个返回是列表
#print(inputTag.send_keys('python')) ## 自动输入查找的内容,注意在原网站上的对应关系。以上效果相同，都可以输入需要查找内容
## 如果只是想解析网页中的数据，那么推荐将网页源代码用lxml来解析，因为它是用C语言写的，效率快。如果要对元素进行操作，比如给一个文本框输入值，或者点击按钮，那么要用selenium操作。from lxml import etree  html=etree.HTML(driver.page_source) html.xpath("")

### 操作表单
## checkbox
# from selenium import webdriver
# a=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
# driver=webdriver.Chrome(executable_path=a)
# driver.get('https://www.douban.com')
#driver.find_element_by_link_text('读书').click() ## 定位文本，并且点击该文本。如果该文本有乱码，则加上u (u'读书')
#driver.find_element_by_partial_link_text('电').click()#定位一串文本的部分字段也可以打开新一页。
#driver.find_element_by_link_text('下次自动登录').click()
#driver.find_element_by_xpath("//input[@type='text']").send_keys('python')

## 布尔定位 and or(一般只用and) 两个定位元素必须相邻。
#driver.find_element_by_xpath('//input[@type="text" and @maxlength="60"]').send_keys('读书')
##driver.find_element_by_xpath('//*[@type="text" and @maxlength="60"]').send_keys('读书') 效果同上

##### 浏览器窗口操作
## 切换页面
from selenium import webdriver
from lxml import etree
a=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
driver=webdriver.Chrome(executable_path=a)
def main():
	url='https://www.baidu.com/'
	driver.get(url)
	
	# 'window.open（'url'）': 切换到另一个网址上。
	# driver.execute_script:调用js脚本。
	driver.execute_script('window.open("https://www.lagou.com/jobs/list_Python/p-city_2?&cl=false&fromSearch=true&labelWords=&suginput=")')
	print(driver.current_url)                # 打印当前网址
	
	# switch_to.window：切换到另一个网页上
	# handle[0]:代表第一个页面；[1]:第二个页面
	driver.switch_to.window(driver.window_handles[1]) # switch_to_window 将to后面的_改为.
	try:
		location=(By.XPATH,'//div[class="body-container"]//div[class="body-btn"]')
		WebDriverWait(driver,10).until(EC.presence_of_element_located(location))
		driver.find_element_by_xpath('//div[class="body-container"]//div[class="body-btn"]').click()
		driver.maximize_window()
		print(driver.current_url)
		print(driver.get_window_size())
		print(driver.get_window_position())
	except:
		print('---没有加载--')
	h = driver.get_window_size()['height']
	while True:
		for x in range(1,5):
			js = "var q=document.documentElement.scrollTop=" + str(h*x)
			driver.execute_script(js)
			time.sleep(1)
			
		next_btn = driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')
		if 'pager_next pager_next_disabled' in next_btn.get_attribute('class'):
			break
		else:
			next_btn.click()
		time.sleep(2)
	
	
if __name__ == '__main__':
	main()
	
# for x in range(1,11,2):
# 	time.sleep(0.5)
# 	j=x/10
# 	js='document.documentElement.scrollTop=document.documentElement.scrollHeight * %f'% j
#
# 	for x in range(1, 15):
# 		time.sleep(0.5)
# 		j = x / 100
# 		js = 'document.documentElement.scrollTop=document.documentElement.scrollHeight * %f' % j
# 		driver.execute_script(js)
#
# 	while True:
# 		for i in range(1, 11):
# 			js = "var q=document.documentElement.scrollTop=" + str(300 + 20 * i)
# 			driver.execute_script(js)
# 			time.sleep(1)
# 			if js == "var q=document.documentElement.scrollTop=700":
# 		next_btn = driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')
# 		if 'pager_next pager_next_disabled' in next_btn.get_attribute('class'):
# 			break
# 		else:
# 			next_btn.click()
# 		time.sleep(2)









