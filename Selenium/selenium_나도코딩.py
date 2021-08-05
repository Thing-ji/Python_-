## selenium1
from selenium import webdriver

browser = webdriver.Chrome('./chromedriver.exe')
browser.get("http://naver.com")

elem = browser.find_element_by_class_name('link_login')
elem.click()
elem.back()
browser.back()
elem = browser.find_element_by_id("query")
from selenium.webdriver.common.keys import Keys
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)

## selenium2
elem = browser.find_element_by_tag_name('a') # 'a'로 된 태크 맨위에꺼 찾기
elem = browser.find_elements_by_tag_name('a') # 'a'로 된 태크 모두 찾기
for e in elem:
    e.get_attribute('href') # 'a'의 href값 얻기
browser.back()

elem = browser.find_element_by_name('q')
elem.send_keys("나도코딩")
elem = browser.find_element_by_xpath('//*[@id="nx_search_form"]/fieldset/button') # xpath를 이용한 검색(검색아이콘 클릭기능)
elem.click()
browser.close() # 브러우저 창 하나만 닫기
browser.quit() # 창 모두 닫기
