from selenium import webdriver
# pip install selenium
from itertools import count
import time
from bs4 import BeautifulSoup
url = "http://www.goobne.co.kr/store/search_store.jsp"

# 크롬 드라이버로 url가져오기  
driver = webdriver.Chrome('E:/pyclass/4--ML/Lec05/Crawling/chromedriver.exe')
driver.get(url)

#페이지 옮기기
time.sleep(3)
driver.execute_script("store.getList('7')")
time.sleep(3)
driver.execute_script("store.getList('9')")
time.sleep(3)
driver.execute_script("store.getList('2')")


# time.sleep(4)
# for page in [0,1]:
#     driver.execute_script("store.getList(%s)"%str(page+1))
#     time.sleep(2)
#     rcv_data = driver.page_source
#     soupData = BeautifulSoup(rcv_data, "html.parser")
#     for store_list in soupData.findAll('tbody', {'id':'store_list'}):
#         for store_tr in store_list:
#             tr_tag = list(store_tr.strings)
#             store_name = tr_tag[1]
#             store_phone = tr_tag[3]
#             store_address = tr_tag[6]
#             print(store_name,":",store_address, ":", store_phone)

# driver.close()
# driver.quit()
