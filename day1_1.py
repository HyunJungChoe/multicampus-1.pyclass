
# 출력문
print("hello", end=' ')
print("hello", end='/')
print("파이썬")

# 변수
x = 100
y = 200
print("x :", x, "y :", y)

# 변수 중복 해서 가능
x = 300
y = 400
print("x :", x, "y :", y)

# 문자열
print("Hello " + "Python")
print('-'*30)

# \n
line = \
'''
살려주세요
배고파요
'''
print(line)

# 변수
x, y = "가나다", "라마바"
print(x, y)

# 정의된 변수 삭제
# print(x)
# del x
# print(x)

#
x = True
y = "오늘도 열심히"
z = 123
print(x, type(x))
print(y, type(y))
print(z, type(z))

#
# print('-'*30)
# username = input('고객님 성함을 입력해 주세요..')
# print(username, '님 환영합니다.')

#
# num1 = int(input("첫 번째 숫자를 입력하세요"))
# num2 = int(input("두 번째 숫자를 입력하세요"))
# print(num1, "+", num2, "=", num1+num2)
# print(num1, "-", num2, "=", num1-num2)
# print(num1, "*", num2, "=", num1*num2)
# print(num1, "/", num2, "=", num1/num2)

#
print(100/3, 100//3, 100%3)

# 인덱싱과 슬라이싱
msg = "가나다라마바사"
print(msg[0])
print(msg[6])  # 마지막
print(msg[-1])  # 마지막

print(msg[:4])
print(msg[2:5])
print(msg[0::2])  # 2칸씩 띄기
print(msg[1::2])

# f'' 포맷팅 ***
stName = "홍길동"
stAge = 99
score = 77.77
print(f'학생명 : {stName} , 나이 : {stAge} , 점수 : {score}')
