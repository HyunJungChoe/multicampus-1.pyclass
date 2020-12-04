import urllib.request
from bs4 import BeautifulSoup
import ssl
context = ssl._create_unverified_context()
url = "https://pelicana.co.kr/store/stroe_search.html?page=111&branch_name=&gu=&si="
req = urllib.request.Request(url)
respose = urllib.request.urlopen(req,context=context)

soupData = BeautifulSoup(respose, "html.parser")
store_table = soupData.find('table', {'class':'table mt20'})
#print(store_table)
tbody = store_table.find('tbody')
for store in tbody.findAll('tr'):
    tr_tag = list(store.strings)
    store_name = tr_tag[1]
    store_address = tr_tag[3]
    store_phone = tr_tag[5].strip()
    store_sido_gu = store_address.split()[:2]
    print(store_name,":",store_address,":", store_sido_gu,":", store_phone)

    