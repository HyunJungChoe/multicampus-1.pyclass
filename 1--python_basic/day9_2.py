
import re


# 정규표현식 (Regular Expression)
# 유효성 검사
# 특정 문자열이 특정 조건(패턴)에 맞는지 검사
# 회원가입시 주민등록번호가 맞는가?
# ??????-?....
# 핸드폰번호 형식이 맞는가?
# 01?-????-????
# 회원가입시 비밀번호 설정 형식이 맞는가?
# 자릿수+특수문자+숫자+대소문자+영문형태인가?

# 파이썬에서 정규표현식 모듈 => re (내장모듈)
import re

# re 객체의 속성과 메소드 확인
# dir(모듈명이나 클래스명) => 지원되는 속성과 함수의 목록을
# 리스트로 표시한다.
print(dir(re))

# 방식1
# 패턴변수 = re.compile(패턴식)
# 패턴변수.정규표현식메소드(문자열)

# 패턴식 메타문자
# ^:문자열의 처음을 나타냄
# $:문자열의 끝

# 문자열이 특정 글자로 시작하는가? - ^a, ^ca
# 문자열이 특정 글자로 끝나는가? - $y

# 정규표현식메소드
# match(문자열) : 문자열 처음부터 검색 => 문자열 / None
# search(문자열) : 문자열 전체 검색 => 문자열 / None
# findall(문자열) : 정규식과 매치되는 문자열을 리스트로 반환
# => 리스트 / []
# finditer(문자열)
# : 정규식과 매치되는 문자열을 반복가능한 객체로 반환
# => 반복가능한객체. for문으로 개별 결과 확인

pat1 = re.compile('^ab')
print(pat1, type(pat1))
# re.compile('^ab') <class 're.Pattern'>
# 결과값을 리스트로 반환
print(pat1.findall('above')) # ['ab']
print(pat1.findall('boy'))  # []
# Match Object / None 로 반환 / None
print(pat1.search('above'))
# <re.Match object; span=(0, 2), match='ab'>
print(pat1.search('boy')) # None
# callable_iterator 집합형 객체로 반환
print(pat1.finditer('above'))
print(pat1.finditer('pineapple'))
for item in pat1.finditer('above'):
    print(item)
# <re.Match object; span=(0, 2), match='ab'>
for item in pat1.finditer('pineapple'):
    print(item)

# 패턴에 맞는 문자열찾기
txt1 = "가나다 009 python ?### 7834 파이썬 java WORD 784 ENGLISH JavaScript"
# 한글만 추출
# re.findall(패턴식, 문자열변수)
result1 = re.findall('[가-힣]', txt1)
print(result1) # ['가', '나', '다', '파', '이', '썬']
print(type(result1))
result2 = re.findall('[가-힣]+', txt1)
print(result2) #['가나다', '파이썬']

# 숫자만 추출
print(re.findall('[0-9]', txt1))
# 집합으로 변환 => 중복 숫자 제거
print(set(re.findall('[0-9]', txt1)))

# 대문자소문자 추출
print(re.findall('[a-z]+', txt1))
# ['python', 'java', 'ava', 'cript']
print(re.findall('[a-zA-Z]+', txt1))
# ['python', 'java', 'WORD', 'ENGLISH', 'JavaScript']

# 한글, 숫자
print(re.findall('[0-9가-흫]+', txt1))
# ['가나다', '009', '7834', '파이썬', '784']


# Match object 메서드
# group() : 매치된 문자열을 리턴한다.
# start() : 매치된 문자열의 시작 위치를 돌려준다.
# end() : 매치된 문자열의 끝 위치를 돌려준다.
# span() : 매치된 문자열의 시작,끝 위치를 튜플 형태로 돌려준다.
print('-'*50)
result = re.finditer('[가-힣]+', txt1)
for item in result:
    print(item)
    print(item.group(), item.span(), item.start(), item.end())

