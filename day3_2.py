# 집합
# {값1, 값2, 값3....}
# CRUD :
# Create
# Read(전체조회만 가능)
# Update Delete
# 집합의 생성
# 집합변수 = set(리스트/문자열/튜플)
# 순서가 없다. 랜덤하게 출력된다.
# 인덱싱이 불가능하다. 슬라이싱 불가능하다.

# 중복값을 허용할까요? => 1개만 표시

# 집합의 생성
# 집합변수 = set(리스트/문자열/튜플)
# 집합변수 = {값1, 값2, 값3....}
# 순서가 없다. 랜덤하게 출력된다.
set1 = {100, 200, 300, 400}
set2 = set('가나다라마바사')
print(f'set1 = {set1}, type={type(set1)}')
print(f'set2 = {set2}, type={type(set2)}')
# set1 = {200, 100, 400, 300}, type=<class 'set'>
# set2 = {'다', '바', '나', '마', '사', '가', '라'}, type=<class 'set'>

# 비어있는 집합 만들기
# set3 = { } # 빈딕셔너리로 인식
set3 = set([])
print(f'set3 = {set3}, type={type(set3)}')
# set3 = set(), type=<class 'set'>

# Read(전체조회만 가능) => 인덱싱이 불가능하다. 슬라이싱 불가능하다.
# print(set1[0])
# TypeError: 'set' object is not subscriptable

# 중복값을 허용할까요? => 1개만 표시
set4 = {1, 2, 56, 78, 90, 100, 1, 1, 56, 6, 56}
print(f'set4 = {set4}, type={type(set4)}, length={len(set4)}')
# set4 = {1, 2, 100, 6, 78, 56, 90}, type=<class 'set'>

# 집합의 요소 추가
# 집합변수.add(값)
# 집합변수.update([값1, 값2...])
set3 = set('')
print(f'set3 = {set3}, type={type(set3)}, length={len(set3)}')
set3.add('오렌지')
print(f'set3 = {set3}, type={type(set3)}, length={len(set3)}')
set3.update(['바나나', '사과', '감자'])
print(f'set3 = {set3}, type={type(set3)}, length={len(set3)}')

# 집합의 요소 삭제
# 집합변수.remove(값)
# 집합변수.clear()
# del 집합변수 => 메모리에서 삭제
set3.remove('사과')
print(f'set3 = {set3}, type={type(set3)}, length={len(set3)}')
set3.clear()
print(f'set3 = {set3}, type={type(set3)}, length={len(set3)}')
del set3
# print(f'set3 = {set3}, type={type(set3)}, length={len(set3)}')
# NameError: name 'set3' is not defined

# 집합의 연산
# +, * => 불가능
set1 = {90, 6, 7, 55, 4}
set2 = {55, 4, 77, 100, 200}
# print(set1 + set2)
# print(set1*2)
# TypeError: unsupported operand type(s) for +: 'set' and 'set'


# 집합 합치기 = 합집합
# 집합변수3 = 집합변수1|집합변수2
# 집합변수3 = 집합변수1.union(집합변수2)
print('-'*20)
print(set1, set2)
print(set1|set2)
print(set1.union(set2))

# 교집합
# 집합변수3 = 집합변수1&집합변수2
# 집합변수3 = 집합변수1.intersection(집합변수2)
print('-'*20)
print(set1, set2)
print(set1&set2)
print(set1.intersection(set2))
# {4, 6, 7, 55, 90} {100, 4, 200, 77, 55}
# {4, 55}
# {4, 55}

# 차집합
# 집합변수3 = 집합변수1-집합변수2
# 집합변수3 = 집합변수1.difference(집합변수2)
print('-'*20)
print(set1, set2)
print(set1-set2)
print(set1.difference(set2))
# {4, 6, 7, 55, 90} {100, 4, 200, 77, 55}
# {90, 6, 7}
# {90, 6, 7}

# 캐스팅
# 집합 => 리스트 : list(집합변수)
# 집합 => 튜플 : tuple(집합변수)
# 집합 => 딕셔너리
# 집합 => 문자열
set5 = set('도레미파솔라시도')
print('-'*20)
print(set5, type(set5))
print(list(set5), type(list(set5)))
print(tuple(set5), type(tuple(set5)))
result = dict(enumerate(set5))
print(result, type(result))
result = ' '.join(set5)
print(result, type(result))