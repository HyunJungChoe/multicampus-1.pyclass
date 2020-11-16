
# import os
# print(os.getcwd())
# os.chdir('data')
# print(os.getcwd())
# print(os.listdir())
# print('population.csv' in os.listdir())
# print('data.csv' in os.listdir())

# 관련 모듈 임포트
import csv

# CSV 파일 읽기
# 파일변수
#  = open('csv파일경로', 'r', encoding='utf-8/cp949')
# csv객체변수 = csv.reader(파일변수)

import os
print(os.getcwd()) # C:\pyclass

f = open('data/data.csv', 'r', encoding='utf-8')
csv_data = csv.reader(f)
print(csv_data)
# csv객체
# <_csv.reader object at 0x000001CF21FD6DC0>
print('-'*50)
# for item in csv객체: 명령문
# csv 각행(레코드)이 리스트로 출력된다.
for item in csv_data:
    print(item)
print('-'*50)

# 2차원 형태의 리스트구조로 변환하기
f = open('data/data.csv', 'r', encoding='utf-8')
csv_data = csv.reader(f)
data_list = []
for item in csv_data:
    data_list.append(item)
f.close()
print('-'*50)
print(f'data_list={data_list}')
print(f'data_list 길이 ={ len(data_list) }')

# 2차원 리스트 출력하기
print('=' * 50)
for row in data_list:
    for col in row:
        print(col, end='\t')
    print()
    print('-'*50)

# 2차원 리스트의 인덱싱
print(data_list[0])
print(data_list[-1][1])

# 'kor' 데이타만 정수형 리스트로 생성하여라
# 1행은 제목 . 제외
korList = []
for i in range(1, len(data_list)):
    korList.append(int(data_list[i][2]))
print(korList, type(korList[0]))


# 'kor' 과목의 총점, 평균, 최고점, 최하점은?
# 리스트의 모든 합계  sum(리스트명)
# 리스트의 최소, 최대 max(리스트명) , min(리스트명)
# tot = 0
# for i in korList:
#     tot += i
# print(f'총점 = {tot}')
print(f'국어 총점 = {sum(korList)}')
print(f'국어 평균 = {sum(korList)/len(korList)}')
print(f'국어 최고점수 = {max(korList)}')
print(f'국어 최하점수 = {min(korList)}')


# 국어 점수의 최고점을 받은 학생의 이름은?
# 값에 해당하는 인덱스번호를 출력하는 함수
# 리스트이름.index(값)
# 알고리즘
# 국어점수의 최고점
# 리스트이름.index(국어점수의 최고점 ) => 인덱스번호
# 리스트이름[인덱스번호][이름인덱스번호]
print('-'*50)
print(f'국어 최고점수 = {max(korList)}')
print(f'국어 최고점수에 해당하는 행인덱스 = {korList.index(max(korList))}')
print(f'국어 최고점수의 학생이름은? = {data_list[korList.index(max(korList))+1][1]}')

# 퀴즈1 : 4과목('kor', 'eng', 'mat', 'bio')의 총점 구하기

# 리스트 초기화
korList = []
engList = []
matList = []
bioList = []

for i in range(1, len(data_list)):
    korList.append(int(data_list[i][2]))
    engList.append(int(data_list[i][3]))
    matList.append(int(data_list[i][4]))
    bioList.append(int(data_list[i][5]))
print(f' kor 총점 = { sum(korList)}')
print(f' eng 총점 = { sum(engList)}')
print(f' mat 총점 = { sum(matList)}')
print(f' bio 총점 = { sum(bioList)}')

print(korList)


# 퀴즈2 : 4과목의 전체 평균 구하기
print(f' kor 평균 = { sum(korList)/len(korList)}')
print(f' eng 평균 = { sum(engList)/len(engList)}')
print(f' mat 평균 = { sum(matList)/len(matList)}')
print(f' bio 평균 = { sum(bioList)/len(bioList)}')

# 퀴즈3 : 전체 총점이 가장 높은 학생의 이름은?
# 각 학생 레코드의 총점 리스트 만들기
totalList = []

for i in range(1, len(data_list)):
    totalList.append(int(data_list[i][2])+int(data_list[i][3])+int(data_list[i][4])+int(data_list[i][5]))
print(totalList)
print(max(totalList))
print(totalList.index(max(totalList)))
print(data_list[totalList.index(max(totalList))+1])
print(data_list[totalList.index(max(totalList))+1][1])

print('\n\n')
print('='*50)
# with문을 이용하여 CSV 파일 읽기
# with open('csv파일경로', 'r', encoding='utf-8/cp949') as 파일변수:
#   csv객체변수 = csv.reader(파일변수)

# 미국 주별 인구수
# data/population.csv
with open('data/population.csv', 'r', encoding='utf-8') as f:
    csv_data = csv.reader(f)
    # 행으로 출력하기
    # for item in csv_data:
    #     print(item)

    # 2중 리스트구조로 변경하기
    data_list2 = []
    for item in csv_data:
        data_list2.append(item)

    # 5개만 출력하기
    print(data_list2[:5])
    print(len(data_list2))

    #data_list2 리스트에서 첫번째는 제외시켜라
    data_list2 = data_list2[1:]
    print(data_list2[:3])

    #인구와 관련된 데이타를 정수 리스트로 생성하여라.
    # ValueError : 쉼표때문에 정수로 바로 변경은 불가능
    # print(int('4,780,131'))
    # 특정문자열 찾아서 교체하기
    # 문자열변수.raplace(old, new)
    # test = '4,780,131'
    # print(test, type(test))
    # test = int(test.replace(',',''))
    # print(test, type(test))

    population_list = []
    for i in range(len(data_list2)):
        temp = int(data_list2[i][1].replace(',', ''))
        population_list.append(temp)
    print(population_list)

    # 퀴즈1 . 가장 많은 인구수는? max()
    print(f'가장 많은 인구수는? {max(population_list)}')

    # 퀴즈2 . 가장 작은 인구수는? min()
    print(f'가장 작은 인구수는? {min(population_list)}')

    # 퀴즈3. 가장 인구가 많은 주(State), 가장 인구가 적은 주(state)는?
    print(f'가장 인구가 많은 주(State)? {population_list.index(max(population_list))}')
    print(f'가장 인구가 많은 주(State)? {data_list2[population_list.index(max(population_list))]}')
    print(f'가장 인구가 많은 주(State)? {data_list2[population_list.index(max(population_list))][0]}')

    print(f'가장 인구가 적은 주(State)? {population_list.index(min(population_list))}')
    print(f'가장 인구가 적은 주(State)? {data_list2[population_list.index(min(population_list))]}')
    print(f'가장 인구가 적은 주(State)? {data_list2[population_list.index(min(population_list))][0]}')


print(f'가장 인구가 많은 주(State)? {data_list2[population_list.index(max(population_list))]}')
print(f'가장 인구가 많은 주(State)? {data_list2[population_list.index(max(population_list))][0]}')

print(f'가장 인구가 적은 주(State)? {population_list.index(min(population_list))}')
print(f'가장 인구가 적은 주(State)? {data_list2[population_list.index(min(population_list))]}')
print(f'가장 인구가 적은 주(State)? {data_list2[population_list.index(min(population_list))][0]}')

