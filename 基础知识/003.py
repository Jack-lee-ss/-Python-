
#### =============  selenium 自动化 ==================

### 选择框（radio,checkbox,select单复选择框）
#coding:utf-8
import time
from selenium import webdriver
import sys

from selenium.webdriver import ActionChains
a=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
dr=webdriver.Chrome(executable_path=a)

#### radio 框 radio框选择选项，直接用WebElement的click方法，模拟用户点击就可以了
## 公用网址
#dr.get('http://f.python3.vip/webauto/test2.html')
# dr.find_element_by_css_selector('#s_radio input[checked=checked]') ### 原网页代码默认勾选项。
# dr.find_element_by_css_selector('#s_radio input[value="小雷老师"]').click()

#### CheckBox框 要选中checkbox的一个选项，必须先获取当前该复选框的状态 ，如果该选项已经勾选了，就不能再点击。否则反而会取消选择。先把 已经选中的选项全部点击一下，确保都是未选状态，再点击需要勾选的内容。

## 先把已经选中（默认选项）的选项全部点击一下，确保都是未点击状态，在点击需要点击的项。
# elements=dr.find_elements_by_css_selector('#s_checkbox input[checked="checked"]') ## find_elements 注意加-s 返回多个数的列表。
# ## 遍历每一个已经选择的项
# for element in elements:
# 	element.click()
# dr.find_element_by_css_selector('#s_checkbox input[value="小雷老师"]').click()


### radio框及checkbox框都是input标签，只是里面的type不同而已。select框 则是一个新的select标签，大家可以对照浏览器网页内容查看一下。对于Select 选择框，Selenium 专门提供了一个Select类 进行操作。Select类 提供了如下的方法：select_by_value 根据选项的 value属性值 ，选择元素。例如：<option value="foo">Bar</option>  s.select_by_value('foo')，select_by_index 根据选项的 次序 （从1开始），选择元素。select_by_visible_text，根据选项的 可见文本 ，选择元素。获取该元素。

## Select单选框

#  导入Select类
# from selenium.webdriver.support.ui import Select
# # 创建Select对象,找到含有select标签的行，并且定位，将对象赋给变量
# a=Select(dr.find_element_by_id("ss_single"))
# ## 选中该对象，在select类中，点击不用 .click()
# a.select_by_visible_text('小雷老师')
#
# ### Select多选框 （先去掉原来的选项，在进行选择）
# # 导入Select类
# from selenium.webdriver.support.ui import Select
#
# # 创建Select对象
# select = Select(wd.find_element_by_id("ss_multi"))
#
# # 清除所有 已经选中 的选项
# select.deselect_all()
#
# # 选择小雷老师 和 小凯老师
# select.select_by_visible_text("小雷老师")
# select.select_by_visible_text("小凯老师")


###### 其他动作形式

### 冻结页面 （有些网站上面的元素， 我们鼠标放在上面，会动态弹出一些内容，当我们的鼠标从图标移开，这个栏目就整个消失了，就没法 查看其对应的 HTML。在 开发者工具栏 console里面执行如下js代码：setTimeout(function(){debugger},5000)表示在5000毫秒后执行 debugger 命令。执行该命令会 浏览器会进入debug状态。 debug状态有个特性， 界面被冻住， 不管我们怎么点击界面都不会触发事件）

### 弹出对话框

##  Alert 目的就是显示通知信息，只需用户看完信息后，点击OK（确定） 就可以了.模拟用户点击弹出对话框 OK 按钮。
# dr.implicitly_wait(5)
# dr.get('http://f.python3.vip/webauto/test4.html')
# dr.find_element_by_id('b1').click() ## 点击按钮
# time.sleep(2)
# print(dr.switch_to.alert.text) ## 弹出点击的对话框
# dr.switch_to.alert.accept()  ## 店家OK按钮，确认。

##  Confirm弹出框，主要是让用户确认是否要进行某个操作,分别是 OK 和 Cancel，分别代表 确定 和 取消 操作。

# dr.find_element_by_id('b2').click() ## 点击按钮
# time.sleep(2)
# print(dr.switch_to.alert.text) ## 弹出点击的对话框
# dr.switch_to.alert.dismiss() ## 点击取消操作

#### Prompt 弹出框 是需要用户输入一些信息，提交上去，
# dr.find_element_by_id('b3').click()
# time.sleep(2)
# print(dr.switch_to.alert.text)
# dr.switch_to.alert.send_keys('hello')
# dr.switch_to.alert.accept()


#### 操作cookie
# dr.get('https://www.baidu.com')
# for cookie in dr.get_cookies(): ## 获得当前页面的cookie
# 	print(cookie)
# print('+'*20)
# print(dr.get_cookie('H_PS_PSSID')) ## 打印 'name': 'H_PS_PSSID' 列表的值
# print('='*30)
# print(dr.delete_cookie('H_PS_PSSID')) ## 删除后无 cookie
# print('----'*20)


### css 选择器   CSS Selector 同样可以根据tag名、id 属性和 class属性 来 选择元素

# 根据 tag（标签）名 选择元素的 CSS Selector 语法非常简单，直接写上tag名即可 elements = wd.find_elements_by_css_selector('div')；根据id属性 选择元素的语法是在id号前面加上一个井号： #id值；<input  type="text" id='searchtext' />      element = wd.find_element_by_css_selector('#searchtext')；根据class属性 选择元素的语法是在 class 值 前面加上一个点： .class值         elements = wd.find_elements_by_css_selector('.animal')

### 选择子代或者后代元素
# 如果元素2是元素1的直接子元素，CSS Selector语法：元素1 > 元素2 选择元素2。多层级的选择：元素1 > 元素2 > 元素3 > 元素4，选择元素4。
# 如果元素2是元素1的后代元素，CSS Selector语法：元素1   元素2 选择元素2。多层级的选择：元素1   元素2   元素3  元素4， 选择元素4。
dr.get('http://f.python3.vip/webauto/sample1.html')
# elements=dr.find_elements_by_css_selector('#layer1  span')
# for element in elements:
# 	print(element.get_attribute('outerHTML')) ### 遍历提取的HTML
# 	print('--'*20)
# elements=dr.find_elements_by_css_selector('.plant  span')
# for element in elements:
# 	print(element.get_attribute('outerHTML')) ### 遍历提取的HTML
# 	print('--'*20)
# dr.quit()

# elements=dr.find_elements_by_css_selector('#container > div')
# for element in elements:
# 	print(element.get_attribute('outerHTML')) ### 遍历提取的HTML
# 	print('--'*20)
# dr.quit()

# elements=dr.find_elements_by_css_selector('#layer1  span')
# for element in elements:
# 	print(element.get_attribute('outerHTML')) ### 遍历提取的HTML
# 	print('--'*20)
# dr.quit()

##### 根据属性值定位元素   css 选择器支持通过任何属性来选择元素，语法是用一个方括号 []
# element = dr.find_element_by_css_selector('[href="http://www.miitbeian.gov.cn"]')   ### ['href'] 效果相同
# print(element.get_attribute('outerHTML'))

### 验证CSS  CSS Selector 是浏览器直接支持的，可以在浏览器 开发者工具栏 中验证，按F12 打开 开发者工具栏

### 联合使用
# element = dr.find_element_by_css_selector('div.footer1 > span.copyright')
# print(element.get_attribute('outerHTML'))
# element = dr.find_element_by_css_selector('.footer1 > .copyright')
# print(element.get_attribute('outerHTML'))
# element = dr.find_element_by_css_selector('.footer1  .date')
# print(element.get_attribute('outerHTML'))
#
# element = dr.find_element_by_css_selector('#container  div')
# print(element.get_attribute('outerHTML'))
#
# ### 组选择（和） 如果我们要 同时选择所有class 为 plant 和 class 为 animal 的元素。css选择器可以 使用 逗号 ，称之为 组选择  .plant , .animal，也可以不同标签的内容。
# elements = dr.find_elements_by_css_selector('.plant,.animal')
# for element in elements:
# 	print(element.get_attribute('outerHTML')) ### 遍历提取的HTML
# 	print('--'*20)

####  不同标签的联合选择
# dr.get('http://f.python3.vip/webauto/sample1a.html')
# elements=dr.find_elements_by_css_selector('#t1 > span , #t1 > p')
# for element in elements:
# 	print(element.get_attribute('outerHTML')) ### 遍历提取的HTML
# 	print('--'*20)
# dr.quit()


#### 按次序选择子节点
dr.get('http://f.python3.vip/webauto/sample1b.html')
elements=dr.find_elements_by_css_selector('#t1 , #t2') ## 全选
for element in elements:
	print(element.get_attribute('outerHTML')) ### 遍历提取的HTML
	print('--'*20)


# 父元素的第n个子节点  nth-child
elements=dr.find_elements_by_css_selector('span:nth-child(2)')
for element in elements:
	print(element.get_attribute('outerHTML')) ### 遍历提取的HTML
	print('--'*20)


## 父元素的倒数第n个子节点   nth-last-child
elements=dr.find_elements_by_css_selector('p:nth-last-child(1)')
for element in elements:
	print(element.get_attribute('outerHTML')) ### 遍历提取的HTML
	print('--'*20)


## 父元素的第几个某类型的子节点   nth-child  不考虑位置，只考虑类型次序
elements=dr.find_elements_by_css_selector('span:nth-of-type(2)')
for element in elements:
	print(element.get_attribute('outerHTML')) ### 遍历提取的HTML
	print('--'*20)


### 兄弟节点选择  选择h3后面的span元素  紧接相邻的
elements=dr.find_elements_by_css_selector('h3+span')
for element in elements:
	print(element.get_attribute('outerHTML')) ### 遍历提取的HTML
	print('==='*20)
elements=dr.find_elements_by_css_selector('#t1 h3+span')
for element in elements:
	print(element.get_attribute('outerHTML')) ### 遍历提取的HTML
	print('+++'*20)
### 后续所有兄弟节点选择
elements=dr.find_elements_by_css_selector('h3~span')
for element in elements:
	print(element.get_attribute('outerHTML')) ### 遍历提取的HTML
	print('==='*20)


dr.quit()