import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
from itertools import count
import ssl 
from pelicanaDB import PelicanaDB
db = PelicanaDB()
result =[]
def getPlicanaAddress(result):
    for page in count():
        context = ssl._create_unverified_context()
        url = 'https://pelicana.co.kr/store/stroe_search.html?page=%s&branch_name=&gu=&si=' \
            %( str(page+1))
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req, context=context)
        soupData = BeautifulSoup(response, 'html.parser')
        store_table = soupData.find('table', {'class','table mt20'})
        tbody = store_table.find('tbody')
        stores = tbody.find_all('tr')
        bEnd = True
        for store in stores:
            bEnd = False
            tr_tag = list(store.strings)
            store_name = tr_tag[1]
            store_address = tr_tag[3]
            store_phone = tr_tag[5].strip()
            store_sido_gu = store_address.split()[:2]
            print(store_name, ":",store_address,":",store_sido_gu,":",store_phone)
            result.append([store_name]+store_sido_gu+ [store_address]+[store_phone])
        if(bEnd == True):
            return;

print("페리카나 주소 크롤링 시작")
getPlicanaAddress(result)
#pelicana_table = pd.DataFrame(result, columns=('store','sido','gungu','address','phone'))
#pelicana_table.to_csv('perlicana.csv', encoding='cp949', index=True)
print(len(result))
for store in result:
    if len(store) == 4 :
        db.pelicana_crawlingInsert(store[0],store[1], store[2], store[3], store[4])
print("페리카나 주소 크롤링 종료")
db.db_free()