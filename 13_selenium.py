## Selenium 기본 문법1

from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe")
browser.get('http://naver.com')

elem = browser.find_element_by_class_name('link_login')
elem

elem.click()
browser.back() # 뒤로
browser.forward() # 앞으로
browser.refresh() # 새로고침
browser.back()

elem = browser.find_element_by_id("query") # naver에서 검색창에 글씨 쓴 후 검색하기
from selenium.webdriver.common.keys import Keys

elem.send_keys("나도코딩") # 검색창에 "나도코딩" 입력
elem.send_keys(Keys.ENTER) # 검색

## Selenium 기본 문법2




