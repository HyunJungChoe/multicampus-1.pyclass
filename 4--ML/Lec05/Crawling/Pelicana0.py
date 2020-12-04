import urllib.request
from bs4 import BeautifulSoup
from itertools import count 
import pandas as pd
import ssl

def getPelicanaAdress(sido, result):
    for page in count():
        context = ssl._create_unverified_context()
        url = "https://pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=%s&page=%s" \
        %(urllib.parse.quote(sido), str(page+1))
        req = urllib.request.Request(url)
        respose = urllib.request.urlopen(req,context=context)

        soupData = BeautifulSoup(respose, "html.parser")
        store_table = soupData.find('table', {'class':'table mt20'})    
        tbody = store_table.find('tbody')
        bEnd = True
        for store in tbody.findAll('tr'):
            bEnd = False;
            tr_tag = list(store.strings)
            store_name = tr_tag[1]
            store_address = tr_tag[3]
            store_phone = tr_tag[5].strip()
            store_sido_gu = store_address.split()[:2]
            result.append([store_name]+ store_sido_gu+[store_address]+[store_phone])
        if(bEnd == True):
            return;

sido_list = ['서울특별시','부산광역시','대구광역시','제주특별자치도','광주광역시',
        '울산광역시','인천광역시','세종특별자치시','경기도','강원도','경상북도',
        '경상남도','충청북도','충청남도','전라북도','전라남도','대전광역시']
result = [];

print("페리카나 주소 크롤링 시작")
for sido in sido_list:
    getPelicanaAdress(sido, result)
print(result)
perincana_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'address', 'phone'))
perincana_table.head()
perincana_table.to_csv('perlicana.csv',encoding='cp949',index =True)                
print("페리카나 주소 크롤링 종료")
