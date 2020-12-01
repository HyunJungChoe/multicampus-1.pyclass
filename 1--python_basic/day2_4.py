
# 캐스팅
# 문자열 => 리스트
# 문자열변수.split() : 공백을 기준으로 해서 리스트화
# 문자열변수.split(구분문자) : 구분문자를 기준으로 해서 리스트화
# list(문자열변수)
# : 공백도 모두 리스트화. 낱글자가 아이템요소로 변경

msg1 = "오늘도 좋은 하루"
msg2 = "가나/콩고/아일랜드"
result1 = msg1.split()
result2 = msg2.split('/')
result3 = list(msg1)

print(result1, type(result1))
print(result2, type(result2))
print(result3, type(result3))

# 리스트 => 문자열
# str(리스트이름)
# : [ ], 쉼표(,) 도 포함해서 모두 문자열화
# '구분자'.join(리스트이름)
# : 구분자가 아이템요소 사이에 모두 추가된 후 문자열화
myList = ['기차','차고','고양이']
result1 = str(myList)
result2 = '  '.join(myList)
print(result1, type(result1), len(result1))
print(result2, type(result2), len(result2))

# 중첩 리스트 생성1
# 초기값으로 중첩 리스트 생성
# 리스트변수 = [ [값1, 값2...],[값1, 값2...]]
list1 = [1, 2, ['a', 'b','c'], ['포도', '수박']]
print('-'*30)
print(f'list1 = {list1}, 전체 길이는? {len(list1)}')
print(f'list1[0] = {list1[0]}')
print(f'list1에 3번째 리스트 요소에서 첫번째 아이템값은? {list1[2][0]}')
print(f'list1에 4번째 리스트 요소에서 마지막 아이템값은? {list1[3][-1]}')

# 중첩 리스트 생성2
# 1차원 리스트 정의 후 1차원 리스트를 다시 리스트로 구성
userName = ['홍길동', '고길동', '최길동']
userAge = [20, 25, 27]
userGender = ['남', '남', '남']
# 2 차원 리스트로 정의
userInfo = [userName, userAge, userGender]
print('-'*20)
print(userInfo)

# 퀴즈 :
'''
아래의 리스트를 이용하여 grade 리스트를 생성하고 합계와 평균을 
과목별로 출력한다. 평균은 소숫점 2번째 자리까지 출력한다. 

kor = [100, 80, 85]
math = [55, 70, 35]
eng = [80, 80, 100]
python = [90, 70, 88]
------------
result 
kor : 합계 = ? , 평균 = ?
math : 합계 = ? , 평균 = ?
eng : 합계 = ? , 평균 = ?
python : 합계 = ? , 평균 = ?
'''

kor = [100, 80, 85]
math = [55, 70, 35]
eng = [80, 80, 100]
python = [90, 70, 88]
# 2차원 리스트 생성
grade = [ kor, math, eng, python]
print(grade)

# 합계
korTot = grade[0][0] + grade[0][1] + grade[0][2]
mathTot = grade[1][0] + grade[1][1] + grade[1][2]
engTot = grade[2][0] + grade[2][1] + grade[2][2]
pythonTot = grade[3][0] + grade[3][1] + grade[3][2]

korAvg = korTot/3
mathAvg = mathTot/3
engAvg = engTot/3
pythonAvg = pythonTot/3

print(f'kor : 합계 = {korTot} , 평균 = {korAvg:.2f}')
print('math : 합계 = %d , 평균 = %.2f' % (mathTot, mathAvg))
print('eng : 합계 = %d , 평균 = %.2f' % (engTot, engAvg))
print('python : 합계 = %d , 평균 = %.2f' % (pythonTot, pythonAvg))
