# 图像处理标准库
from PIL import Image
# web测试
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 鼠标操作
from selenium.webdriver.common.action_chains import ActionChains
# 等待时间
import time
# 产生随机数
import random
# 图片转换
import base64
import geecrack


driver = webdriver.Chrome()
driver.get("https://otcbtc.com/sign_in")
username = driver.find_element_by_id('user_login')
username.send_keys("boxer009")

password = driver.find_element_by_id('user_password')
password.send_keys("passw0rd")
submit_btn = driver.find_element_by_id('tencent-verify-btn')
submit_btn.click()

while 1:
    time.sleep(1)
    start = time.process_time()
    try:
        driver.switch_to.frame(driver.find_element_by_id("tcaptcha_iframe"))
        slideblock = driver.find_element_by_id('tcaptcha_drag_thumb')
        print('已定位到元素')
        end=time.process_time()
        break
    except:
        print("-----------------------------------------------------------------------------------------------还未定位到元素!")

print('定位耗费时间：'+str(end-start))

# 鼠标点击圆球不松开
ActionChains(driver).click_and_hold(slideblock).perform()
# 将圆球滑至相对起点位置的最右边
ActionChains(driver).move_by_offset(xoffset=250, yoffset=0).perform()
time.sleep(0.4)
# 保存包含滑块及缺口的页面截图
driver.save_screenshot('D:\quekou.png')
# 放开圆球
ActionChains(driver).release(slideblock).perform()
#打开保存至本地的缺口页面截图
quekouimg=Image.open('d://quekou.png')
# 匹配本地对应原图
sourceimg=match_source(quekouimg)



visualstack=get_diff_location(sourceimg,quekouimg)
# 获取移动距离loc，827为滑块起点位置
loc=visualstack-827

