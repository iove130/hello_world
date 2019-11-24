# coding = UTF-8
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://mail.163.com/')
sleep(2)
driver.find_element_by_xpath("//*[@id='switchAccountLogin']").click()

xf = driver.find_element_by_xpath("//*[@id='loginDiv']/iframe")

driver.switch_to.frame(xf)
sleep(1)
driver.find_element_by_xpath("//*[@placeholder='邮箱帐号或手机号码']").send_keys("lujingui8805")
sleep(2)
driver.find_element_by_xpath("//*[@placeholder='输入密码']").send_keys("iove130324713")


sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/form/div/div[8]/a").click()
driver.switch_to.parent_frame()
sleep(5)
# 点击写信按钮
driver.find_element_by_id("_mail_component_23_23").click()
driver.find_element_by_class_name("nui-editableAddr-ipt").send_keys("475938408@qq.com")
sleep(1)
driver.find_element_by_xpath("//*[@id='_mail_input_3_221']/input").send_keys("这是测试邮件")
ss = driver.find_element_by_class_name("APP-editor-iframe")
driver.switch_to.frame(ss)
driver.find_element_by_xpath("/html/body").send_keys("这个也是测试邮件")
sleep(2)
driver.switch_to.default_content()
sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/header/div/div[1]/div/span[2]").click()
#driver.find_element_by_class_name("nui-btn-text").click()
