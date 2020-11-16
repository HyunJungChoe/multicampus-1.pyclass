# csv.DictReader(파일변수) => ordered dict 형태로 데이터 불러오기

# 파일변수 = open('csv파일경로', 'r', encoding='utf-8/cp949')
# csv객체변수 = csv.DictReader(파일변수)

# with open('csv파일경로', 'r', encoding='utf-8/cp949') as 파일변수:
#   csv객체변수 = csv.DictReader(파일변수)


# https://www.data.go.kr/index.do
# data 폴더에 복사 붙여넣기
# 시도 대학별 기업규모에 따른 취업자수_2018.csv => 2018.csv
# 한국교통안전공단_대중교통 이용자유형별 이용인원(2017년).csv => traffic_2017.csv

import csv, os
# print(os.getcwd())
# os.chdir('data')
# print('2018.csv' in os.listdir(os.getcwd()))
# print('traffic_2017.csv' in os.listdir(os.getcwd()))

# 파일변수 = open('csv파일경로', 'r', encoding='utf-8/cp949')
# csv객체변수 = csv.DictReader(파일변수)
f = open('data/traffic_2017.csv', 'r', encoding='cp949')
csv_data = csv.DictReader(f)
# print(csv_data, type(csv_data))
# <csv.DictReader object at 0x0000023E4F223730> <class 'csv.DictReader'>
# 한 행이 딕셔너리 구조로 출력
# for item in csv_data:
#     print(item)

# 리스트안의 딕셔너리 구조로 변경하기
data_dict_list = []
for item in csv_data:
    data_dict_list.append(item)
print(data_dict_list)
f.close()

print(data_dict_list[0])
print('-'*50)
# 서울 데이타의 일반인 값은?
# 리스트명[인덱스값][키값]
print(data_dict_list[0]['일반인'])
print(data_dict_list[0]['어린이'])

# 제주지역의 대중교통 총 사용자수는 ?
# data_dict_list[?]['구분'] == '제주'

# 1) 구분 리스트 생성
city_list = []
for i in range(len(data_dict_list)):
    city_list.append(data_dict_list[i]['구분'])
print(city_list)

# 2) '제주' 인덱스값은?
print(city_list.index('제주'))

# 3) '제주' 전체 데이타 출력
print(data_dict_list[city_list.index('제주')])

# 4) '제주' 대중교통 총 사용자수
temp = data_dict_list[city_list.index('제주')]
print(temp, type(temp))
# print(int(temp['일반인'])+int(temp['어린이'])+int(temp['청소년']))
# 63008

# print(int(temp['일반인'])+int(temp['어린이'])+int(temp['청소년'])+int(temp['기타']))
# ValueError

sum = 0
for key in temp:
    try:
        sum += int(temp[key])
    except:
        pass
print(sum)

# 각 지역이름을 입력하면 총 사용자수가 출력되게 함수 정의하기
def city_total(city, m):
    city_list = city
    temp = data_dict_list[city_list.index(m)]
    sum = 0
    for key in temp:
        try:
            sum += int(temp[key])
        except:
            pass
    print(f'{m} 지역의 총 사용자수 = {sum}')

city_total(city_list, '제주')
city_total(city_list, '서울')

# 퀴즈 - 각 지역별 대중교통총사용자수를 아래와 같은 딕셔너리 구조로
#  생성하여 출력하여라
# {'서울': 4006394, '부산': 952394,
# '대구': 547517, '인천': 716825,
# '광주': 242717, '대전': 262872,
# '울산': 152289, '세종': 22677,
# '경기': 2816335, '강원': 84879,
# '충북': 117371, '충남': 148303,
# '전북': 118447, '전남': 120123, '경북': 165815,
# '경남': 253772, '제주': 63008}


with open('data/traffic_2017.csv', 'r') as f:
    csv_data = csv.DictReader(f)
    list_city = []
    list_user = []

    for row in csv_data:
        list_city.append(row['구분'])
        if row['기타'] == '':
            temp = '0'
        else:
            temp = row['기타']
        list_user.append(int(row['일반인'])+
                         int(row['어린이'])+
                         int(row['청소년'])+int(temp))

    # print(list_city)
    # print(list_user)
    korea_traffic_dict = {}
    for i in range(0, len(list_city)):
        # 딕셔너리변수[키] = 값
        korea_traffic_dict[list_city[i]] = list_user[i]
    print(korea_traffic_dict)


