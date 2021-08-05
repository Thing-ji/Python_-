import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('./chromedriver.exe')

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id('id').send_keys("naver_id")
browser.find_element_by_id('pw').send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id를 새로 입력
browser.find_element_by_id('id').clear() # 기존에 입력되었던 것을 지워줌
browser.find_element_by_id('id').send_keys("my_id") # my_id라고 다시 입력

time.sleep(5)

browser.quit()
