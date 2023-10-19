from selenium import webdriver      # 동적 크롤링을 위한 셀레니움 임포트.
from selenium.webdriver import ActionChains     # 화면 조작을 위한 클래스 함수.
from selenium.webdriver.common.keys import Keys     # 셀레니움으로 키를 조작하기 위한 임포트.
from selenium.webdriver.common.by import By     # find_element By 사용을 위한 임포트.

from bs4 import BeautifulSoup as bs
import requests     # 정적 크롤링, html 문서를 가져오기 위한 패키지.

import time     # time.sleep 함수를 사용하기 위한 임포트.

import sys

import csv

########

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




for PMNP1 in range(1,10):

    PButtn_2 = driver.find_element(By.CSS_SELECTOR, "#divBoardPager > a.next")
    act.click(PButtn_2).perform()
    time.sleep(3)  # 페이지 이동 후 로딩 대기.


# 1 부터 31 페이지까지 페이지를 자동으로 이동.
for PMRS1 in range(1, 4):

    for SP1 in range(2, 12):


        if SP1 != 11:       # 마지막 11의 버튼은 '다음' 버튼이다.

            NumbeFF = SP1 + 1
            PButtn_2 = driver.find_element(By.CSS_SELECTOR, "#divBoardPager > a:nth-child({})".format(NumbeFF))
            act.click(PButtn_2).perform()       # 아래쪽의 페이지 버튼을 클릭해서 다음 페이지로 이동. (이렇게 해야 검색조건을 유지하면서 다음 페이지로 이동할 수 있다.)
            time.sleep(3)         # 페이지 이동 후 로딩 대기.

        else:       # 11 버튼은 '다음' 버튼이다.
            PButtn_2 = driver.find_element(By.CSS_SELECTOR, "#divBoardPager > a.next")
            act.click(PButtn_2).perform()
            time.sleep(3)         # 페이지 이동 후 로딩 대기.

        #######

        artcs_titles = driver.find_elements(By.CSS_SELECTOR, "#mainsearch_info_list > div.search_txt")

        sys.stdout = open('./DataBS_For_Training_1/ArtcsE1.txt', 'a', encoding='utf-8')

        for i in artcs_titles:
            ArtcsE1 = i.text
            print(ArtcsE1)

        sys.stdout.close()
        ###
        ###
        artcs_titles = driver.find_elements(By.CSS_SELECTOR, "#iconStatus")

        sys.stdout = open('./DataBS_For_Training_1/Result1.txt', 'a', encoding='utf-8')

        for i in artcs_titles:
            Result1 = i.text
            print(Result1)

        sys.stdout.close()

        ### 텍스트 파일로 저장.


time.sleep(3)       # 마지막 화면 확인용 대기시간.


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

### csv 파일로 저장 > 행렬 전환 필요한 상태, 1500개 희망.