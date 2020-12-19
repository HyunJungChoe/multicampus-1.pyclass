from bs4 import BeautifulSoup

with open('book.xml', 'r', encoding="utf-8") as book_xml:
    xml = book_xml.read()

soupdata = BeautifulSoup(xml,'lxml')
print(soupdata.findAll('book')[1].text)
# for boo_info in soupdata.find_all('book'):
#     print(boo_info.get_text())
