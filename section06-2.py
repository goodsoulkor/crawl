# Section06-2
# Selenium
# Selenium 사용 실습(2) - 실습 프로젝트(1)

# selenium import
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 크롬 옵션 브라우져를 실행하지 않는다.
chrome_options = Options()
chrome_options.add_argument("--headless")

# webdriver 초기화 - headless 모드
browser = webdriver.Chrome("./webdriver/chrome/chromedriver", options=chrome_options)

# webdriver 초기화 - 브라우저 실행
# browser = webdriver.Chrome("./webdriver/chrome/chromedriver")

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920, 1280)

# 페이지 이동
browser.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")

# 1차 페이지 내용
# print("Before Page Contents : {}".format(browser.page_source))

# 제조사별 더보기 클릭1
# Explicitly wait

WebDriverWait(browser, 3).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]')
    )
).click()

# 제조사별 더보기 클릭2
# Implicitly wait
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

# 원하는 모델 카테고리 클릭
# //*[@id="selectMaker_simple_priceCompare_A"]/li[12]/label
WebDriverWait(browser, 2).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[12]/label')
    )
).click()

# 2차 페이지 내용
# print("After Page Contents : {}".format(browser.page_source))

time.sleep(2)

# bs4 초기화
soup = BeautifulSoup(browser.page_source, "html.parser")

# 소스코드 정리
# print(soup.prettify())

# # 메인 상품 리스트 선택
pro_list = soup.select("div.main_prodlist.main_prodlist_list > ul > li")

# # 상품 리스트 확인
# # print(pro_list)

# # 필요 정보 추출
for v in pro_list:
    # 임시 출력
    # print(v)

    if not v.find("div", class_="ad_header"):
        # 상품명, 이미지 , 가격
        print(v.select("p.prod_name > a")[0].text.strip())
        if v.find("img", class_="image_lazy"):
            print(v.select("a.thumb_link > img")[0]["data-original"])
        else:
            print(v.select("a.thumb_link > img")[0]["src"])
        print(v.select("p.price_sect > a")[0].text.strip())
    print()

# 브라우저 종료
browser.close()

# find와 select 차이 알기
