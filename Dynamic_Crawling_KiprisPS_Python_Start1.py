from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

import time

driver = webdriver.Chrome()


url = 'http://kpat.kipris.or.kr/kpat/searchLogina.do?next=MainSearch#page1'

driver.get(url)
time.sleep(1.5)

act =ActionChains(driver)

search_box = driver.find_element("id", "queryText")
act.click(search_box).perform()

search_box.send_keys('핸드폰')
search_box.send_keys(Keys.RETURN)
time.sleep(1.5)


HJ_ALL_Box = driver.find_element("id", "leftHangjung00")

HJ_Decl_Box = driver.find_element("id", "leftHangjung06")
HJ_Acpt_Box = driver.find_element("id", "leftHangjung07")
HJ_OK_Box = driver.find_element("xpath", "//*[@id='leftside']/div/span/a/img")

act.click(HJ_ALL_Box).perform()
act.click(HJ_Decl_Box).perform()
act.click(HJ_Acpt_Box).perform()

act.click(HJ_OK_Box).perform()

# 웹 페이지 초기 검색조건 정렬.(동적 웹크롤링)


for PMRS1 in range(1, 4):

    for SP1 in range(2, 12):


        if SP1 != 11:

            NumbeFF = SP1 + 1
            PButtn_2 = driver.find_element(By.CSS_SELECTOR, "#divBoardPager > a:nth-child({})".format(NumbeFF))
            act.click(PButtn_2).perform()
            time.sleep(2)

        else:
            PButtn_2 = driver.find_element(By.CSS_SELECTOR, "#divBoardPager > a.next")
            act.click(PButtn_2).perform()
            time.sleep(2)


time.sleep(3)





