
# 프로그래밍 언어의 종류
# 절차지향 - c
# 객체지향 - java, javascript, c++, c#, python
# 사물(사용자, 아이템...) 의 단위가 객체


# 클래스 : 특별한 자료구조
#         변수 + 함수
# 관련 키워드 => OOP, 인스턴스=객체

# 기본자료형(숫자, 문자열, 불른)
# 콜렉션형 (리스트, 집합, 튜플, 딕셔너리)
# 함수

# 기본자료형 < 집합형(리스트, 집합, 튜플, 딕셔너리) < 클래스(함수(메서드)+변수(속성)의 조합) < 모듈 < 라이브러리 < 패키지

# 클래스 ( 속성, 함수 ...) => 틀
# 인스턴스=객체=Object
#   => 클래스에 의해서 만들어진 산출물

# 클래스란? 설계도/틀 -> 붕어빵틀
# => 인스턴스(객체) -> 붕어빵
# 자동차 설계도 => 클래스
# 자동차 => 객체

# 클래스 생성 문법
# 클래스이름은 첫글자는 대문자로 지정
# class 클래스이름:
#   명령문

# 인스턴스 생성하기
# 인스턴스명은 첫글자는 소문자로 지정
# 인스턴스변수 = 클래스이름()
# isinstance(인스턴스변수, 클래스이름)
# 특정클래스에 의해서 생성된 인스턴스가 맞는지 출력
# True / False 로 출력

# 자동차 클래스
class Car:
    pass

print(Car, type(Car))
# <class '__main__.Car'> <class 'type'>

# 인스턴스 생성
# 인스턴스변수 = 클래스이름()
car1 = Car()
car2 = Car()
print(car1, type(car1))
print(car2, type(car2))
'''
<__main__.Car object at 0x0000019DE43B8640> <class '__main__.Car'>
<__main__.Car object at 0x0000019DE4417FD0> <class '__main__.Car'>
'''

class Bus:
    pass
bus1 = Bus()

# 인스턴스?가 클래스?에 의해서 생성되었는가?
# isinstance(인스턴스변수, 클래스이름)
print(isinstance(car1, Car))
print(isinstance(car2, Car))
print(isinstance(bus1, Car))
print(isinstance(bus1, Bus))

# 사각형 클래스 정의
# 속성 - 가로, 세로, 색상, 스타일
class Square:
    # 생성자 함수 정의
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.style = '줄무늬'
        self.maker = ('영희', '철수', '미미')

    # 속성 출력 클래스 메서드(함수 개념) 정의
    def printInfo(self):
        print(f' square color = {self.color} ')
        print(f' square width = {self.width} ')
        print(f' square height = {self.height} ')
        print(f' square style = {self.style} ')
        print(f' square maker = {self.maker} ')

    # 사각형의 넓이를 반환하는 클래스 메서드 정의
    def area(self):
        return self.width * self.height

# 인스턴스, 객체 생성
square1 = Square(50, 100, 'Red')
square2 = Square(30, 30, 'Yellow')

print(square1)
print(square2)

print(f'square1.color : {square1.color}')
print(f'square2.color : {square2.color}')

# 속성을 출력하는 클래스 메서드 호출
# 인스턴스명.메서드(인자)
square1.printInfo()
print('-'*30)
square2.printInfo()

# 넓이를 구하는 클래스 메서드 호출
print(f' square1의 넓이는? {square1.area()}')
print(f' square2의 넓이는? {square2.area()}')

class Bread:
    # 생성자 함수 - 속성
    def __init__(self, kind, price, kcal, src):
        self.kind = kind
        self.price = price
        self.kcal = kcal
        self.src = src
        self.brand = "파리바게뜨"

    # 속성 출력 클래스 메서드(함수 개념) 정의
    def printInfo(self):
        print(f' 종류 = {self.kind} ')
        print(f' 가격 = {self.price} ')
        print(f' 칼로리 = {self.kcal} ')
        print(f' 재료 = {self.src} ')
        print(f' 브랜드 = {self.brand} ')

    # 빵수에 따른 가격 계산 메서드
    def printPrice(self, count ):
        print(f' {self.kind}를 {count} 개 주문하셨습니다.')
        print(f' 주문 가격 = {self.price*count}')


# 빵 인스턴스 생성
# kind, price, kcal, src
bread1 = Bread('팥빵',3500, 300, ('밀가루','팥','설탕'))
bread1.printInfo()
bread1.printPrice(5)
print('-'*30)
bread2 = Bread('마늘바게트',5500, 150, ('밀가루','마늘','버터'))
bread2.printInfo()
bread2.printPrice(2)





