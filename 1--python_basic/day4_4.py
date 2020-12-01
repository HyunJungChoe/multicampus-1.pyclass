# ---------- for 반복문  ----------

# 1. 1~100 사이의 숫자 중 11의 배수이거나 7의 배수로 구성된 리스트를
# 리스트 내포 방식을 이용하여 출력하고 총 갯수도 함께 출력하세요.
'''
[7, 11, 14, 21, 22, 28, 33, 35, 42, 44, 49, 55, 56, 63, 66, 70, 77, 84, 88, 91, 98, 99]
 총 22 개
'''
result = [i for i in range(1, 101) if (i % 7 == 0 or i % 11 == 0)]
print(result)
print(f"총 {len(result)}개")


# 2. 이중 리스트 내포 방식을 이용하여 다음과 같은 리스트를 생성하고 출력하여 보세요
# ['1 - 1', '1 - 2', '1 - 3',
# '2 - 1', '2 - 2', '2 - 3',
#    '3 - 1', '3 - 2', '3 - 3',
#    '4 - 1', '4 - 2', '4 - 3',
#    '5 - 1', '5 - 2', '5 - 3']
result = [f'{i}-{j}' for i in range(1,6) for j in range(1, 4)]
print(result)


# 3. 다음 2차원 리스트를 생성하고 결과와 같이 for...in 문을 이용하여 출력하여 보세요
# employees = [
#                 ['김수철', '서울', 25, '남', '총무부'],
#                 ['고길동', '부산', 33, '남', '회계부'],
#                 ['최미나', '대전', 22, '여', '기획부'],
#                 ['은지원', '서울', 44, '남', '영업부'],
#                 ['김영탁', '울산', 36, '남', '영업부'],
#                 ['마동탁', '대구', 50, '남', '기획부'],
#                 ['이은미', '창원', 42, '여', '총무부']
#               ]
#
#    ----------------------------------------
#      사원명     출신지     나이     성별     부서
#    ----------------------------------------
#      김수철     서울     25     남     총무부
#      고길동     부산     33     남     회계부
#      최미나     대전     22     여     기획부
#      은지원     서울     44     남     영업부
#      김영탁     울산     36     남     영업부
#      마동탁     대구     50     남     기획부
#      이은미     창원     42     여     총무부
employees = [
                ['김수철', '서울', 25, '남', '총무부'],
                ['고길동', '부산', 33, '남', '회계부'],
                ['최미나', '대전', 22, '여', '기획부'],
                ['은지원', '서울', 44, '남', '영업부'],
                ['김영탁', '울산', 36, '남', '영업부'],
                ['마동탁', '대구', 50, '남', '기획부'],
                ['이은미', '창원', 42, '여', '총무부']
              ]
print('-'*40)
print('사원명\t 출신지\t 나이\t  성별\t 부서\t')
print('-'*40)
for (i, j, k, l, m) in employees:
    print(f'{i}\t {j}\t {k}\t\t{l}\t\t{m}\t')



# 4. 16번의 리스트에서 남자 사원 목록만 출력하여 보세요.
print('-'*40)
for (i, j, k, l, m) in employees:
    if(l == '남'):
        print(f'{i}\t {j}\t {k}\t\t{l}\t\t{m}\t')



# 5. 16번의 리스트에서 성이 '김'인 사원 목록만 출력하여 보세요.
print('-'*40)
for (i, j, k, l, m) in employees:
    if(i[0] == '김'):
        print(f'{i}\t {j}\t {k}\t\t{l}\t\t{m}\t')


# ------------------- 함수 퀴즈

# 퀴즈1 : 별찍기
# 숫자만큼 다음과 같은 형태로 출력하는
# 함수를 정의한 후 호출하여라.

def starPrint(n):
    for i in range(n+1):
        print('*'*i)
starPrint(5)
starPrint(3)

# 퀴즈 2
# 인자값을 받아서 출력하는 구구단 함수를 정의한 후
# 호출하여 출력하여라

def gugu(n):
    print('*' * 30)
    for i in range(1, 10):
        print('{} X {} = {}'.format(n, i, n * i))

gugu(9)
gugu(5)


# 퀴즈 3:
# 리스트를 호출하면 각각의
# 아이템이 다음과 같이 출력되도록 함수를 정의하여라

def printList(foodList):
    print('\n\n   오늘의 메뉴   ')
    for i in range(0,len(foodList)):
        print(i+1, ' : ', foodList[i])

printList(['모밀', '탕수육', '육계장'])
printList(['라면', '빙수'])


# 퀴즈 4
# 키와 몸무게를 인자로 입력하여
# 메세지가 출력되도록 함수를 정의하고
# bmi 값에 따라 출력한다.
#
# k = 키(입력값) 단위 cm
# w = 체중(입력값)
#
# bmi = (체중(kg)/키(m)의제곱)*1000
#
# bmi 값에 따라 다음과 출력한다.
#
# 고도 비만 : 35 보다 클 경우
# 중등도 비만  : 30 - 35 미만
# 경도 비만 : 25 - 30 미만
# 과체중 : 23 - 25 미만
# 정상 : 18.5 - 23 미만
# 저체중 : 18.5 미만

def bmi(k,w):
    # k = k/100
    # bmi = (몸무게/키의제곱)*1000
    bmi = (w/(k**2))*10000

    print('===================')
    print('키 : ', k)
    print('몸무게 : ', w)
    print('BMI : %4.2f' % bmi)

    if bmi >= 35 :
        print('고도 비만')
    if 30 <= bmi < 35 :
        print('중등도 비만')
    if 25 <= bmi < 30 :
        print('경도 비만')
    if 23 <= bmi < 25 :
        print('과체중')
    if 18.5 <= bmi < 23 :
        print('정상')
    if bmi < 18.5 :
        print('저체중')

bmi(170,68)


# 퀴즈 5
# 아래와 함수를 호출하여 메세지가 출력되도록
# 함수를 정의하여라
# 이때 함수 인자는 3개로 구성하며 마지막 man 만 True 형태로
# 초기값을 지정한다.

def say_myself(name, old, man=True):
    print('-' * 50)
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
    print ('-'*50)


say_myself('김철수', 20)
say_myself('백설공주', 15, False)



# 퀴즈 6
# 여러가지 값이 리스트에 저장될 수 있게
# 인자가 가변인 함수를 정의하고 호출하여라
def addList(*args):
    listResult = list(args)
    print(f'\n\n총 갯수 : {len(listResult)}')
    print(f'데이타형 : {type(listResult)}')
    for i in range(0, len(listResult)):
        print(f'{i} 번째 => {listResult[i]}')

addList(1,2,3,4)
addList('가','나','다','라','마')


# 퀴즈 7
# 첫번째 인자의 값이 'min'이면 다음 인자의 숫자 중
# 최대값을 출력하고
# 첫번째 인자의 값이 'max'이면 다음 인자의 숫자중
# 최소값을 출력하여라
# 이 때 전달하는 숫자의 갯수는 가변으로 한다.

def dictDefine(**kwargs):
    print('\n'*2)
    print(kwargs)
    for key in kwargs:
        print(key, ':', kwargs[key])

dictDefine(a='apple', b='banana', n='nano')
dictDefine(b='banana', n='nano', s='soup', d='dress', q='quit')




# 퀴즈 8
# **kwargs 인자 가변 함수를 이용하여
# 함수 호출시 결과값이 다음과 같이 딕셔너리 형태로
# 출력되도록 하여라
'''
# 함수 호출 
dictDefine(a='apple', b='banana', n='nano')
dictDefine(b='banana', n='nano', s='soup', d='dress', q='quit')

결과1 >>>

{'a': 'apple', 'b': 'banana', 'n': 'nano'}
a : apple
b : banana
n : nano

결과2 >>>
{'b': 'banana', 'n': 'nano', 's': 'soup', 'd': 'dress', 'q': 'quit'}
b : banana
n : nano
s : soup
d : dress
q : quit

'''
def dictDefine(**kwargs):
    print('\n'*2)
    print(kwargs)
    for key in kwargs:
        print(key, ':', kwargs[key])

dictDefine(a='apple', b='banana', n='nano')
dictDefine(b='banana', n='nano', s='soup', d='dress', q='quit')



# 퀴즈 9
# 첫글자를 제외한 나머지 글자를 '*'로 표시하는
# 람다함수를 정의하여라. 입력되는 문자열은 3글자로 한다.


'''
# 함수 호출 
# f1('홍길동')
# f1('김철수')

결과: >>
홍**
김**
'''
f1 = lambda txt:print(txt[0]+'**')
f1('홍길동')
f1('김철수')

# 퀴즈 10
# 국어,영어,수학 3과목의 합과 평균을 구하는
# 람다 함수를 정의하여라
'''
# 람다 호출 
# f2(100,80,90)

결과 >>
국어:100, 영어:80, 수학:90 , 총점:270, 평균90.00

'''
f2 = lambda x,y,z:print(f'국어:{x}, 영어:{y}, 수학:{z} , 총점:{x+y+z}, 평균{(x+y+z)/3:.2f}')
f2(100,80,90)