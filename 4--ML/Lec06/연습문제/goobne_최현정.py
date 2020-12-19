from selenium import webdriver
from itertools import count
import pandas as pd
import time
from bs4 import BeautifulSoup
url = "http://www.goobne.co.kr/store/search_store.jsp"

# driver = webdriver.Chrome("chromedriver.exe")
driver = webdriver.Chrome('E:\pyclass\4--ML\chromedriver.exe')

driver.get(url)
time.sleep(4)

result =[]
for page in [0,1]:
    driver.execute_script("store.getList(%s)"%str(page+1))
    time.sleep(2)
    rcv_data = driver.page_source
    soupData = BeautifulSoup(rcv_data, "html.parser")
    for store_list in soupData.findAll('tbody', {'id':'store_list'}):
        for store_tr in store_list:
            tr_tag = list(store_tr.strings)
            store_name = tr_tag[1]
            store_phone = tr_tag[3]
            store_address = tr_tag[6]
            print(store_name,":",store_address, ":", store_phone)
            result.append([store_name]+[store_phone]+[store_address])

driver.close()
driver.quit()


goobnae_csv = pd.DataFrame(result, columns=('store', 'phone', 'address'))
goobnae_csv.to_csv('goobnae_최현정.csv',encoding='cp949',index =True)
