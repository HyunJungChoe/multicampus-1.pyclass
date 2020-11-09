
# 캐스팅
# 딕셔너리 => 리스트
# 리스트 => 딕셔너리
# 값만 모아서 리스트로 생성
# list(딕셔너리변수) => 키값만으로 생성된 리스트


# 리스트 => 딕셔너리(인덱싱숫자가 키값이 된다)
# 리스트 => enumerate(리스트,문자열,튜플)
#   => dict(enumerate(리스트,문자열,튜플))
# dict()
# enumerate(리스트,문자열,튜플)
# : 리스트,문자열,튜플 같은 자료형을 enumerate 객체로 반환
# enumerate 객체의 요소는 딕셔너리 스타일. 키값은 숫자로 표시

dict1 = {'a':'apart', 's':'say', 'd':'drama', 'c':'camera', 'y':'yes'}
print(f'dict1 = {dict1}, type={type(dict1)}')
result1 = list(dict1)
result2 = dict1.keys()
result3 = list(result2)
print(f'result1 = {result1}, type={type(result1)}')
# result1 = ['a', 's', 'd', 'c', 'y'], type=<class 'list'>
print(f'result2 = {result2}, type={type(result2)}')
# result2 = dict_keys(['a', 's', 'd', 'c', 'y']), type=<class 'dict_keys'>
print(f'result3 = {result3}, type={type(result3)}')
# result3 = ['a', 's', 'd', 'c', 'y'], type=<class 'list'>

# 딕셔너리 => 리스트
# 키나 값만 모아서 리스트로 생성
# list(딕셔너리변수) => 키값만으로 생성된 리스트
# list(딕셔너리변수.keys()) => 키값만으로 생성된 리스트
# list(딕셔너리변수.values()) => 값만으로 생성된 리스트
dict1 = {'a':'apart', 's':'say', 'd':'drama', 'c':'camera', 'y':'yes'}
print(f'dict1 = {dict1}, type={type(dict1)}')
result1 = list(dict1)
result2 = dict1.keys()
result3 = list(result2)
print(f'result1 = {result1}, type={type(result1)}')
# result1 = ['a', 's', 'd', 'c', 'y'], type=<class 'list'>
print(f'result2 = {result2}, type={type(result2)}')
# result2 = dict_keys(['a', 's', 'd', 'c', 'y']), type=<class 'dict_keys'>
print(f'result3 = {result3}, type={type(result3)}')
# result3 = ['a', 's', 'd', 'c', 'y'], type=<class 'list'>
result4 = list(dict1.values())
print(f'result4 = {result4}, type={type(result4)}')

# 리스트 => 딕셔너리(인덱싱숫자가 키값이 된다)
# 리스트 => enumerate(리스트,문자열,튜플) => enumerate 객체
#   => dict(enumerate(리스트,문자열,튜플)) => 딕셔너리
# dict()
# enumerate(리스트,문자열,튜플)
# : 리스트,문자열,튜플 같은 자료형을 enumerate 객체로 반환
# enumerate 객체의 요소는 딕셔너리 스타일. 키값은 숫자로 표시

list1 = ['도라지','지하수','수국']
print('-'*10)
print(f'list1 = {list1} type={type(list1)}')
result1 = enumerate(list1)
print(f'result1 = {result1} type={type(result1)}')
# result1 = <enumerate object at 0x000002A55352FB00> type=<class 'enumerate'>
result2 = dict(result1)
print(f'result2 = {result2} type={type(result2)}')
# result2 = {0: '도라지', 1: '지하수', 2: '수국'} type=<class 'dict'>
print(result2[0])
list2 = ['Red','Green','Blue']
result3 = dict(enumerate(list2))
print(f'result3 = {result3} type={type(result3)}')

# 튜플 => 딕셔너리
t1 = (100, 200, 300, 400, 500)
print(f't1 = {t1} type={type(t1)}')
# t1 = (100, 200, 300, 400, 500) type=<class 'tuple'>
result = dict(enumerate(t1))
print(f'result = {result} type={type(result)}')

# 문자열 => 딕셔너리
txt1 = '가나다라마바사'
print(f'txt1 = {txt1} type={type(txt1)}')
result = dict(enumerate(txt1))
print(f'result = {result} type={type(result)}')

