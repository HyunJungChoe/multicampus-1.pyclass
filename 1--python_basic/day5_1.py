
# Review
# for 문
# 사용자정의함수
# 시간과 관련된 모듈과 사용법

# 시간과 관련된 모듈 임포트
import datetime
import time

now = datetime.datetime.now()
print(now)
# 2020-11-11 09:18:02.070485
print(now.year,'년', now.month,'월', now.day, '일')
# 2020 년 11 월 11 일

now = time.time()
print(now)
now = time.ctime()
print(now)
now = time.localtime(time.time())
print(list(now))
# 여러가지 출력 포맷 이용하기
# time.strftime('포맷코드1 포맷코드2', time.localtime(time.time()))
print(time.strftime('%Y . %B . %d . %A ', time.localtime(time.time())))
# 2020 . November . 11 . Wednesday

# 퀴즈
'''
오늘은 11 월  11 입니다.
1년을 기준으로 ?번째 날입니다.
'''

m = time.strftime("%m", time.localtime(time.time()))
d = time.strftime("%d", time.localtime(time.time()))
r = time.strftime("%j", time.localtime(time.time()))

print(f'오늘은 {m} 월  {d} 입니다.')
print(f'1년을 기준으로 {r} 번째 날입니다.')

num = -10
print(num, abs(num))

myList = [10, 67, 800, 65, -100]
myTuple = (10, 67, 800, 65, -100)
print(f'{myList}의 최대값은? {max(myList)}, 최소값은? {min(myList)}')
print(f'{myTuple}의 최대값은? {max(myTuple)}, 최소값은? {min(myTuple)}')
# [10, 67, 800, 65, -100]의 최대값은? 800, 최소값은? -100
# (10, 67, 800, 65, -100)의 최대값은? 800, 최소값은? -100

# 나누기 연산자 /(실수), //(정수)
# 나머지 연산자 %
# divmod(n1,n2) => 몫과 나머지 값을 구한다. => 튜플
print(divmod(100,33), type(divmod(100,33)))
# (3, 1) <class 'tuple'>

# enumerate(리스트/튜플/문자열 , 인덱스숫자 )
# 인덱스숫자로 구성된 리스트/튜플/문자열
# => enumerate 객체 생성
# => for .. in 하나씩아이템 출력 가능
# => 각각 튜플아이템으로 생성 (인덱스, 값)

result = enumerate(myTuple)
print(result)
# <enumerate object at 0x00000201ADD8ED00>
# 순차적으로 접근해서 출력
# (인덱스번호, 값) 튜플구조로 출력
for item in result:
    print(item, type(item))
# (0, 10)
# (1, 67)
# (2, 800)
# (3, 65)
# (4, -100)

# 인덱스 번호 새로 지정
result = enumerate(myTuple, 51)
for item in result:
    print(item, type(item))

result_dict = dict(enumerate(myTuple, 51))
for key in result_dict:
    print(key , '=>', result_dict[key])

result_list = list(enumerate(myTuple, 51))
for item in result_list:
    print(item)

# 튜플 리스트
print(result_list)
print(result_list[0][0])
# [(51, 10), (52, 67), (53, 800), (54, 65), (55, -100)]

# 문자열 => 딕셔너리
# result = dict(enumerate(myTxt, 11))
# print(result)

# 퀴즈1 :  5개의 값을 입력문을 이용하여 리스트로 저장한 후
# 최대값과 최소값을 출력한다.
'''
숫자를 입력하세요.. 56
숫자를 입력하세요.. 100
숫자를 입력하세요.. 240
숫자를 입력하세요.. 90
숫자를 입력하세요.. 45

[56, 100, 240, 90, 45]의 최대값은 240
[56, 100, 240, 90, 45]의 최소값은 45
'''

# 빈 리스트 생성
inList = []
for i in range(0,5):
    temp = int(input('숫자를 입력하세요'))
    inList.append(temp)

print(f'{inList}의 최대값은 {max(inList)}')
print(f'{inList}의 최소값은 {min(inList)}')


# 퀴즈2 :  divmod() 함수를 이용하여 다음과 같은 출력화면이 나오도록
# 프로그래밍 하여라
'''
몫 = 27
나머지 = 1
'''

# print(f'몫 = {divmod(55,2)[0]}')
# print(f'나머지 = {divmod(55,2)[1]}')

x, y = divmod(55,2)
print(f'몫 = {x}')
print(f'나머지 = {y}')

# 퀴즈 3 : 리스트를 양수로 모두 출력하는 함수를 정의하고 호출하여라
'''
# def absTrans(리스트변수) :
#       명령문 

# 함수 호출 
absTrans([-90, 100, -67, 55, -33])

# 결과 
[90, 100, 67, 55, 33]
'''

# def absTrans(list):
#     result = []
#     for item in list:
#         result.append(abs(item))
#     return result

# def absTrans(list):
#     for i in range(len(list)):
#         list[i] = abs(list[i])
#     return list

def absTrans(list):
    return [abs(i) for i in list]

print(absTrans([-90, 100, -67, 55, -33]))

# 아스키코드와 관련된 함수
# char() , ord()
# char(숫자) => 아스키코드값에 해당하는 문자나 숫자
# 문자의 아스키 코드 값을 돌려주는 함수
# 0에서 127 사이의 숫자를 각각 하나의 문자 또는 기호에
# ord(관련 문자나 숫자) => 아스키코드값
# char()과 반대되는 함수
# 대응시켜 놓은 코드표
# https://ko.wikipedia.org/wiki/ASCII

print('-'*20)
print(ord('A')) # 65
print(chr(65)) # A
print(ord('Z')) # 90
print(chr(90))

# 대문자 알파벳으로 구성된 리스트를 생성하여라
# result = ['A' .. 'Z']
result = []
for i in range(65, 91):
    result.append(chr(i))
print(result)

# 소문자 알파벳으로 구성된 리스트를 생성하여라
print(ord('a')) #97
print(ord('z')) #122
result = []
for i in range(97, 123):
    result.append(chr(i))
print(result)


# 입력받은 숫자로 구성된 리스트 생성하여라 (길이는 5)
# 빈 리스트를 생성한다.
# 입력문이 실행된다.
# 입력값이 숫자이면 리스트에 추가한다.
# 입력값이 숫자가 아니면 다시 입력문이 실행된다.
# 리스트의 전체길이가 5이면 입력을 종료한다.
# 리스트를 출력한다.

def makeNumList() :
    result = []
    while True:
        data = input('데이타 입력 => ')
        if data.isdigit():
            result.append(data)
            print('리스트가 추가되었습니다.')
        else:
            print('숫자가 아닙니다. 다시 입력해주세요')
        # 탈출 조건
        if len(result) == 5:
            break
    print(result)

# makeNumList()

# 퀴즈 : 문자열에서 숫자와 숫자가아닌문자의 갯수를 출력하여라
# testWord = 'Python1234Java4774'
'''
결과 >>
숫자 갯수 : ? 
문자 갯수 : ?
'''
testWord = 'Python1234Java4774'
def tmp():
    n = len(testWord)
    res1 = 0
    for i in testWord:
        if i.isdigit():
            res1 += 1
    print(res1, n - res1)
# tmp(testWord)

# dir(자료형) => Reference 기능
# 사용가능한 속성과 함수를 리스트 구조로 표시
print(dir('String'))
print(dir(True))
print(dir(100))
print(dir([1,2,3,4,5]))
print(dir((1,2,3,4,5)))
print(dir({1:'하나', 2:'둘'}))
print(dir({1,2,3,4,5}))
print('-'*10, '\n'*2)

# zip(리스트1, 리스트2 .. )
# zip 객체로 리턴 => for...in zip 문 이용해서 아이템 확인
# : 리스트의 각 아이템요소를 튜플화 구조로 묶어준다.
# list(zip 객체): [(아이템1,아이템2) ...]
# zip(*zip객체)
# : zip으로 묶어준 객체를 원래대로 풀어준다.

p1 = ['길동', '동미', '미영', '영철']
p1Gender= ['남','여','여','남']

result = zip(p1, p1Gender)
print(result)
for item in result:
    print(item)

# zip으로 리스트안의 튜플구조 해제하기 - unzip
# 변수1, 변수2 = zip(*리스트튜플이름)
# 리스트 튜플 정의
myListTupe = [('a','apart'),('y','yes'),('b','base')]
x, y = zip(*myListTupe)
print(f' x = {x}, {type(x)}')
print(f' y = {y}, {type(y)}')

# 딕셔너리 구조를 튜플 형태로 변경
# 딕셔너리  => 키 리스트, 값 리스트 => zip =>  unzip 튜플
myDict = {'a':'africa', 'd':'drama', 'm':'movie'}
print(f'myDict = {myDict}, {type(myDict)}')



