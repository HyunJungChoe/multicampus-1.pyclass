

# random 난수 함수들
# 외장모듈 필요
# import random
# random.randint(start, end)
# : start~end 사이의 정수 난수
# random.choice(리스트)
# : 리스트에서 랜덤하게 뽑는다.
# random.shuffle(리스트)
# : 리스트를 랜덤하게 섞는다.

import random

# 범위내에서 정수 뽑기
print(f' 1~10 사이의 숫자 뽑기 => { random.randint(1, 10)}')
print(f' 1~10 사이의 숫자 뽑기 => { random.randint(1, 10)}')
print(f' 1~10 사이의 숫자 뽑기 => { random.randint(1, 10)}')

# 리스트에서 하나 뽑기
eventList = ['꽝', '카니발', '5000만원', '스타벅스 10만원 상품권', '캠핑카']
print(f' 뽑기1 => { random.choice(eventList)}')
print(f' 뽑기2 => { random.choice(eventList)}')
print(f' 뽑기3 => { random.choice(eventList)}')
'''
 뽑기1 => 5000만원
 뽑기2 => 꽝
 뽑기3 => 스타벅스 10만원 상품권
'''
# 실수 난수
print(random.random())

# 리스트 섞기
print(f'eventList = {eventList}')
random.shuffle(eventList)
print(f'eventList = {eventList}')
random.shuffle(eventList)
print(f'eventList = {eventList}')

# 학생중에서 2명을 오늘의 청소 당번으로 하려고 한다.
# random.shuffle() 함수를 이용하여 2명만 출력하여라.
studentList = ['기대주', '하민수', '이동백', '김철수', '홍길동', '이승기', '김남길']

# 학생중에서 2명을 오늘의 청소 당번으로 하려고 한다.
# random.shuffle() 함수를 이용하여 2명만 출력하여라.
studentList = ['기대주', '하민수', '이동백', '김철수', '홍길동', '이승기', '김남길']
def choicePerson(list):
    random.shuffle(list)
    print(list[0:2])

choicePerson(studentList)
choicePerson(studentList)

# 리스트에서 짝수만 추출하여라
list1 = [10, 56, 77, 33, 88, 100]

# filter 함수 없이 프로그래밍
print(f'list1 => { list1 }')
result = []
for item in list1:
    if item%2 == 0:
        result.append(item)
print(f'결과 => { result }')

# filter 함수에 사용될 함수 정의
# 원소하나에 대해서 짝수인지 판독
def odd(num):
    if num%2 == 0:
        return True
print(odd(100)) # True
print(odd(55)) # None

# filter에 적용
print(filter(odd, list1))
# <filter object at 0x0000016AF28E8640>
for i in filter(odd, list1):
    print(i)
print(list(filter(odd, list1)))

print(f'결과 => { list(filter(odd, list1)) }')

# 아래 리스트에서 양수만 리스트로 출력하여라
numlist = [10, -30, 20, 5, -100]
print(f'numlist = {numlist}')
# 방법1 => 일반함수
def positive(list):
    result = []
    for item in list:
        if item>0:
            result.append(item)
    return result
print(f' 결과1 = {positive(numlist)}')

# 방법2 => 함수+filter
def positiveOne(n):
    return n>0
# print(positiveOne(90))
# print(positiveOne(-99))
print(f' 결과2 = {list(filter(positiveOne,numlist))}')

# 방법3 => 람다함수+filter
# f = lambda n:n>0
# print(f(100))
# print(f(-100))
print(f' 결과3 = {list(filter(lambda n:n>0,numlist))}')


# map() 함수
# map(정의된함수나 lambda함수,데이타(리스트,튜플))
# -> map오브젝트 생성
# list(map(정의된함수나 lambda함수, 데이타(리스트,튜플)))
# 데이타 요소를 정의된함수의 결과값으로 리턴한다.
# 결과값을 리스트 요소로 추가
#
# 리스트의 제곱을 구해서 새로운 리스트로 만들기
numlist2 = [1,2,3,4] # 결과 => [1, 4, 9, 16]

# 방법1 = 일반함수
def power_list(list):
    result = []
    for item in list:
        result.append(item**2)
    return result
print(f'방법1 : {power_list(numlist2)}')

# 방법2 = 함수 + map()
def power_one(n):
    return n**2
# print(power_one(3))
# print(f'방법2 : {map(power_one, numlist2)}')
# 방법2 : <map object at 0x000001FF2DE08340>
print(f'방법2 : {list(map(power_one, numlist2))}')

# 방법3 = 람다 함수 + map()
# f = lambda n:n**2
# print(f(4))
print(f'방법3 : {list(map(lambda n:n**2, numlist2))}')

#두 리스트에서 인덱스가 같은 값을 서로 곱한 후 리스트로 만들기
list1 = [2,3,7]
list2 = [4,5,9]

print('='*30)
print(list1+list2)
print(list1*5)
# print(list1*list2)
# TypeError: can't multiply sequence by non-int of type 'list'

# 방법1 => 일반함수
def make_mullist(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i]*list2[i])
    return result
print(f'list1={list1}, list2={list2}')
print(f'방법1 : {make_mullist(list1, list2)}')


# 방법2 => 함수 + map()
def mul_two(x, y):
    return x*y
print(f'방법2 : {list(map(mul_two, list1, list2))}')


# 방법3 => 람다함수 + map()
# f = lambda x,y:x*y
# print(f(10,22))
print(f'방법3 : {list(map(lambda x,y:x*y, list1, list2))}')


#----------------------------------------------------------------
# # 퀴즈3
# aList = [78,90,80,50]
# bList = [8,100,34,60]
# 두개의 리스트 요소중에서 최대값과 최소값을 출력하여라
'''
aList = [78,90,80,50]
bList = [8,100,34,60]

최소값 : 8
최대값 : 100
'''
aList = [78,90,80,50]
bList = [8,100,34,60]
res1 = max(aList)
res2 = min(bList)
print(f'최소값 : {res2}')
print(f'최대값 : {res1}')

# 퀴즈 4
# enumerate() 함수를 이용하여 아래 리스트를
# 시작 인덱스가 1이 되게 자료 구조를 생성하고
# 아래 형태로 출력한다.
'''
foodList = ['감자탕', '떡국', '모밀냉면', '연어덮밥', '케이준 샐러드']

1 번째 메뉴: 감자탕
2 번째 메뉴: 떡국
3 번째 메뉴: 모밀냉면
4 번째 메뉴: 연어덮밥
5 번째 메뉴: 케이준 샐러드

'''
foodList = ['감자탕', '떡국', '모밀냉면', '연어덮밥', '케이준 샐러드']
res1 = enumerate(foodList, 1)
for i, v in res1:
  print(f"{i}번째 메뉴: {v}")



# 퀴즈 5
# 아래는 리스트를 딕셔너리 리스트(리스트안의 딕셔너리 구조)로 변경하는 프로그래밍이다.
# 이때 딕셔너리 키는 'user숫자' 형태이다.
# map 함수를 이용한 구조로 변경하여라
'''
# 리스트 => 딕셔너리 리스트로 변경 코드 
valueList = ['양준일', '노사연', '구창모', '조용원', '김정화']

def makeDict(valueList):
    result = []
    for i in range(0, len(valueList)):
        temp = {}
        temp['user'+str(i+1)] = valueList[i]
        result.append(temp)
    return result

print(f'\n 결과 >> \n valueList = {valueList}')
print((f' \n 딕셔너리 리스트 구조로 변경 => \n {makeDict(valueList)}'))
'''

'''
 결과 >>
 valueList = ['양준일', '노사연', '구창모', '조용원', '김정화']

 딕셔너리 리스트 구조로 변경 => 
 [{'user1': '양준일'}, {'user2': '노사연'}, {'user3': '구창모'}, {'user4': '조용원'}, {'user5': '김정화'}]
'''

'''
 map함수 이용 결과 >> 
 valuelist = ['양준일', '노사연', '구창모', '조용원', '김정화']
 [{'user1': '양준일'}, {'user2': '노사연'}, {'user3': '구창모'}, {'user4': '조용원'}, {'user5': '김정화'}]
'''

print('\n\n퀴즈5')

# 일반 함수 이용
valueList = ['양준일', '노사연', '구창모', '조용원', '김정화']
def makeDict(valueList):
    result = []
    for i in range(0, len(valueList)):
        temp = {}
        temp['user'+str(i+1)] = valueList[i]
        result.append(temp)
    return result

print(f'\n 결과 >> \n valueList = {valueList}')
print((f' \n 딕셔너리 리스트 구조로 변경1 => \n {makeDict(valueList)}'))
print('-'*20)

# 함수 + map 이용
def makeDict2(numKey, value):
    result = {'user' + str(numKey): value}
    return result

# print(makeDict2(1, '양준일'))
# {'user1': '양준일'}
# numKey = list(range(1, len(valueList)+1))
# print(numKey)
print(list(map(makeDict2, list(range(1, len(valueList)+1)), valueList )))


# 퀴즈 6
# 퀴즈5의 딕셔너리 리스트(리스트안의 딕셔너리 구조)로 변경하는 프로그래밍을
# map 함수안에 lambda 함수를 이용한 구조로 변경하여라

'''
 map함수와 lambda 이용 결과 >> 
 valuelist = ['양준일', '노사연', '구창모', '조용원', '김정화']
 [{'user1': '양준일'}, {'user2': '노사연'}, {'user3': '구창모'}, {'user4': '조용원'}, {'user5': '김정화'}]
'''

print('\n\n퀴즈6')

# def makeDict2(numKey, value):
#     result = {'user' + str(numKey): value}
#     return result

# f = lambda numKey, value:{'user' + str(numKey): value}
# print(f(1, '양준일'))
print(list(map(lambda numKey, value:{'user' + str(numKey): value}, list(range(1, len(valueList)+1)), valueList )))
print(list(map(lambda numKey, value:{'user' + str(numKey): value}, list(range(1, len(valueList)+1)), valueList )))


#  퀴즈7
# 아래의 2개의 리스트를 튜플 리스트(리스트안에 튜플 구조)로 zip() 함수를 이용하여 변경하여라
# mKind = ['발라드', '댄스', '클래식', 'OST']
# mTitle = ['거리에서', 'DNA', '소녀의 기도', '썸머']

'''
첫번째 리스트 = ['발라드', '댄스', '클래식', 'OST']
두번째 리스트 = ['거리에서', 'DNA', '소녀의 기도', '썸머']
튜플 리스트로 변경 
 [('발라드', '거리에서'), ('댄스', 'DNA'), ('클래식', '소녀의 기도'), ('OST', '썸머')]
 <class 'list'>

('발라드', '거리에서') <class 'tuple'>
('댄스', 'DNA') <class 'tuple'>
('클래식', '소녀의 기도') <class 'tuple'>
('OST', '썸머') <class 'tuple'>
'''
mKind = ['발라드', '댄스', '클래식', 'OST']
mTitle = ['거리에서', 'DNA', '소녀의 기도', '썸머']
print(f'\n\n첫번째 리스트 = {mKind}')
print(f'두번째 리스트 = {mTitle}')
result = list(zip(mKind, mTitle))
print(f'튜플 리스트로 변경 \n {result}')
print(type(result))
for i in result:
    print(i, type(i))

# 퀴즈 8
# 아래는 퀴즈 7의 결과 튜플 리스트이다. 딕셔너리 구조로 변경하고 출력하여라
'''
튜플리스트 [('발라드', '거리에서'), ('댄스', 'DNA'), ('클래식', '소녀의 기도'), ('OST', '썸머')]
딕셔너리로 변경 
 {'발라드': '거리에서', '댄스': 'DNA', '클래식': '소녀의 기도', 'OST': '썸머'}

발라드  :  거리에서 <class 'str'>
댄스  :  DNA <class 'str'>
클래식  :  소녀의 기도 <class 'str'>
OST  :  썸머 <class 'str'>
'''
print('\n\n 튜플리스트' , result)
print(f'딕셔너리로 변경 \n {dict(result)}\n')
result_dict = dict(result)
for key in result_dict:
    print(f'{key} : {result_dict[key]} {type(result_dict[key])}')

# 퀴즈 9
# 아래는 5~10까지의 곱을 구하는 프로그래밍이다.
# lambda 함수, reduce()를 이용한 구조로 변경하여라
# reduce() 함수 임포트 명령어는?
# import functools as f

'''
print('-'*20)
numList = list(range(5,11))
print(f'\n\nnumList = {numList}')

def fact_f1(numList):
    result=1
    txtList = []
    for i in numList:
        result *= i
        txtList.append(str(i))
    return txtList, result

print(f'\n \n numList = {numList}')
print(f' 5~10까지의 곱 >> \n {" * ".join(fact_f1(numList)[0])} = {fact_f1(numList)[1]}\n\n')
'''
'''
 numList = [5, 6, 7, 8, 9, 10]
 5~10까지의 곱 >> 
 5 * 6 * 7 * 8 * 9 * 10 = 151200
'''
'''
lambda 함수, reduce() 이용 >> 5~10까지의 곱 >> 
 numList = [5, 6, 7, 8, 9, 10]
5 X 6 X 7 X 8 X 9 X 10  =  151200
'''
# 일반 함수 이용
myString = 'a4+5b6&word*bn%~564^3'
def filterList(txt):
    result = []
    for i in range(0,len(txt)):
       #  숫자와 글자가 아니라면 리스트에 추가
       if not (txt[i].isdigit() or txt[i].isalpha()) :
           result.append(txt[i])
    return result

print('-'*20)
print(f'\n\n myString = {myString}')
print(f' 숫자와 글자 제외 결과 리스트 = {filterList(myString)}')
print(f' 총 갯수 = {len(filterList(myString))}')

# 함수 + filter 함수 이용
def filterItem(c):
    if not (c.isdigit() or c.isalpha()):
        return True

# print(filterItem('a'))
# print(filterItem('8'))
# print(filterItem('*'))
print('-'*30)
print(f' 숫자와 글자 제외 결과 리스트 = {list(filter(filterItem, myString))}')
print(f' 총 갯수 = {len(list(filter(filterItem, myString)))}')

# 함수 + filter 함수 이용
# f = lambda c: not(c.isdigit()) and not(c.isalpha())
# f = lambda c: not (c.isdigit() or c.isalpha())
# print(f('a'))
# print(f('8'))
# print(f('*'))

print('-'*30)
print(f' 숫자와 글자 제외 결과 리스트 = {list(filter(lambda c: not(c.isdigit()) and not(c.isalpha()), myString))}')
print(f' 총 갯수 = {len(list(list(filter(lambda c: not(c.isdigit()) and not(c.isalpha()), myString))))}')





