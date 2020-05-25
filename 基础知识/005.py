### ================  App操作 =====================
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.connectiontype import ConnectionType
from selenium.webdriver.support.wait import WebDriverWait

desired_caps=dict()
desired_caps['platformName']="Android"
desired_caps["platforVersion"]="5.1.1"
desired_caps["deviceName"]="127.0.0.1:62001"
desired_caps["appPackage"]='com.android.settings'
desired_caps['appActivity']='.Settings'
#####  以下两句代码支持中文输入
desired_caps['unicodeKeyboard']='True'
desired_caps['resetKeyboard']='True'



## 连接本地
driver =webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


###--------------------------定位一个元素-----------

#### 定位放大镜按钮并且点击 ID
# driver.find_element_by_id('com.android.settings:id/search').click()
# ### 放大镜输入框中输入文字 class
# driver.find_element_by_class_name('android.widget.EditText').send_keys('hello')
# ### 定位返回按钮 xpath
# # driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='收起']").click()
# driver.find_element_by_xpath('//*[@content-desc="收起"]').click()

####-------------------------定位一组元素-------------

# titles=driver.find_elements_by_id('com.android.settings:id/title') ## 获取的是列表
# for title in titles:
# 	print(title.text) ## 输出列表内容
# print(len(titles)) ## 输出列表里个数
# print(titles)      ## 输出类型
# print(titles[0].text)   ## 输出列表中第一个文本
# # titles[3].click()  ## 点击第四个文本
#
# #### 输出 class类型 同上 同一个元素可以有不同标签来定位
#
# ### xpath 定位包含相同元素的内容
# ls=driver.find_elements_by_xpath("//*[contains(@text,'设')]") ## 包含相同元素
# print(len(ls))
# for l in ls:
# 	print(l.text)

##### 注意：如果传入使用 find.element_xx 方法的错误数据，会报错；如果传入使用 find.elements_xx 方法的错误数据，会返回空列表，不会报错。


####  元素等待
## 网速，服务器处理，电脑配置等原因，导致页面加载慢于代码处理速度，导致报错现象。

# 隐式等待  等待元素加载指定时长超出时长报错，NoSuchElementException，调用deiver.implicity_wait.后面多有定位元素方法都会按照该设置进行。

# 显示等待 等待元素加载指定时长，超出时长出现TimeoutException错误。调用webdriver

# print('-----准备点击')
# a=WebDriverWait(driver,5,1).until(lambda x: x.find_element_by_xpath("//*[@content-desc='收起']"))
# a.click()
# print('-----点完了')   ### 注意：element 不加 S ，单个元素可以点击，列表不能点击。

### 显式与隐式等待区别：显式只对当前操作元素作用；隐式等待则对全局查找元素作用。sleep():会造成时间浪费，降低效率。

### 输入和清空
# driver.find_element_by_id('com.android.settings:id/search').click()
# input=driver.find_element_by_class_name('android.widget.EditText')
# input.send_keys('你好')
# time.sleep(2)
# input.clear()
# driver.find_element_by_class_name('android.widget.ImageButton').click()

#### 获取元素的大小和位置
# button=driver.find_element_by_id('com.android.settings:id/search')
# print(button.location)
# print(button.location['x']) 元素距离左边界的距离
# print(button.location['y']) 元素距离上边界的距离
# print('-------------')
# print(button.size)
# print(button.size['width'])
# print(button.size['height'])

######  获取元素属性值：返回元素属性名对应的属性值

### 一般属性值的获取，直接输入属性名，即可返回属性值。
# search=driver.find_elements_by_id('com.android.settings:id/title')
# for i in search:
# 	print(i.get_attribute('enabled'))
# 	print(i.get_attribute('clickable'))
# 	print(i.get_attribute('text'))
# 	print('------------')


### 特殊属性值的获取，resource-id(使用resourceId),class（使用className）,两者API>=18,如果想要获取 content-desc 则使用 name 属性名获取。其他都可以使用uiautomatice获取。
# search=driver.find_elements_by_id('com.android.settings:id/title')
# for i in search:
# 	print(i.get_attribute('text'))
# 	print(i.get_attribute('resourceId'))
# 	print(i.get_attribute('className'))
# 	print(i.get_attribute('name')) # name属性名获得 text和content-desc任意存在的值
# 	print('------------')


########  模拟滑动

### driver.swipe（start_x,start_y,end_x,end_y,duration=None(毫秒，1000)）

#driver.swipe(100,2000,100,1500,5000)
#driver.swipe(100,2000,100,500,5000)
# 时间相同时，距离越长，效果靠后
#driver.swipe(100,2000,100,100,5000)
#driver.swipe(100,2000,100,100,2000)
# 距离相同时，持续时间约长，惯性越小，受惯性影响小。

###  scroll 事件  滑动事件 一个元素到另一个元素（swipe：坐标的变化）直到页面停止。driver.scroll(初始元素，结束元素)  滑动距离受惯性影响，距离不准,有持续事件
# a=driver.find_element_by_xpath("//android.widget.TextView[@text='电池']")
# b=driver.find_element_by_xpath('//android.widget.TextView[@text="更多"]')
# driver.scroll(a,b)


### drag_and_drop 拖拽事件 一个元素位置替换另一个元素位置，元素变动位置准确，无惯性影响。
# a=driver.find_element_by_xpath("//android.widget.TextView[@text='电池']")
# b=driver.find_element_by_xpath('//android.widget.TextView[@text="更多"]')
# driver.drag_and_drop(a,b)

### 注意三中滑动是否传入元素还是坐标，是否需要惯性影响。


######  高级手势的应用-------TouchAction  创建对象，调用手势，perform()执行

## 轻敲，tap
#tap=driver.find_element_by_xpath('//android.widget.TextView[@text="更多"]')
#TouchAction(driver).tap(tap).perform() ## 通过标定位元素在点击

# TouchAction(driver).tap(x=750,y=750).perform() ## 通过坐标点击元素，效果同上
# TouchAction(driver).tap(x=750,y=750,count=2).perform() ## 对目标元素双击

### 按下和抬起  ---------- press release

# tap=driver.find_element_by_xpath('//android.widget.TextView[@text="更多"]')
# TouchAction(driver).press(tap).perform()

# TouchAction(driver).press(x=750,y=750).perform() ## 按下
# time.sleep(2)
# TouchAction(driver).press(x=750,y=750).release().perform() ## 先按下再抬起

## 等待 ------------------ wait(1000毫秒)
# TouchAction(driver).tap(x=650,y=650).perform()
# time.sleep(2)
# TouchAction(driver).press(x=650,y=650).wait(2000).perform()

## 长按 ----------------- long_press  效果等价  按下+等待
# Action(driver).long_press(x=650,y=650,duration=2000).release().perform()


#### 移动 ------------- move_to()    注意文件名发生改变，直接跳至画图解锁处。
## 先做好图案，在 uiautomation 中拍照后，将右边数据拉大，出现数据定位值，在将鼠标依次放在每一个节点上，记录相关xy数值对，记录下来，运行代码。
# desired_caps=dict()
# desired_caps['platformName']="Android"
# desired_caps["platforVersion"]="5.1.1"
# desired_caps["deviceName"]="127.0.0.1:62001"
# desired_caps["appPackage"]='com.android.settings'
# desired_caps['appActivity']='.ChooseLockPattern'
# #####  以下两句代码支持中文输入
# desired_caps['unicodeKeyboard']='True'
# desired_caps['resetKeyboard']='True'
#
# driver =webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# (TouchAction(driver).press(x=722,y=998).move_to(x=722,y=998)
#  .move_to(x=237,y=1487).move_to(x=704,y=1963)
#  .move_to(x=237,y=1967).release().perform())
### 代码过长，可以通过换行缩短，但会出现\,如果不想出现可以在代码首尾加上（），在里面换行，如上图。

### 获取手机分辨率与截图
# print(driver.get_window_size())  ## 手机页面去分辨率 返回值是字典
# print(driver.get_window_size()['height'])
#
# print(driver.get_screenshot_as_file('D:/data/001.png'))  ### 返回值是布尔值，传路径+命名图片

### 获取手机网络
#print(driver.network_connection)  # 返回 网络类型，6：流量+网络。1：飞行模式； 4：只有流量；2：无线网

### 设置网络类型 飞行模式
#print(driver.set_network_connection(1))

### 判断网络类型 from appium.webdriver.connectiontype import ConnectionType
# if driver.network_connection == ConnectionType.DATA_ONLY:
# 	print(1)
# else:
# 	print(0)
# print(driver.set_network_connection(6))


### 发送键到设备 记住常见的数值
# 三次音量+，返回 两次音量-。
# driver.press_keycode(24) ## +
# time.sleep(1)
# driver.press_keycode(24)
# time.sleep(1)
# driver.press_keycode(24)
# time.sleep(1)
# driver.press_keycode(4)  ## 返回键
# time.sleep(1)
# driver.press_keycode(25) ## -
# time.sleep(1)
# driver.press_keycode(25)
# time.sleep(1)


### 下拉通知栏和关闭
driver.open_notifications()
time.sleep(2)
driver.press_keycode(4) # 返回键
