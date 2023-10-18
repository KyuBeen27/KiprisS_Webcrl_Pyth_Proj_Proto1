from selenium import webdriver      # 동적 크롤링을 위한 셀레니움 임포트.
from selenium.webdriver import ActionChains     # 화면 조작을 위한 클래스 함수.
from selenium.webdriver.common.keys import Keys     # 셀레니움으로 키를 조작하기 위한 임포트.
from selenium.webdriver.common.by import By     # find_element By 사용을 위한 임포트.

from bs4 import BeautifulSoup as bs
import requests     # 정적 크롤링, html 문서를 가져오기 위한 패키지.

import time     # time.sleep 함수를 사용하기 위한 임포트.

import sys

import csv


driver = webdriver.Chrome()     # 크롬드라이버 변수할당.


url = 'http://kpat.kipris.or.kr/kpat/searchLogina.do?next=MainSearch#page1'
# 검색할 장소.

driver.get(url)     # 크롬 드라이버에 실행.

time.sleep(2)     # 대기.

act = ActionChains(driver)

search_box = driver.find_element("id", "queryText")
act.click(search_box).perform()         # 검색 박스 클릭.

search_box.send_keys('핸드폰')
search_box.send_keys(Keys.RETURN)
time.sleep(3)         # 단어 입력 후 엔터.


HJ_ALL_Box = driver.find_element("id", "leftHangjung00")

HJ_Decl_Box = driver.find_element("id", "leftHangjung06")
HJ_Acpt_Box = driver.find_element("id", "leftHangjung07")
HJ_OK_Box = driver.find_element("xpath", "//*[@id='leftside']/div/span/a/img")

# 검색조건 중 왼쪽 행정상태 체크박스를 찾아 변수에 저장.


act.click(HJ_ALL_Box).perform()
act.click(HJ_Decl_Box).perform()
act.click(HJ_Acpt_Box).perform()

act.click(HJ_OK_Box).perform()

time.sleep(3)

# 왼쪽 행정상태 체크박스를 클릭해서 정리.


# artcs_titles = driver.find_elements(By.CSS_SELECTOR, "#mainsearch_info_list > div.search_txt")
#
# sys.stdout = open('./DataBS_For_Training_1/ArtcsE1.txt', 'w', encoding='utf-8')
#
# for i in artcs_titles:
#     ArtcsE1 = i.text
#     print(ArtcsE1)
#
# sys.stdout.close()
# ###
# ###
# artcs_titles = driver.find_elements(By.CSS_SELECTOR, "#iconStatus")
#
# sys.stdout = open('./DataBS_For_Training_1/Result1.txt', 'w', encoding='utf-8')
#
# for i in artcs_titles:
#     Result1 = i.text
#     print(Result1)
#
# sys.stdout.close()

### 텍스트 파일로 저장.


file = open('./DataBS_For_Training_1/ArtcsE1.txt', 'r', newline="", encoding='utf-8')
list = []
list = file.read().splitlines()
output_file = open('./DataBS_For_Training_1/ArtcsE1.csv', 'a', newline="", encoding='utf-8')
wr = csv.writer(output_file, quoting=csv.QUOTE_ALL)
wr.writerow(list)

file = open('./DataBS_For_Training_1/Result1.txt', 'r', newline="", encoding='utf-8')
list = []
list = file.read().splitlines()
output_file = open('./DataBS_For_Training_1/ArtcsE1.csv', 'a', newline="", encoding='utf-8')
wr = csv.writer(output_file, quoting=csv.QUOTE_ALL)
wr.writerow(list)

### csv 파일로 저장 > 행렬 전환 필요한 상태.