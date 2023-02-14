# import module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Get log in info
user_info = []
with open('userinfo.txt', 'r') as f:
    for line in f:
        user_info.append(line.strip())

username = user_info[0]
password = user_info[1]

# Create the webdriver object
driver = webdriver.Chrome(r"../chromedriver")

driver.get("https://my.deltasig.org/")

log_in_button = driver.find_element_by_link_text("Login with FSID")
log_in_button.click()

emailElement = driver.find_element_by_id("email")
emailElement.send_keys(user_info[0])

passwordElement = driver.find_element_by_id("password")
passwordElement.send_keys(user_info[1])
passwordElement.send_keys(Keys.ENTER)

brother_search = driver.find_element_by_xpath('//a[@href="/directory"]')
brother_search.click()

time.sleep(0.2)

search_field = Select(driver.find_element_by_xpath(
    "//select[@name='search_field']"))
search_field.select_by_index(5)

time.sleep(0.2)

search_field = Select(driver.find_element_by_xpath(
    "//select[@name='lookup_field']"))
# Chapter index (Epsilon = 95)
search_field.select_by_index(95)

time.sleep(2)

brother_file = open("brother_list.txt", "w")

# Get range by ceil(results/20): 1809/20 = 91
for i in range(5):
    elem = driver.find_element_by_xpath(
        """//*[@id="directory-table"]/tbody""")
    brother_file.write(elem.text + "\n\n")

    next_page = driver.find_element_by_xpath(
        '//button[@class="button is-pulled-right has-margin-right-touch-5 "]')
    next_page.click()
    time.sleep(3)

driver.close()
brother_file.close()
