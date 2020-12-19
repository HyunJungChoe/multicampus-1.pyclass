import json

with open('employees.json', 'r', encoding='utf8') as file:
    content = file.read()
    json_data = json.loads(content)
    print(json_data['employees'])

print(json_data['employees'][0]['firstName'])
print(json_data['employees'][1]['firstName'])
print(json_data['employees'][2]['firstName'])

for item in json_data['employees']:
    print(item.keys())