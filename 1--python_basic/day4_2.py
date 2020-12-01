

# 함수 정의 1
# 인자도 없고 return문도 없음

# 함수 호출시 특정 메세지 3번 출력
# 함수 정의

def hello_world():
    for i in range(3):
        print('Hello World')
    print('-'*30)


# 함수 정의 2
# 인자가 있다. return이 없다.
'''
def 함수명(인자1,인자2..):
    인자가 있는 명령문
'''
# 호출
# 함수명(값1, 값2...)

# 특정 메세지를 3번 반복
def hello(message):
    for i in range(3):
        print(f'Hello {message}')
    print('-'*30, '\n'*2)


# 특정 메세지를 n번 반복
def hello_n(n, message):
    for i in range(n):
        print(f'{i+1} : Hello {message}')
    print('-'*30, '\n'*2)

# 출력문이 있는 경우의 함수
def resultString2():
    print('Hello Numpy1')
    return 'Hello Numpy2'
# print('+'*30)
# print(f' 함수 호출 : {resultString2()}')
#

# 함수 정의 4
# 인자가 있다. return 이 있다
'''
def 함수명(인자1, 인자2...):
    인자에 관련된 명령문...
    return 결과값/수식/명령문
'''
# 호출
# 함수명(값1, 값2...)
# 이름을 인자로 설정, 인사말+이름 리턴
def wecome(userName):
    print(f'함수호출 => {wecome("고길동")}')
    print(f'함수호출 => {wecome("최길동")}')
    return '환영합니다. '+userName+' 님'




'''
퀴즈 1: n까지의 누적합을 반환하는 함수 정의 후 호출 
print(f'1~500까지의 합은? {sumN(500)}')
print(f'1~2000까지의 합은? {sumN(2000)}')

퀴즈 2: x~y까지의 누적합을 반환하는 함수 정의 후 호출 
       2개의 수 x, y를 인자로 전달하여 누적합 구하기        
print(f'100~500까지의 합은? {sumXY(100,500)}')
print(f'500~1000까지의 합은? {sumXY(500, 1000)}')
'''
def sumN(n):
    tot = 0
    while(n):
        tot += n
        n -= 1
    return tot
# print(sumN(500))
# print(sumN(2000))


# 함수 정의 5
# 인자가 있다. return 값이 다중인 경우
# 다중 return 값인 경우 자료형은 튜플
# (결과값1, 결과값2...)
# 각각의 결과값은 인덱싱 으로 접근할 수 있다.
'''
def 함수명(인자1, 인자2...):
    인자에 관련된 명령문...
    return 결과값1, 결과값2 ....
'''
# 호출
# 함수명(값1, 값2...)

# 인자 X,  리턴값 2개
def multiReturn1():
    x = 100
    y = 4
    return x+y, x*y

# 인자 X,  리턴값 2개
def multiReturn1():
    x = 100
    y = 7
    return x+y, x*y, x-y, x//y, x%y

print(multiReturn1(), type(multiReturn1()))
# (107, 700, 93, 14, 2) <class 'tuple'>
result = multiReturn1()
# print(f'100과 7의 연산 => 더한값은? {result[0]}')
# print(f'100과 7의 연산 => 차이값은? {result[2]}')


# 인자 O,  리턴값 2개이상
# n개의 입력값 이용 => 튜플 또는 리스트로 반환
def multiReturn2(n):
    result = []
    for i in range(n):
        item = input('값 입력 => ')
        result.append(int(item))
    resultTuple = tuple(result)
    return result, resultTuple

# print('-'*20)
# result = multiReturn2(3)
# print(result, type(result))
# print( result[0], type(result[0]))
# print( result[1], type(result[1]))
# for i in result[0]:
#     print(i)
# print('-'*50)
# for i in result[1]:
#     print(i)

# 함수 정의 6
# 인자의 초기값 설정 (모든 인자의 초기값이 있는 경우)
'''
def 함수명(인자1=값1, 인자2=값2):
    인자에 관련된 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명()
# 함수명(값1)
# 함수명(값1, 값2)

# 숫자의 합을 출력하는 함수 정의
# 인자 O, return X
def sumTwo(x=0, y=0):
    print(f'{x} + {y} = {x+y}')

sumTwo()
sumTwo(100)
sumTwo(23, 67)

# 숫자의 곱을 출력하는 함수 정의
# 인자 O, return O
def multiTwo(x=1, y=1):
    # return x*y
    return f'{x} * {y} = {x*y}'

print(multiTwo())
print(multiTwo(8))
print(multiTwo(10, 67))


# 함수 정의 7
# 인자의 초기값 설정 (특정 인자만 초기값이 있는 경우)
# 주의 사항은 마지막 인자에는 초기값이 있어야 한다.
'''
def 함수명(인자1, 인자2=값2):
    인자에 관련된 명령문...
    return 값/변수/수식/명령문
'''

# 숫자의 모든 합
def sumNumber1(x, y=0, z=0):
    return f'{x} + {y} + {z} = {x+y+z}'

# print(sumNumber1()) # TypeError
print(sumNumber1(10))
print(sumNumber1(10, 30))
print(sumNumber1(20, 50, 100))


# if __name__ == '__main__':
    # 함수 호출
    # hello_world()
    # # hello('Python')
    # hello_n(1, 'Flask')
    # hello_n(5, 'PANDAS')
    # resultString2()
    # print(wecome('aaa'))
    # print(sumN(500))
    # print(sumN(2000))
    # print(multiReturn1(), type(multiReturn1()))
