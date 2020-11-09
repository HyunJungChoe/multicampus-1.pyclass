# range(start, end , step)
# start~ (end-1)까지 step만큼 차례대로 숫자 생성
# range 객체로 생성되므로
# 실제 출력을 확인하려면 리스트, 튜플, 집합 형태로 자료형 변경

print(range(0,10))
# range(0, 10)
print(list(range(0,10)))
print(tuple(range(0,10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(list(range(2, 21, 2)))
print(set(range(0,31,3)))
print(set(range(10)))
print(dict(enumerate(list(range(10, 101, 10)))))


# for 문과 range
# for 인덱스변수 in range(start,end,step):
#   명령문

# 1~10까지 출력하기
for i in range(1,11):
    print(i)

# 1~10까지 홀수만 출력하기
for i in range(1,11,2):
    print(i, end=' / ')
print('\n','-'*20)

# 1~100사이의 합 구하기
sum = 0
for i in range(1, 101):
    sum += i
print(sum)
print('\n','-'*20)

# 1~27 에서 5의 배수만 빼고 출력하기
for i in range(1,28):
    if i%5 == 0:
        continue
    print(i, end=' ')
print('\n\n-----------------')

# 퀴즈 : 다중 for 문을 이용하여 구구단 출력
#  아래의 while 반복문을 for 문을 이용하여 수정하여라.
# cnt1 = 2
# while cnt1<=9:
#     print(f' { cnt1 } 단')
#
#     cnt2 = 1
#     while cnt2<=9:
#         print(f' {cnt1} X {cnt2} = {cnt1*cnt2}')
#         cnt2 += 1
#
#     print('-'*20)
#     cnt1 += 1

# 리스트 for = 리스트 내포
# 리스트 안에 for 문이 내포된 형태
# 결과값으로 구성된 리스트가 생성된다.
# 리스트변수 = [ 결과값 for 명령문 ]

# 1~10까지 숫자로 이루어진 리스트를 만들어라

numList1 = []
for i in range(1,11):
    numList1.append(i)
print('numList1 = ',numList1)
# numList1 =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numList2 = [ i for i in range(1,11)]
print('numList2 = ',numList2)


# 3단의 결과값으로 리스트를 만들어라
numList2 = [ i*3 for i in range(1,10)]
print('numList2 = ',numList2)

# 3단의 결과값에서 -1 한 값으로 리스트를 만들어라
numList2 = [ i*3-1 for i in range(1,10)]
print('numList2 = ',numList2)

# 아래와 같은 형태로 리스트를 만들어라
# ['*', '**', '***' .... ,'**********']

numList1 = []
for i in range(1,11):
    numList1.append('*'*i)
print('numList1 = ',numList1)

numList2 = [ '*'*i for i in range(1,11) ]
print('numList2 = ',numList2)

# for문이 2번 있는 리스트 for
# 리스트변수 = [ 결과값 for 명령문1 for 명령문2 ]
# 구구단의 결과값으로 리스트를 생성하여라

numList1 = []
for i in range(2, 10):
    for j in range(1, 10):
        numList1.append(i * j)
print('numList1 = ', numList1)

numList2 = [ i * j for i in range(2, 10) for j in range(1, 10) ]
print('numList2 = ', numList2)


# for문+ if 문 리스트 for
# 리스트변수 = [ 결과값 for 명령문1 if 조건식  ]
# 1~30까지 숫자중에서 5의 배수를 제외하고 리스트로 생성하여라

numList1 = []
for i in range(1, 31):
    if i%5 != 0:
        numList1.append(i)
print('numList1 = ', numList1)

numList2 = [ i for i in range(1, 31) if i%5 != 0]
print('numList1 = ', numList1)

# 자료형의 각 요소 값을 순차적으로 출력
# for 인덱스변수 in 리스트,문자열,튜플:
#   명령문

cityList = ['서울', '부산', '대구', '대전', '제주']

cnt = 0
while cnt < len(cityList):
    print(cityList[cnt])
    cnt += 1

print('-'*20)

for item in cityList:
    print(item)
print('-'*20)

# for 를 이용한 딕셔너리 요소 출력
# for 키변수 in 딕셔너리:
#   명령문
myDict = {1:'일', 100:'백', 50:'오십', 1000:'천'}

for key in myDict:
    print(key,' = > ', myDict[key])