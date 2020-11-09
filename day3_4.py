
# 입력값이 짝수인지 홀수인지 판단 ?
# 숫자%2 == 0

# myNum = int(input('숫자값을 입력해주세요'))
# if (myNum%2 == 0):
#     print(f'{myNum} 은 짝수')
# if (myNum%2 != 0):
#     print(f'{myNum} 은 홀수')
#
# myNum = int(input('숫자값을 입력해주세요 ... '))
# if (myNum%3 == 0):
#     print(f'{myNum} 은 3의 배수이다')
# if (myNum%3 != 0):
#     print(f'{myNum} 은 3의 배수가 아니다.')

'''
if 조건식:
    명령문1
else:
    명령문2
'''
myNum = 100
if (myNum % 2 == 0):
    print(f'{myNum} 은 짝수')
else:
    print(f'{myNum} 은 홀수')

a = 10
b = 1
if a>b:
    print('a 는 b보다 크다')
elif a<b:
    print('a 는 b보다 작다')
else:
    print('a 와 b는 같다')

# 숫자인지 숫자가 아닌지 판독
data = '가나다라'
if data.isdigit():
    if int(data)>0:
        print('양수')
    else:
        print('0 제로')
else:
    print('숫자가 아니다.')

# 문자가 문자열에 있는가/없는가?
print('a' in 'banana')  # True
print('x' in 'banana')  # False
print('a' not in 'banana')  # False
print('x' not in 'banana')  # True


# 값이 리스트에 있는가?
myList = [100, 200, 300]
print(100 in myList) # True
print(100 not in myList) # False
print(1 in myList) # False
print(1 not in myList) # True

fruits = ('수박', '체리', '자두')
if '귤' in fruits:
    print('체리가 냉장고에 있다')
elif '아보카도' in fruits:
    print('체리가 냉장고에 있다')
else:
    print('냉장고에 아무것도 없다')