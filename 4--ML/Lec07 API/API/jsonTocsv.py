import json
#import csv
import pandas as pd
with open('서울특별시_관광지입장정보_2011_2016.json', encoding='utf-8') as input:
    df = pd.read_json(input)
df.to_csv("서울특별시_관광지입장정보_2011_2016.csv", encoding="cp949", index=False)