
# 튜플
# CRUD : Create Read Update(Add)
# 튜플 생성1 (초기값 지정)
# 튜플변수 = (값1, 값2...)

# 튜플 생성2 (초기값 지정)
# 튜플변수 = 값1, 값2...

# 튜플 생성3 (빈 튜플)
# 튜플변수 = ()

t1 = ()
t2 = (100, 200, 300)
t3 = '가','나','다'
print(f't1 = {t1}, 자료형 = {type(t1)}')
print(f't1 = {t2}, 자료형 = {type(t2)}')
print(f't1 = {t3}, 자료형 = {type(t3)}')

# 튜플 인덱싱
# 튜플변수[인덱싱위치번호] , 0부터 시작
# 튜플 슬라이싱
# 튜플변수[start:end:step]

# 튜플은 값을 새로 추가할 수 있는가?
# +=  연산자 이용
# 튜플변수 += (값1,)
# 한개 추가시에는 쉼표(,) 주의
# 튜플변수 += (값1, 값2...)
print(t1, len(t1))
t1 += ('가','나','다')
print(t1, len(t1))
# t1 += ('스크립트')
# TypeError: can only concatenate tuple (not "str") to tuple
t1 += ('스크립트',)
print(t1, len(t1))

# 튜플의 연산자 + : 튜플끼리 더하기
# 튜플의 연산자 * : 튜플 요소 반복
print('-'*20)
print(t2)
print(t3)
print(t2+t3)
print(t3*3)

# 각각 튜플 변수 정의하기
# 튜플전체변수 = (변수1, 변수2...) = (값1, 값2...)
color = (c1, c2, c3) = ('red','green','blue')
print('-'*20)
print(color)
print(c1)
print(c2)
print(c3)

# 튜플 함수
# 튜플변수.count(값)
# 튜플변수.index(값)
myTuple = (100, 100, 300, 100, True, True, '나','다라마')
print('-'*20)
print(myTuple)
print(myTuple.count(100)) # 3
print(myTuple.index(True)) # 4

# 튜플 => 문자열
# : str(튜플변수나 값)
# : 구분자.join(튜플변수나 값)
#  주의사항은 join() 사용시에는 튜플의 자료형이 문자열이어야 한다.
# 튜플 => 리스트 : list(튜플변수나 값)
myTuple = (1, 2, 3, 4, 5)
myTuple2 = ('a','b','c')
print('-'*20)
print(myTuple, type(myTuple))
result1 = str(myTuple)
# result2 = ' / '.join(myTuple) # 숫자로 구성된 튜플이라서 에러 발생
# TypeError: sequence item 0: expected str instance, int found
result2 = ' / '.join(myTuple2)
result3 = list(myTuple)
print(result1, type(result1)) # (1, 2, 3, 4, 5) <class 'str'>
print(result2, type(result2)) # a / b / c <class 'str'>
print(result3, type(result3)) # [1, 2, 3, 4, 5] <class 'list'>

# 중첩 튜플
t1 = ((1,2,3),(4,5,6))
print('-'*20)
print(t1, len(t1)) # ((1, 2, 3), (4, 5, 6)) 2
print(t1[0]) # (1, 2, 3)
print(t1[0][0]) # 1
# 튜플 리스트란?
# 리스트안에 튜플이 삽입되어 있는 구조
tupleA = (100, 200, 300)
tupleB = ('가','나','다')
Resultlist = [tupleA, tupleB]
print('-'*20)
print(Resultlist, len(Resultlist), type(Resultlist))
print(Resultlist[0], len(Resultlist[0]), type(Resultlist[0]))
print(Resultlist[0][0], type(Resultlist[0][0]))

# 퀴즈
# 아래와 같이 튜플을 정의한 후 출력한다.
'''
튜플 리스트 :  ('강아지', '토끼', '돼지', '곰')
튜플 요소 추가 후 :  ('강아지', '토끼', '돼지', '곰', '호랑이')
튜플의 0-3번째 요소 표시 :  ('강아지', '토끼', '돼지', '곰')
'강아지' 요소의 위치값은?   0
튜플을 문자열로 변환하여 출력 :  강아지,토끼,돼지,곰,호랑이
튜플을 리스트로 변환하여 출력 : :  ['강아지', '토끼', '돼지', '곰', '호랑이']
'''
tupleA = ('강아지', '토끼', '돼지', '곰')
print(f'튜플 리스트 : {tupleA}')
tupleA += '호랑이',
print(f'튜플 요소 추가 후 : {tupleA}')
print(f'튜플의 0-3번째 요소 : {tupleA[:4]}')
print(f"\'강아지\'요소의 위치값은?: {tupleA.index('강아지')}")
print(f"튜플을 문자열로 변환하여 출력 : { ','.join(tupleA)}")
print(f'튜플을 리스트로 변환하여 출력 : {list(tupleA)}')


