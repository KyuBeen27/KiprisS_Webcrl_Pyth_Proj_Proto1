from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

driver.get('http://kpat.kipris.or.kr/kpat/searchLogina.do?next=MainSearch')

time.sleep(2)

act =ActionChains(driver)

search_box = driver.find_element("id", "queryText")
act.click(search_box).perform()

search_box.send_keys('핸드폰')
search_box.send_keys(Keys.RETURN)
time.sleep(3)

HJ_ALL_Box = driver.find_element("id", "leftHangjung00")
HJ_Decl_Box = driver.find_element("id", "leftHangjung06")
HJ_Acpt_Box = driver.find_element("id", "leftHangjung07")
HJ_OK_Box = driver.find_element("xpath", "//*[@id='leftside']/div/span/a/img")

act.click(HJ_ALL_Box).perform()

act.click(HJ_Decl_Box).perform()

act.click(HJ_Acpt_Box).perform()

act.click(HJ_OK_Box).perform()

time.sleep(7)