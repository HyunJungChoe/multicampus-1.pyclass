import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
from itertools import count
import ssl 
import time
from selenium import webdriver

url = 'http://www.goobne.co.kr/store/search_store.jsp'

# driver = webdriver.Chrome('chromedriver.exe')
# driver = webdriver.Chrome('4--ML/chromedriver.exe')
driver = webdriver.Chrome('E:/pyclass/4--ML/Lec05/Crawling/chromedriver.exe')
driver.get(url)
time.sleep(3)
driver.execute_script("store.getList('7')")
time.sleep(2)
rcv_data = driver.page_source
soupData = BeautifulSoup(rcv_data, "html.parser")

for storelist in soupData.findAll('tbody', {'id':'store_list'}):
    for strore_tr in storelist:
        tr_tag = list(strore_tr.strings)
        store_name = tr_tag[1]
        store_phone = tr_tag[3]
        store_address = tr_tag[6]
        print(store_name, ":", store_address)
 
driver.close()
driver.quit()



