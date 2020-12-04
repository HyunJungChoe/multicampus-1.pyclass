# from bs4 import BeautifulSoup
# import pandas as pd
# import numpy as np

# print("version:")
# print(pd.__version__)
# print(np.__version__)

import bs4

htm_str="<html><div>Hello</div></html>"
result = bs4.BeautifulSoup(htm_str,"html.parser")
print(result.find('div').text)

