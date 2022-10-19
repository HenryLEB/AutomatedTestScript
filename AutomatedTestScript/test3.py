#coding=utf-8
from appium import webdriver
import time
#导入TouchAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '12'     #手机系统版本
desired_caps['deviceName'] = '192.168.101.151:42265'     #刚才的devicename
desired_caps['appPackage'] = 'com.wewave.circlef'#计算器的package
desired_caps['appActivity'] = 'com.wewave.circlef.ui.launch.LaunchActivity'
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 1200
desired_caps['settings[waitForIdleTimeout]'] = 100

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps )#运行该脚本desired_caps
time.sleep(1)  #在计算器页面等待3秒
# driver.find_elements(By.NAME, "Hi")[0].click()
# driver.find_elements(By.ID, "com.wewave.circlef:id/iv_rankings")[0].click()
driver.find_elements(By.ID, "com.wewave.circlef:id/td_post")[0].click()
driver.find_elements(By.ID, "com.wewave.circlef:id/iv_post_bg_3")[0].click()
driver.find_elements(By.ID, "com.wewave.circlef:id/v_random_subject_click")[0].click()
driver.tap([(53,686),(350,781)])
driver.find_elements(By.ID, "com.wewave.circlef:id/tv_post_together_ga")[0].click()
time.sleep(5)
elements = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
print(f"哈哈： ${elements}")
time.sleep(5)
for item in elements:
    print(item.text)
    if item.text == '关闭麦克风':
        item.click()
        break
driver.find_elements(By.ID, "com.wewave.circlef:id/ll_create_or_change")[0].click()
time.sleep(1)
driver.tap([(53,686),(350,781)])

print('连接成功')  #控制台输出“连接成功”

# driver.quit()
# (filed.get(imm) as? View)?.takeIf { WeakReference(it.context) == context.get() }?.also {
# (filed.get(imm) as? View)?.takeIf { WeakReference(it.context).get() == context.get() }?.also {
