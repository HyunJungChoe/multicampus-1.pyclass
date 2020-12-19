import json 

dic_data= {'Name':'Jane', 'Age':43, 'Class':'Thrid'}
with open('result.json', 'w') as jsonfile:
    json.dump(dic_data, jsonfile)