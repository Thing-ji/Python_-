from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # 잠시 기다리기
from selenium.webdriver.support import expected_conditions as EC # 밑에 쓰이는거 보면서 이해하기


browser = webdriver.Chrome()
browser.maximize_window() # 창 화면 최대화

# 네이버 이동
url = "https://www.naver.com/"
browser.get(url)

# 검색창에 네이버 항공편 겅색
browser.find_element_by_name('query').send_keys("네이버 항공권")
browser.find_element_by_id('search_btn').send_keys(Keys.ENTER)

# browser.find_element_by_class_name('link_name').click()
browser.find_element_by_link_text('네이버 항공권').click()

### 오류나지만 일단 코드 적어보기

# 가는 날 선택 클릭
browser.find_element_link_text('가는날 선택').click()

# 이번달 27일, 28일 선택
browser.find_elements_by_link_text('27')[0].click() # [0] -> 이번달
browser.find_elements_by_link_text('28')[0].click() # [0] -> 이번달

# 다음달 27일, 28일 선택
browser.find_elements_by_link_text("27")[1].click() # [1] -> 다음달
browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

# 이번달 27일, 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [0] -> 이번달
browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음달

# 제주도 선택
browser.find_element_by_xpath("xpath.copy()").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()


try:
    elem= WebDriverWait(browser, 10).until(EC.presence_of_element_located(By.XPATH, 'xpath.copy()')) # 브라우저를 열어서 최대 10초 기다리는데, xpath의 화면이 보일때까지 기다렸다가 하라
    # 성공했을 때 동작 수행
    print(elem.text) # 첫 번쨰 결과 출력
finally:
    browser.quit()



# # 첫번째 결과 출력
# elem = browser.find_element_by_xpath("xpath.copy()")
# print(elem.text)


