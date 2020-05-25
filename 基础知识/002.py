#### =========== selenium 浏览器用法 ===================
#coding:utf-8
import time

from selenium import webdriver
### 设置浏览器宽高
import sys

from selenium.webdriver import ActionChains

a=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
dr=webdriver.Chrome(executable_path=a) ## 具有路径的变量
# dr.get("http://m.mail.10086.cn")
# dr.set_window_size(480,800) ## （宽，高）
# dr.maximize_window()

# """
# ## 浏览器页面后退和前进按钮
# #now_url=dr.current_url ## 获取当前地址
# dr.find_element_by_link_text('139企业邮箱').click()
# time.sleep(3)
# dr.back()
# now_url=dr.current_url
# #print(now_url)
# time.sleep(2)
# dr.forward()
# now_url=dr.current_url
# #print(now_url)
# """ 多行注释 Ctrl+/  再次则取消

#### 自动登录网易账户页面
# dr.get("http://mail.163.com/index_alternate.htm")
# # dr.find_element_by_link_text('密码登录').click()
# time.sleep(3)
# # now_url=dr.current_url
# # print(now_url)
# dr.find_element_by_id('idInput').clear()
# dr.find_element_by_id('idInput').send_keys('lcq19920706')
# dr.find_element_by_id('pwdInput').clear()
# dr.find_element_by_id('pwdInput').send_keys('1142lcq')
# dr.find_element_by_id('loginBtn').click()

##### 获取浏览器宽高参数
# dr.get('https://www.baidu.com')
# print(dr.find_element_by_id('kw').size)
#
# print(dr.find_element_by_id('kw').is_displayed()) # 判断是否显示或者加载某个内容
# print(dr.find_element_by_id('kw').get_attribute('type')) # 判断类型

###### 鼠标事件
# dr.get("https://www.douban.com/")
# time.sleep(5)
# a=dr.find_element_by_xpath('//input[@ name="remember"]/label/text')
# a.click()
#dr.get("https://www.baidu.com")
# right_click=dr.find_element_by_id('su').click()
# ActionChains(dr).context_click(right_click).perform()
#####  鼠标右键点击查看

# a=dr.find_element_by_link_text('设置')
# ActionChains(dr).move_to_element(a).perform()
###    鼠标悬停

# double_click=dr.find_element_by_link_text('新闻')
# ActionChains(dr).double_click(double_click).perform()
####   双击元素

# a=dr.find_element_by_link_text('设置')
# ActionChains(dr).move_to_element(a).perform()
# b=dr.find_element_by_link_text('搜索设置')
# c=dr.find_element_by_link_text('隐私设置')
# ActionChains(dr).drop_by_(b,c).perform()
####   拖拽

#####  键盘事件  ？？


# dr.get("http://mail.163.com/index_alternate.htm")
# print('Before login========')
# title=dr.title
# print(title)
# ### 打印当前页面
# now_url=dr.current_url
# print(now_url)
# time.sleep(3)
# dr.find_element_by_id('idInput').clear()
# dr.find_element_by_id('idInput').send_keys('lcq19920706')
# dr.find_element_by_id('pwdInput').clear()
# dr.find_element_by_id('pwdInput').send_keys('1142lcq')
# dr.find_element_by_id('loginBtn').click()
# #### 输密码登录
#
# print('After login==============')
# title=dr.title
# print(title)
# ####### 打印当前页面 title
#
# now_url=dr.current_url
# print(now_url)
# #### 打印当前页面url
# time.sleep(3)
# user_name=dr.find_element_by_id('spnUid').text
# print(user_name)
#
# if user_name=='lcq19920706@163.com':
# 	print('login success！')
# else:
# 	print('login error！')

#### 登录豆瓣登录网
# dr.get("https://accounts.douban.com/passport/login")
# time.sleep(3)
# dr.find_element_by_name('phone').send_keys('111111')
# dr.find_element_by_id('code').send_keys('1122')
# dr.find_element_by_name('remember').click()
# time.sleep(5)
# dr.find_element_by_class_name('btn').click()

#### 登录豆瓣官网 https://www.douban.com/
# dr.get('https://www.douban.com/')
# #dr.switch_to.frame(dr.find_element_by_css_selector('[frameborder="0"]'))
# dr.switch_to.frame(dr.find_element_by_xpath('//iframe[@frameborder="0"]')) ## 效果同上
# dr.find_element_by_name('phone').send_keys('1234567')
# dr.find_element_by_id('code').send_keys('bbbbbbb')
# time.sleep(3)
# dr.find_element_by_name('remember').click()
# dr.find_element_by_class_name('btn-phone').click()
#### 注：在含有iframe的元素中，元素查找一般只在除iframe子集的范围内寻找，所以当出现有需要定位的元素在iframe子集中，需要先转向该子集中，dr.switch_to.frame(),里面填入ID,Name属性的值，如无则用 CSS或者xpath 在该行定位。后面解析元素均在iframe中进行，当需要跳出该子集时，加上代码 dr.switch to.default_content() 用法和进入相同。  Class属性dr.find_element_by_class_name('btn btn-phone')，注：该代码错误，class只能将一部分作为值，btn或者btn-phone，不能一起。

### 切换到新的窗口 handle（句柄），网页的ID
dr.get('http://f.python3.vip/webauto/sample3.html')
print(dr.title)
dr.find_element_by_css_selector('[target="_blank"]').click()
Mainwindow=dr.current_window_handle ## 存储原窗口可以与新窗口分开

for handle in dr.window_handles:
	dr.switch_to.window(handle)
	if 'Bing' in dr.title:
		break
#### 该循环通过关键字判断需要寻找的窗口


dr.find_element_by_id('sb_form_q').send_keys('Python')
print(dr.title)
time.sleep(2)
dr.switch_to.window(Mainwindow)
## 返回原窗口

dr.find_element_by_id('outerbutton').click()
## 对原窗口操作















