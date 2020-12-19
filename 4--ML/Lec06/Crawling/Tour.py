from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time 
from TourDB import MyDB
from TourObject import TourInfo
db = MyDB()
result = []
area = '영국'
url = 'http://tour.interpark.com'
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)
driver.find_element_by_id('SearchGNBText').send_keys(area)
driver.find_element_by_class_name('search-btn').click()


try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'boxTitle')))
except Exception as e:
    print("오류발생", e)

driver.implicitly_wait(2)
driver.find_element_by_css_selector('.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click()
time.sleep(1)
driver.execute_script("searchModule.SetCategoryList(1, '')")
time.sleep(2)
boxItems = driver.find_elements_by_css_selector('.oTravelBox>.boxList>li')
for item in boxItems:
    print("="*30)    
    print("상품명:"+item.find_element_by_css_selector('h5.proTit').text )
    print("가격  :"+item.find_element_by_css_selector('.proPrice').text )
    print("정보  :"+item.find_elements_by_css_selector('.info-row .proInfo')[1].text )
    obj = TourInfo(
        item.find_element_by_css_selector('h5.proTit').text,
        item.find_element_by_css_selector('.proPrice').text[:-1],
        item.find_elements_by_css_selector('.info-row .proInfo')[1].text.replace('출발 가능 기간 :',''),
        area
    )
    result.append(obj)
print(result, len(result))

for ele in result:
    db.tour_crawlingInsert(ele.title, ele.price, ele.term, ele.area)

print("클롤링 완료 DB 저장 끝!!!!")
driver.close()
driver.quit()
db.db_free()
import sys 
sys.exit()
