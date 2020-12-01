# 오류의 종류 (에러코드 - 에러메세지 e)
# SyntaxError - 예시) print('dddd)
# NameError
# IndexError
# ZeroDivisionError : 0으로 나눈 경우
# FileNotFoundError : 잘못된 파일 경로
# ValueError
# TypeError

# 예외처리란?
# 에러가 나면 그아래의 명령은 실행되지 않는다.

# 에러처리 문법 1
# ## try..except 에러코드 as e: 에러처리명령
# - 에러코드를 알고있어야 한다.
# try:
#   명령어
# except 에러코드 as e:
#   에러처리명령

# 잘못된 인덱스 접근
# IndexError: list index out of range
myList = [1, 100, 80, 90]
try:
    print(myList[0])
    print(myList[10])
    # print(myList[1])
    # print(myList[2])
    # print(myList[-1])
except IndexError as e: # e는 에러메세지 출력시 사용
    print(f'에러메세지 - {e}')
    print(myList[1])
    print(myList[2])
    print(myList[-1])
print('-'*50)

# ## try..except 명령2
# 모든 예외의 에러 메시지를 출력할 때는 Exception 키워드
# 에러코드를 몰라도 된다. => Exception
# try:
#     명령
# except Exception as e:
#     print(e)

num1 = 10
# num2 = 0
num2 = 5
try:
    result = num1/num2
    print(result)
    print(result2)
# except ZeroDivisionError as e:
except Exception as e:
    print(f'에러메세지 - {e}')

print('-'*50)

# try..except 명령3
# 에러메세지 e를 출력하지 않는 경우
# try:
#   명령어
# except:
#   에러처리명령`

# 파일입출력과 관련된 에러 발생 후 명령어 처리
try:
    # 에러발생
    with open('도레미.txt', 'r', encoding='utf-8') as f:
    # 파일이 있는 경우
    # with open('data/color.txt', 'r', encoding='utf-8') as f:
        print(f.readline())
# except Exception as e:
#         print(e)
except:
    # print('그런 파일 없습니다.')
    # 에러무시
    pass
print('-'*50)


'''
try:
    명령어1
    명령어2
except:    
except 오류코드 as e:    
except Eception as e:    
    에러처리명령어 
    pass
'''


# 퀴즈 1: FileNotFoundError
#  data/test.txt 가 없다면
#  에러메세지(e)와 함께 '파일이 없습니다.' 메세지 출력
#  있다면 파일의 내용을 출력한다.



# 퀴즈 2: ValueError
# 2개의 숫자글자를 입력받아서 더한다.
# 입력된 글자가 숫자글자가 아니라면 에러 메세지 출력
# 입력된 글자가 숫자글자라면  더한후 출력한다.

# try:
#   n1 = input('숫자1입력 ? .... ')
#   n2 = input('숫자2입력 ? .... ')
#   print(f'{n1} + {n2} = {int(n1)+int(n2)}')
# # except ValueError as e:
# except Exception as e:
#   print('입력 데이터가 숫자가 아닙니다.\n\t\t %s' %e)


# try: ... except: ... else:...

# 에러명을 아는 경우
# try:
#   명령어
# except 에러코드 as e:
#   e 출력 ,에러처리명령
# else:
#   에러가 발생하기 않은 경우 명령어

# 에러코드는 모르지만 에러 메세지 출력하고 싶을때
# try:
#   명령어
# except Exception as e:
#   e 출력 ,에러처리명령
# else:
#   에러가 발생하기 않은 경우 명령어


# 에러코드도 모르고 에러메세지도 출력하고 싶지않을때
# try:
#   명령어
# except:
#   에러처리명령
# else:
#   에러가 발생하기 않은 경우 명령어

# print('-'*50)
# try:
#   n1 = int(input('숫자1입력 ? .... '))
#   n2 = int(input('숫자2입력 ? .... '))
# # except ValueError as e:
# # except Exception as e:
# #   print('입력 데이터가 숫자가 아닙니다.\n\t\t %s' %e)
# except:
#     print('오류발생 - 명령처리 불가능')
# else:
#     print(f'{n1} + {n2} = {n1+n2}')
#
# print('-'*90)


# try: ... except:... else:... finally:...
# else... , finalley... 는 생략 가능
# try:
#   명령어
# except 에러코드 as e:
# except Eception as e:
# except:
#   에러처리명령
# else:
#   에러가 발생하기 않은 경우 명령어
# finally:
#   무조건 실행되는 명령어


try:
    # 파일이 없다
    # f = open('data/test.txt', 'r', encoding='cp949')
    # 파일이 있다.
    f = open('data/Yesterday.txt', 'r', encoding='cp949')
except Exception as e:
    print(f'파일이 없습니다. \n\t\t {e}')
else:
    print(f.readline())
    f.close()
finally:
    print('파일 읽기 테스트 종료')

'''
파일이 없습니다. 
       [Errno 2] No such file or directory: 'data/test.txt'
파일 읽기 테스트 종료
'''

'''
Yesterday 

파일 읽기 테스트 종료
'''


# 여러개의 오류 처리하기
# 먼저 발생한 오류 우선: 뒤에 오류는 실행되지 않음
# 에러코드를 알고 있는 경우에 사용

# try:
#     명령실행 1
#     명령실행 2
#       ...
# except 발생오류1:
#     에러메세지 출력1
# except 발생오류2:
#     에러메세지 출력2
# finally:
#     테스트완료명령


try:
    # myNumber = 77
    print(myNumber)
    print(800/0)
except ZeroDivisionError as e:
    print(f'0으로 나누는 경우의 에러 : 에러메세지 - {e}')
except NameError as e:
    print(f'정의되지 않은 변수 에러 : 에러메세지 - {e}')
finally:
    print('테스트종료')

# 정의되지 않은 변수 에러 : 에러메세지 - name 'myNumber' is not defined
# 테스트종료

try:
    myNumber = 77
    print(myNumber)
    print(800/0)
except ZeroDivisionError as e:
    print(f'0으로 나누는 경우의 에러 : 에러메세지 - {e}')
except NameError as e:
    print(f'정의되지 않은 변수 에러 : 에러메세지 - {e}')
finally:
    print('테스트종료')

# 0으로 나누는 경우의 에러 : 에러메세지 - division by zero
# 테스트종료

# -------------------------------
# 사용자정의 에러
# 에러만들기1 : raise 문 이용
# 일부러 에러 발생
# if 조건식:
#   raise Exception(오류 메세지)

# x 값에 따라 에러 발생
# 변수값이 음수이면 에러발생
print('-'*50)
# x = 10
# x = 0
# x = -10
# if x < 0:
#     raise Exception('x는 양수이거나 0이어야한다.')
# elif x==0:
#     print('x는 0')
# else:
#     print('x는 양수')

print('*'*50)
# try + raise 구문
# x = 10
x = -10
try:
    if x < 0:
        raise Exception('x는 양수이거나 0이어야한다.')
    elif x==0:
        print('x는 0')
    else:
        print('x는 양수')
except Exception as e:
    # print('에러 테스트.. x는 양수이거나 0이어야한다.')
    print(f'에러 테스트.. {e}')

# 에러 테스트.. x는 양수이거나 0이어야한다.

# 금칙어 에러
# exceptWord = ['바보', '멍청이', '예쁜이']

# nickName = input('닉네임을 입력해주세요...').strip()
# if nickName in exceptWord:
#     raise Exception('금칙어입니다. 닉네임으로 사용하실 수 없습니다')
# else:
#     print(f'당신의 닉네임은 {nickName}')
#     print(f'환영합니다 {nickName} 님')

# 예외처리 구문안에 사용자정의 에러 사용하기


# exceptWord = ['바보', '멍청이', '예쁜이']
# try:
#     nickName = input('닉네임을 입력해주세요...').strip()
#     if nickName in exceptWord:
#         raise Exception('금칙어입니다. 닉네임으로 사용하실 수 없습니다')
# except Exception as e:
#     print(f' 에러메세지 - {e}')
# else:
#     print(f'당신의 닉네임은 {nickName}')
#     print(f'환영합니다 {nickName} 님')
# finally:
#     print('--- 닉네임 테스트 종료--- ')

'''
닉네임을 입력해주세요...똘똘이
당신의 닉네임은 똘똘이
환영합니다 똘똘이 님
--- 닉네임 테스트 종료--- 
'''

'''
닉네임을 입력해주세요...예쁜이
 에러메세지 - 금칙어입니다. 닉네임으로 사용하실 수 없습니다
--- 닉네임 테스트 종료--- 
'''


# 퀴즈 3 : ValueError, ZeroDivisionError
# 2개의 데이타값을 입력받은 후 나누기 명령을 실행한다.
# try ... except .. except..
# 에러가 발생하면
#   에러 메세지 출력 : '데이타 오류 ...'
# 에러가 발생하지 않으면
#   결과 수행 : n1 / n2 = ?

print('-'*70)
def plusNum():
    try:
        num1 = int(input('첫번째 값을 입력하세요...'))
        num2 = int(input('두번째 값을 입력하세요...'))
        result = num1/num2

    except ZeroDivisionError as e:
        print(f'ZeroDivisionError 데이타 오류 ... - {e}')
    except ValueError as e:
        print(f'ValueError 데이타 오류 ... - {e}')
    else:
        print(f'{num1} / {num2} = {result}')

# plusNum()

# 퀴즈 4
# data_eng.txt 파일을 파일 변수로 저장한다.
# data/data_eng.txt 파일이 없다면 (에러발생)
# data_eng.txt 파일이 없다면 (에러발생)
#   메세지 출력. => '파일없음'
# 파일이 있다면 (에러가발생하지 않는다면)
#   총합과 평균을 구하여 출력한다.


print('-'*70)
def total_avg(url, op):
    try:
        sum=0
        with open(url,'r',encoding=op) as f:
            data_list = f.readlines()
            for item in data_list:
                sum+=int(item)
            print(f'sum={sum}')
            print(f'avg={sum/len(data_list)}')
    except:
        print('파일 없음')
total_avg('data_eng.txt', 'cp949')
print('-'*70)
total_avg('data/data_eng.txt', 'cp949')



# 퀴즈 5
# 매개변수값에 따라 다음과 같은 메세지를 출력한다.
# 0과 같거나 0보다 작다
# 0보다 크다
# 매개변수값이 숫자가 아닌경우에는 오류를 무시하도록(pass)
# try...except 문을 작성하여라

def numCompare(x):
    try:
        # x=int(input('값을 입력하세요... '))
        if x<=0:
            print(f'매개변수는 0과 같거나 0보다 작다.')
        else:
            print(f'0보다 크다.')
    except Exception:
        pass
numCompare(0)
numCompare(90)
numCompare('가나다')



# 퀴즈6
# 학생의 학년을 저장하는 변수 classYear값은
# 1학년, 2학년, 3학년, 4학년 이어야한다.
# 나머지 값은  raise Exception 을
# 이용하여 오류를 발생시켜라
#  예시) classYear = '8학년'
# 오류 메세지
#       학년 정보가 올바르지 않습니다.
#       올바른 값은 1학년~4학년 입니다.


def classYear():
    classYear=['1학년','2학년','3학년','4학년']
    ans = input('학년을 입력하시요...')
    if ans not in (classYear):
        raise Exception('학년 정보가 올바르지 않습니다.\n올바른 값은 1학년~4학년 입니다.')

# classYear()

def classYear2():
    classYear=int(input('학년을 입력하시요...'))
    if 1<=classYear<=4:
        # print(f'{classYear}학년 입니다.')
        pass
    else:
        raise Exception('학년 정보가 올바르지 않습니다.\n올바른 값은 1학년~4학년 입니다.')

classYear2()

