
# 함수내에서 지역변수를 전역변수로 정의
# global 변수명

# 전역변수 정의
x = 10
y = 100
z = 200

def scopeTest():
    # 지역변수
    x = 0
    y = 0
    # 전역변수 선언
    global z
    z = 500
    print(f' 함수안의 x = {x}')
    print(f' 함수안의 y = {y}')
    print(f' 함수안의 z = {z}')

print(f' 함수밖의 x = {x}') # 10
print(f' 함수밖의 x = {y}') # 100
print(f' 함수밖의 z = {z}')

scopeTest()
# 함수안의 x = 0
# 함수안의 y = 0
# 함수안의 z = 500

print(f' 함수밖의 x = {x}') # 10
print(f' 함수밖의 x = {y}') # 100
print(f' 함수밖의 z = {z}') # 500

# 시간과 관련된 모듈 임포트
import datetime, time

# 현재 시간을 기준으로 년월일시분초 변수 생성하기
now = datetime.datetime.now()
print(f' now = {now} , {type(now)}')

# 퀴즈1 : if문과 datetime 모듈 이용
# 현재 시간을 아래와 같이 오전과 오후로 분리해서 출력한다.
# 현재 시간은 오후 5시 ? 분입니다.

now = datetime.datetime.now()
if now.hour < 12:
    print(f'현재 시간은 오전 {now.hour}시 {now.minute} 분입니다.')
else:
    print(f'현재 시간은 오후 {now.hour-12}시 {now.minute} 분입니다.')

# 퀴즈2 : if문과 datetime 모듈 이용
# 현재 달을 추출 now.month
# 달에 따라 봄, 여름, 가을 ,겨울 메세지 출력
# 12, 1,2 : 겨울
# 3~5 : 봄
# 6~8 : 여름
# 9~11 : 가을
# 출력은 아래와 같이한다.
# ?월은 ?입니다.

def printMonth():
    now = datetime.datetime.now()
    # 봄 구분
    # if now.month>=3 and now.month<=5:
    if 3 <= now.month <= 5:
        print("{}월은 봄입니다!".format(now.month))
    # 여름 구분
    elif 6 <= now.month <= 8:
        print("{}월은 여름입니다!".format(now.month))
    # 가을 구분
    elif 9 <= now.month <= 11:
        print("{}월은 가을입니다!".format(now.month))
    # 겨울 구분
    else:
        print("{}월은 겨울입니다!".format(now.month))

printMonth()

def printMonth2():
    now = datetime.datetime.now()
    if now.month in (12,1,2):
        print(f'{now.month}월은 겨울입니다')
    elif now.month in (3,4,5):
        print(f'{now.month}월은 봄입니다')
    elif now.month in (6,7,8):
        print(f'{now.month}월은 여름입니다')
    else:
        print(f'{now.month}월은 가을입니다')

printMonth2()

# 시간에 관련된 속성 리스트화
result = list(time.localtime(time.time()))
print(result) # [2020, 11, 10, 17, 39, 48, 1, 315, 0]
print(type(result))
result2 = ['년', '월', '일', '시', '분', '초']
# ? 년 / ? 월 / ? 일 / ? 시 / ? 분 / ? 초 /
for i in range(0, len(result2) ):
    print(result[i], end=' ')
    print(result2[i], end=' ')

print('\n'*2,'-'*30)
print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%X', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
print(time.strftime('%a %A', time.localtime(time.time())))
print(time.strftime('%p %I', time.localtime(time.time())))
print(time.strftime('%p %H', time.localtime(time.time())))
print(time.strftime('%Y %b', time.localtime(time.time())))



