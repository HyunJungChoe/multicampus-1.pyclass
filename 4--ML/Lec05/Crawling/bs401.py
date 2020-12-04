import bs4 
htm_str = "<html><div>hello</div></html>"
result = bs4.BeautifulSoup(htm_str, 'html.parser')
print(result)
print(result.find('div').text)