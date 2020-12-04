import requests
import bs4

url = "https://finance.naver.com/item/main.nhn?code=215480"
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
#print(result.content)
#print(bs_obj.find('div', {'class':'today'}))
today =bs_obj.find('div', {'class':'today'})
print(today.find('span').text)
