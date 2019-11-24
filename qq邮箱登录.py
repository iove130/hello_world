# coding = UTF-8
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("https://mail.qq.com/")
driver.maximize_window()
sleep(2)
driver.switch_to.frame("login_frame")
# 输入账号
driver.find_element_by_id("u").send_keys("475938408")
sleep(1)
# 输入密码
driver.find_element_by_id("p").send_keys("qingmingshijie12")
sleep(1)
# 点击登录按钮
driver.find_element_by_id("login_button").click()


quit()