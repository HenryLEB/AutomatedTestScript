#coding=utf-8
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '12'     #手机系统版本
desired_caps['deviceName'] = '192.168.101.151:42265'     #刚才的devicename
desired_caps['appPackage'] = 'com.wewave.circlef'#计算器的package
desired_caps['appActivity'] = 'com.wewave.circlef.ui.launch.LaunchActivity'
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 1200

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps )#运行该脚本desired_caps
time.sleep(3)  #在计算器页面等待3秒
print('连接成功')  #控制台输出“连接成功”

# driver.quit()
