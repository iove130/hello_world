# coding=UTF-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("http://shop.aircheng.com/")
# get the search textbox
search_filed = driver.find_element_by_name('q')
search_filed.clear()

# enter search keyword ang submit
search_filed.send_keys('phone')
search_filed.submit()

# get all the anchor elements which have product names displayed
# currently o result page using find_elements_by_xpath method
products = driver.find_element_by_xpath("//h2[@class='product-name']/a")

# get the number of anchor elements found
print ("Found" + str(len(products)) + "products:")

#iterate through each anchor element and print the text that is
# name of the product
for product in products:
    print(product.text)
# close the browser window
driver.quit()
