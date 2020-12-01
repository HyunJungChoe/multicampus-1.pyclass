
# 파이썬에 외부 자료 이용하기
# txt, csv, xml, json
# html, webURL

# 파일변수 = open('csv파일경로', 'r', encoding='utf-8/cp949')
# csv객체변수 = csv.reader(파일변수)   # 2중 리스트
# csv객체변수 = csv.DictReader(파일변수) # 리스트안의 딕셔너리
# 파일변수.close()

# with open('csv파일경로', 'r', encoding='utf-8/cp949') as 파일변수:
    # csv객체변수 = csv.reader(파일변수)   # 2중 리스트
    # csv객체변수 = csv.DictReader(파일변수) # 리스트안의 딕셔너리

import csv, os

print(os.getcwd())

# 2차원 리스트
with open('data/2018.csv', 'r') as f:
    csv_data1 = csv.reader(f)
    # for item in csv_data1:
    #     print(item)
    data_list1 = []
    for item in csv_data1:
        data_list1.append(item)
    print(data_list1)
    # 첫번째 리스트 제외
    data_list1 = data_list1[1:]
    print(data_list1)
    print(len(data_list1))

# 딕셔너리 리스트
with open('data/2018.csv', 'r') as f:
    csv_data2 = csv.DictReader(f)
    # for item in csv_data2:
    #     print(item)

    # 리스트화1
    # data_list2 = []
    # for item in csv_data2:
    #     data_list2.append(item)

    # 리스트화2
    data_list2 = [item for item in csv_data2]
    print(data_list2)

    # 1000명 이상인 회사에 들어간 취업자수가 가장 많은 도시는?
    # 지역 필드를 리스트로 만들기
    # city_list = []
    # for item in data_list2:
    #     city_list.append(item['지역'])

    city_list = [item['지역'] for item in data_list2]
    print(f'city_list = {city_list}')

    # 1000명이상 필드를 정수 리스트로 만들기
    # employ1000_list = []
    # for item in data_list2:
    #     temp = int(item['1000명이상'].replace(',',''))
    #     employ1000_list.append(temp)

    employ1000_list = [int(item['1000명이상'].replace(',','')) for item in data_list2]
    print(f'employ1000_list = {employ1000_list}')
    # print(type(employ1000_list[0])) #<class 'str'>

    # 1000명이상 필드에서 최대값은?
    print(max(employ1000_list))

    # 1000명이상 필드에서 최대값을 갖는 인덱스 번호는?
    print(employ1000_list.index(max(employ1000_list)))

    # 1000명 이상인 회사에 들어간 취업자수가 가장 많은 도시는?
    num = employ1000_list.index(max(employ1000_list))
    print(f' 1000명 이상인 회사에 들어간 취업자수가 가장 많은 도시는?  {city_list[num]}' )

    # 퀴즈 => 100인 미만의 회사에 들어간 취업자수가 가장 적은 도시는?

    # 3개의 필드에서 리스트 각각 생성하기
employ_list1 = [int(item['1-5인미만'].replace(',', '')) for item in data_list2]
employ_list2 = [int(item['6-50인미만'].replace(',', '')) for item in data_list2]
employ_list3 = [int(item['51-100인미만'].replace(',', '')) for item in data_list2]
print(employ_list1)
print(employ_list2)
print(employ_list3)
# print(employ_list1+employ_list2+employ_list3)
employ_list4 = []
for i in range(len(employ_list1)):
    temp = employ_list1[i] + employ_list2[i] + employ_list3[i]
    employ_list4.append(temp)
print(employ_list4)

print(min(employ_list4))
print(employ_list4.index(min(employ_list4)))
num = employ_list4.index(min(employ_list4))
print(f' 100인 미만의 회사에 들어간 취업자수가 가장 적은 도시는?  {city_list[num]}')
