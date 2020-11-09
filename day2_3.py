# 자료형의 종류
# 기본 자료형 - 문자열, 정수, 실수, 불린형
# 집합형 자료형=콜렉션 : 여러개의 구성요소로 조직화
#       : 리스트 [], 튜플 (), 딕셔너리 { }, 집합{ }
# CRUD : Create Read Update Delete

# 리스트 []
# 다른 데이터형 가능
# 순차적으로 생성
# 빈 리스트, 초기값 설정 방식
mylist=[]
# mylist[0]=100
# print(mylist[0])  #IndexError: list assignment index out of range
mylist.append(100)
mylist.append(200)
print(mylist)

# 서로 다른 데이터형으로 리스트 정의 => 파이썬 리스트의 특징중 하나
myList2 = [ '가나다', 20, True, False, 34.3445 ]
print(myList2, type(myList2)) # [] <class 'list'>

# 리스트 슬라이싱
a = [1, 2, 3, 4, 5]
print('-'* 20)
print(a[0:2])

# 리스트 연산
a =[1, 2, 3]
b =[4, 5, 6]
# print(a[2]+"hi")  # 형이 달라서 불가능
print(str(a[2]) + "hi")
print(a+b)

# 리스트 함수
# 리스트변수.함수명(옵션)
# 정의된 리스트에 새로운 값을 추가
# 리스트변수.append(값) : 마지막에 아이템이 추가
# 리스트변수.insert(삽입위치, 값) : 삽입위치에 아이템이 추가
food = []
print('-'*20)
print('food = ', food)
food.append('쫄면')
print('food = ', food)
food.append('칼국수')
print('food = ', food)
food.insert(0, '김밥')
print('food = ', food)
food.insert(0, '떡국')
print('food = ', food)

# 리스트 전체 길이 출력
# len(리스트변수)
# 리스트 데이터형 출력
# type(리스트변수)
singer = ['블랙핑크', 'BTS', '트와이스', 'ELS', '성시경']
print('-'*20)
print(f'singer = {singer}')
print(f'singer 리스트의 길이 = {len(singer)}')
print('-'*20)

# 입력받은 값으로 리스트를 생성하여라
# numberList = []
# print(f'numberList = {numberList}')
# item = input('리스트 아이템1 => ')
# numberList.append(item)
# print(f'numberList = {numberList}')
# numberList.append(input('리스트 아이템2 => '))
# print(f'numberList = {numberList}')

list1 = [10, 40, 23, 4, 77, 12]
list2 = ['하나', 'word', 'js', '234']
list3 = [10, 'google', True, '도레미파', 500 ]
print('-'*20)
print(f'list1 = {list1}')
# print(f'list1 = {list1.sort()}') # list1 = None
list1.sort()
print(f'list1 = {list1}')
list2.sort()
print(f'list2 = {list2}')
# list3.sort()
# print(f'list3 = {list3}') # 타입이 혼합되어 에러

# 리스트변수.count(값)
# 중복값이 몇개인가?
myList = [100, 300, 100, 100, True, True, False, '가', '가', '가다나']
print('-'*20)
print(f'myList = {myList}')
print(f'100의 중복 횟수 = { myList.count(100)}')
print(f'True의 중복 횟수 = { myList.count(True)}')
# 중복 인용부호 불가 =>
print(f"가의 중복 횟수 = { myList.count('가')}")
'''
100의 중복 횟수 = 3
True의 중복 횟수 = 2
가의 중복 횟수 = 2
'''

# 리스트변수.index(값)
# 값에 해당하는 요소가 몇번째에 위치하고 있는가?
print('-'*20)
print(f'myList = {myList}')
print(f'첫번째 True의 위치 = {myList.index(True)}')
print(f'첫번째 가의 위치 = {myList.index("가")}')
'''
myList = [100, 300, 100, 100, True, True, False, '가', '가', '가다나']
첫번째 True의 위치 = 4
첫번째 가의 위치 = 7
'''

# 퀴즈 1

'''
2개의 리스트를 정의하고 다음과 같이 출력한다.
myList1 : ['홍길동', '신데렐라', '알라딘', '장화', '홍련', '지니', '엘리스']
myList2 : ['토끼', '거북이', '물개', '펭귄']
2개의 리스트 합 : (결과값 출력 )
4개만 출력 : (결과값 출력 )
짝수번째만 출력 : (결과값 출력 )
홀수번째만 출력 : (결과값 출력 )
총 길이 :  11
'''
myList1 = ['홍길동', '신데렐라', '알라딘', '장화', '홍련', '지니', '엘리스']
myList2 = ['토끼', '거북이', '물개', '펭귄']
myList3 = myList1 + myList2
print(f'두 개 리스트 합 : {myList3}')
print(f'4개만 출력 : {myList3[:3]}')
print(f'짝수번째만 출력 : {myList3[1::2]}')
print(f'홀수번째만 출력 : {myList3[::2]}')
print(f'총 길이 : {len(myList3)}')
print('-'*30,'\n')

# 퀴즈 2
'''
리스트를 정의한 후 리스트 요소를 편집한다.
(변경, 삭제, 추가)
['사과', '배', '망고']
첫번째 요소 변경 후 : ['포도', '배', '망고']
마지막 위치에 요소 추가후 : ['포도', '배', '망고', '오렌지']
2번째 위치에 요소 추가후 : ['포도', '수박', '배', '망고', 
                        '오렌지']
마지막 위치 삭제 : ['포도', '수박', '배', '망고']
배 삭제 : ['포도', '수박', '망고']
'''

fruitList = ['사과', '배', '망고']
print(f'{fruitList}')
fruitList[0]= '포도'
print(f'첫번째 요소 변경 후 : {fruitList}')
fruitList.append('오렌지')
print(f'마지막 위치에 요소 추가 후 : {fruitList}')
fruitList.insert(1,'수박')
print(f'2번째 위치에 요소 추가 후 : {fruitList}')
fruitList.pop()
print(f'마지막 위치 삭제 : {fruitList}')
fruitList.remove('배')
print(f'배 삭제 : {fruitList}')
print('-'*30,'\n')


# 퀴즈 3
'''
데이터를 입력받은 후 리스트에 추가하는 예제입니다.
( input() 이용 )

좋아하는 음식은? 초밥
최근 본 영화는? 알라딘
좋아하는 가수는? BTS
좋아하는 숫자? 10
최근 여행지? 부산
당신에 관한 리스트 : ['초밥', '알라딘', 'BTS', 10, '부산' ]
'''

yourList = []
yourList.append(input('좋아하는 음식은? ... '))
yourList.append(input('최근 본 영화는?  ... '))
yourList.append(input('좋아하는 가수는? ... '))
yourList.append(input('좋아하는 숫자? ... '))
yourList.append(input('최근 여행지? ... '))
print(f'당신에 관한 리스트 : {yourList}')
print('-'*30,'\n')

# 퀴즈 4
'''
아래와 같이 리스트를 정의하고 다음과 같이 출력한다. 

foods = ['사과','망고','치즈케이크','주스']

우리집 냉장고에는?  ['사과', '망고', '치즈케이크', '주스']
동생이 사과를 먹었다 
우리집 냉장고에는?  ['망고', '치즈케이크', '주스']
이모가 수박을 사오셨다. 
우리집 냉장고에는?  ['망고', '치즈케이크', '주스', '수박']
동생 친구가 치즈케이크,수박을 먹었다. 
우리집 냉장고에는?  ['망고', '주스']

'''

foods = ['사과','망고','치즈케이크','주스']
print(f'우리집 냉장고에는?  {foods}')
print(f'동생이 {foods.pop(0)}를 먹었다 ')
print(f'우리집 냉장고에는?  {foods}')
foods.append('수박')
print(f'이모가 {foods[-1]}을 사오셨다. ')
print(f'우리집 냉장고에는?  {foods}')
print(f'동생 친구가 {foods.pop(1)},{foods.pop()}을 먹었다. ')
print(f'우리집 냉장고에는?  {foods}')

# 2개이상의 리스트 삽입
myList = [1 ,2, 3, 4, 5]
print(myList)
myList.extend(['가', '나'])
print(myList)
# 첫번째 위치에 2개 삽입
myList = [50, 90] + myList
print(myList)
# 2번째 위치에 n 개 삽입
myList = [myList[0]] + [True, False, True, True] + myList[1:]
print(myList)