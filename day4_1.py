
# for .. in range(start, end, step) { 명령문 }
# for item in 문자열/튜플/리스트 { 명령문 }
# for key in 딕셔너리 { 명령문 }
# 리스트변수 = [ 결과값 for 문 ]

# 1~10까지 출력한다.
for i in range(1, 11):
    print(i, end = ' ')
print('\n','-'*20)

# 10~1 까지 출력한다.
for i in range(10, 0, -1):
    print(i, end = ' ')

# for .. in range(start, end, step) { 명령문 }
# for item in 문자열/튜플/리스트 { 명령문 }
# for key in 딕셔너리 { 명령문 }
# 리스트변수 = [ 결과값 for 문 ]

# 1~10까지 출력한다.
for i in range(1, 11):
    print(i, end = ' ')
print('\n','-'*20)

# 10~1 까지 출력한다.
for i in range(10, 0, -1):
    print(i, end = ' ')
print('\n','-'*20)

# 중복 for 문
for i in range(5):
    print(i)
    for j in range(3):
        print(j, end = ' ')
    print()

print('\n','-'*20)

# for item in 문자열/튜플/리스트 { 명령문 }
myList = [100, 200, 300, 400, 500]
for item in myList:
    print(item)
print('\n','-'*20)


# for key in 딕셔너리 { 명령문 }
myDict = { '가':'가지', '나':'나라', '다':'다리'}
for key in myDict:
    print(key, ' => ', myDict[key])

# ---- 리스트 컴프리핸션
# [표현식 for 항목 in 순회가능 객체 if 조건 ]
# 리스트 변수 = [결과값 for 문 ]
# 1~100 3의 배수
result = [i for i in range(1, 10)]
print(result)
# 1~100 3의 배수
result = [i for i in range(3, 101, 3)]
print(result)
# 1~100 3의 배수 제외
result = [i for i in range(1, 101) if i % 3 != 0]
print(result)

# 다중 리스트와 for
# 2차원 리스트의 갯수가 같아야 한다.
# for (i, j...) in 다중리스트:
#   명령문
print('-'*20)
listMulti1 = [[1, 2, 3],
              ['a', 'b'],
              ['홍길동', '춘향이', '흥부', '놀부']]
print(listMulti1)
print(listMulti1[0])
print(listMulti1[1][0])
print(listMulti1[2][3])

listMulti2 = [[1, 2, 3],
              ['a', 'b', 'c'],
              ['홍길동', '춘향이', '흥부']]
print('-'*20)

listMulti2 = [[1, 2, 3],
              ['a', 'b', 'c'],
              ['홍길동', '춘향이', '흥부']]
print('-'*20)
for (i, j, k) in listMulti2:
    print(f'i = {i}, j = {j}, k = {k}')

listMulti3 = [[2,100],
              ['b', 'c'],
              ['춘향이', '홍련이']]
for (i, j) in listMulti3:
    print(i, j)
    print('+++++++++')

# 퀴즈 : 학생이름, 국어, 영어, 수학 으로 구성된
# 2차원 리스트를 생성한다.
# 출력형식은 아래와 같이 한다.
'''
학생이름  국어  영어  수학  합계  평균   
김태희     30   40   100   ?     ?
...

'''
stGradeList = [['김태희', 30, 50, 55],
               ['신민아', 50, 90, 80],
               ['박지민', 50, 90, 40],
               ['김소희', 60, 50, 56],
               ['윤준희', 90, 88, 66]]

print(f"학생이름  국어  영어  수학  합계  평균 ")
for (i, j, k, l) in stGradeList:
    s = j + k + l
    a = int(s/3)
    print(f" {i}   {j}    {k}   {l}  {s}   {a}")