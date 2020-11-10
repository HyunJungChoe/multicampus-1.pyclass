
# 가변인자인 경우 : 인자의 갯수가 정해지지 않는 경우
# *args => arguments
# 인자가 args 리스트로 반환
'''
def 함수명(*args):
    args에 관련된 명령문...
    return 값/변수/수식/명령문
'''

# 호출
# 함수명(값1)
# 함수명(값1, 값2)
# 함수명(값1, 값2, 값3 ...)

# 메세지 출력
def messagePrint(*args):
    return args;

print(messagePrint('안녕하세요'), type(messagePrint('안녕하세요')))
print(messagePrint('안녕하세요','반가워요'), type(messagePrint('안녕하세요','반가워요')))
print(messagePrint('고맙습니다.','안녕하세요','반가워요'),
                    type(messagePrint('고맙습니다.','안녕하세요','반가워요')))

# 퀴즈1 . 위의 예제를 다음 형태로 변경하여라
'''
studentName2()
# 학생이 없습니다.
studentName2('홍길동')
# 1번째 학생 : 홍길동
studentName2('홍길동', '이순신', '이몽룡')
# 1번째 학생 : 홍길동
# 2번째 학생 : 이순신
# 3번째 학생 : 이몽룡
'''

def studentName2(*args):
    print('\n'*3)
    if len(args) == 0:
        print('학생이 없습니다.')
    else:
        cnt = 1
        for item in args:
            print(f'{cnt} 번째 학생 => {item}')
            cnt += 1


studentName2()
studentName2('고미란')
studentName2('마동탁','고길동','임요환')

def sumNumber(*args):
    print('-'*3)
    if len(args) == 0:
        print('인자값이 없다')
    else:
        sum = 0
        tempList = []
        for item in args:
            sum+=item
            tempList.append(str(item))
        print(' + '.join(tempList), '=', sum)

sumNumber() # 인자값이 없다
sumNumber(1,2) # 1 + 2 = 3
sumNumber(4,5,6) # 4 + 5 + 6 = 15
sumNumber(4,5,6,10,50) # 4 + 5 + 6 + 10 + 50 = 75

# 문자 인자 숫자는 가변인자
def  printParameter(txt, *args):
    print('-'*20)
    print('txt', '=', txt)
    print('args', '=', args)
    for item in args:
        print('\t',item)

printParameter('영희', 10, 20)
printParameter('철수', 78, 99, 10, 20)

def calChoice(choice, *args) :
    if choice == '*':
        result = 1
        for item in args:
            result *= item
        return print(f'계산결과 = 곱 : {result}')
    elif choice == '+':
          result = 0
          for item in args:
              result += item
          return print(f'계산결과 = 합 : {result}')
    else:
          return print("계산 오류 ")

calChoice('*', 20,30) # 계산결과 = 곱 : 600
calChoice('+', 20,30,50) # 계산결과 = 합 : 100
calChoice('-', 20,30,50) # 계산 오류

# 함수 정의 10
# 딕셔너리 가변인자 **kwargs
# 가변인자는 키=값
# 결과 데이터형이 딕셔너리
# kwargs = Keyword Arguments

'''
def 함수명(**kwargs):
    kwargs를 명령문...
    return 값/변수/수식/명령문
'''
# 호출시 키는 인용부호를 붙이지 않는다.
# 함수명(키1=값1)
# 함수명(키1=값1, 키2=값3 ...)

# 딕셔너리 스타일로 인자 전달 후 출력
def printDict(**kwargs):
    print(kwargs)
    print(type(kwargs))

printDict()
printDict(key1='사과')
printDict(key1='사과',key2='바나나',key3='포도')
# {}
# <class 'dict'>
# {'key1': '사과'}
# <class 'dict'>
# {'key1': '사과', 'key2': '바나나', 'key3': '포도'}
# <class 'dict'>

# 딕셔너리 스타일로 가변인자 전달 후 세로로 출력
def printDict2(**kwargs):
    print('함수 호출')
    for key in kwargs:
        print(f'{key} => {kwargs[key]}')

printDict2(a='apple', b='banan', c='cat')
printDict2(y='yes', s='sale', a='apple', b='banan', c='cat')

# 사원정보에 관련된 함수 정의
# nationality 키값의 초기값은 Korea
def personInfo(**kwargs):
    # 초기값 지정
    kwargs['nationality'] = 'Korea'
    print('-'*30)
    for key in kwargs:
        print(f'{key} => {kwargs[key]}')

personInfo(name='Maria', age=23, gender='female', nationality='USA')
personInfo(name='홍길동', age=28, gender='male')

# 람다 함수 = 익명함수 = 한줄함수
# def 로 정의하지 않다.
# 한줄로 정의한다.
'''
# 람다함수 정의
함수변수 = lambda 인자:명령

# 람다함수 호출
함수변수(인자)
'''

# 두수의 합을 출력하는 람다 함수 정의
def sum(x,y):
    print(f'{x} + {y} = {x+y}')

sum(10, 30)

f1 = lambda x,y:print(f'{x} + {y} = {x+y}')
f1(34, 100)

# 문자열에 인사말추가 출력
f2 = lambda userName:userName+'님 오늘도 좋은 하루'
print(f2('성춘향'))




