
# 자료선언
# 변수 < 콜렉션 (리스트, 튜플, 집합, 딕셔너리) <
# 함수 < 클래스 < 모듈(파일단위) < 패키지(폴더 단위)

# 함수의 종류
# - 사용자정의 함수
# - 내장함수 (import 명령 X)
# - 외장함수 (import 명령 O) : random, os....

# 모듈의 종류
# - 빌트인 모듈 (pip install x)
# - 외장 모듈 (pip install o) : pandas, numpy, seaborn ...
# - 사용자정의 모듈 : 직접만들어서 임포트

# -------------------------
# 모듈의 호출방법 1
# import 모듈이름
# 모듈이름.함수(인자)
# 모듈이름.속성
# math 모듈은 빌트인 모듈인데 수학함수 제공
# import math
# print(f' pi = {math.pi}')
# print(f' sin(10) = {math.sin(10)}')
'''
 pi = 3.141592653589793
 sin(10) = -0.5440211108893698
'''

# 모듈의 호출방법 2 - 별칭
# import 모듈이름 as 별칭
# 호출된 모듈의 함수 호출방법2
# 별칭.함수(인자)
# import math as m
# print(f' pi = {m.pi}')
# print(f' sin(10) = {m.sin(10)}')


# 모듈의 호출방법 3
# from 모듈이름 import 모듈함수
# 호출된 모듈의 함수 호출방법3
# 모듈함수(인자)
# 모듈명 없이 바로 함수나 속성 호출 가능
# sin, cos, pi 함수만 사용
# from math import sin, cos, pi
# print(f' pi = {pi}')
# print(f' sin(10) = {sin(10)}')
# print(f' sin(10) = {cos(10)}')

# 설치형 모듈이란?
# 파이썬이나 아나콘드를 설치시 미설치 모듈
# 1) 설치 확인  - 예) requests - 웹상의 페이지를 파이썬과 연동하는 모듈. 스크래핑
#   - 파이참 : [File]-[Setting] Project-interpreter 항목에서 모듈 확인
#   - 터미널 모드에서 명령으로 확인 : pip list
# 2) 모듈 설치하기
#   - 파이참 : [File]-[Setting] Project-interpreter
#   - 터미널 모드 이용
#     pip install 모듈명  예) pip install requests
#     conda install 모듈명  예) conda install requests

# 설치모듈 확인
# - flask, pymysql
# - beautifulsoup4,requests

# requests 모듈 테스트
# 방법1
# 모듈명으로 접근 - 모듈명.함수명(인자)
# requests.get(url) => 온라인상의 웹페이지 연동
# import requests
# respons = requests.get('http://naver.com')
# print(respons.content)
# 방법2
# 모듈명을 별칭으로 접근 - 별칭.함수명(인자)
# requests.get(url) => 온라인상의 웹페이지 연동
# import requests as r
# respons = r.get('http://naver.com')
# print(respons.content)

# 방법3
# 모듈명안의 특정함수 사용  - 함수명(인자)
# requests.get(url) => 온라인상의 웹페이지 연동
from requests import get
respons = get('http://naver.com')
print(respons.content)


# 사용자정의 모듈
# 다른 파이썬 파일에 있는 함수나 클래스를 사용하고 싶다면?
# import 파일명(모듈명)
# test.py, triange.py 모듈 임포트
import test, triange

test.testPrint()
test.HelloMessage('Python')

# 객체화
t1 = triange.Triangle('삼각형1', 20, 20)
t1.printInfo()
t1.printArea()

# 파이참에서 패키지용도의 폴더만들기
# [Project] 창에서 폴더 마우스우측버튼
# [New]-[python package]
# 패키지폴더가 생성되고 자동으로 __init__.py 파일 생성
# __init__.py
# : 패키지폴더임을 알려주는 파일

# 별도패키지폴더명 - AAA
# 패키지안의 모듈 파일 - AAA/a.py
# 모듈파일안에 함수 정의 - testPrint()

# AAA패키지안의 a.py 에 정의된 testPrint 함수 호출하기
# import 패키지명.모듈명
# 패키지명.모듈명.함수(인자) 호출
# import AAA.a
# AAA.a.testPrint()

# import 패키지명.모듈명 as 별칭
# 별칭 .함수(인자) 호출
# import AAA.a as Aa
# Aa.testPrint()

#  from 패키지명.모듈명  import 함수명
# 함수(인자) 호출
# from AAA.a import testPrint
# testPrint()

import Custom.lotto
Custom.lotto.lottoNumber()