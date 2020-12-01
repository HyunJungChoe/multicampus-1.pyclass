
# 딕셔너리
# CRUD : Create Read Update Delete

# 딕셔너리 생성 - 초기값 지정
# 딕셔너리변수 = {키1:값1, 키2:값2,...}
# 키값은 문자형, 숫자형 둘다 가능

dict1 = {'a':'apple' , 'b':'banana' , 'c':'cat'}
dict2 = {100:'apple' , 200:'banana' , 300:'cat'}
print(dict1, type(dict1))
print(dict2, type(dict2))
'''
{'a': 'apple', 'b': 'banana', 'c': 'cat'} <class 'dict'>
{100: 'apple', 200: 'banana', 300: 'cat'} <class 'dict'>
'''

# 딕셔너리 생성 - 빈 딕셔너리 생성 후 값 추가
# 딕셔너리 요소 추가
# 딕셔너리변수[키값]=값
# 위치 인덱싱은 안된다.
# 키 값으로만 호출 가능, 값은 중복 가능하지만 키값은 중복 불가.
dict3 = {}
print(dict3, type(dict3), len(dict3))

dict3[100] = '백'
dict3[200] = '이백'
dict3[300] = '삼백'
print(dict3)
print(dict3[300])
# print(dict3['삼백'])  # 불가능

# 딕셔너리 중복키는 가능할까요?
# 값은 같아도 되지만 키값이 중복되면 마지막 키값만 유효하다
print('-'*20)
dict4 = {'a':'apple' , 'b':'banana' , 'c':'cat', 'a':'apart'}
print(dict4) # {'a': 'apart', 'b': 'banana', 'c': 'cat'}
print(dict4['a'])

# 딕셔너리 값 교체
# 딕셔너리[키값]=값
dict4['c'] = 1000
print(dict4)

# 딕셔너리 요소 삭제
# 딕셔너리변수.clear()
# 딕셔너리변수.pop(키값)
# del 딕셔너리변수
# del 딕셔너리변수[키값]
dict4.pop('a')
print(dict4)
dict4.clear()
print(dict4)
del dict4
# print(dict4)
# NameError: name 'dict4' is not defined

# 딕셔너리에서 키값만 리스트로 만들어서 마지막 키값 조회
# result = list(dict2.keys())
# print(result)
# print(result[-1])
print('-'*20)
print(list(dict2.keys()))
print(list(dict2.keys())[-1])