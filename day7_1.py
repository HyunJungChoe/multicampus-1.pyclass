
# import os
# print(os.getcwd())

# 프로그래밍 설계 기법
# 절차지향
# 객체지향

# 클래스란?
# 설계도
# 함수의 집합
# 속성(정적인거. 특징) + 메서드(집합)의 집합

# 객체화(인스턴스화)
# 클래스를 이용해서 실제 결과물을 생성하는 과정

# 고양이 클래스
# 속성(특징) - 종류 , 성별, 나이, 이름
# 메서드(동적인거) - 잔다. 먹는다. 달리다. 고양이 속성 출력. 걷는다.
# class 클래스명:
#   생성자 메서드 정의 (속성 정의)
#   def __init__(self, 인자 ):
#       self.속성 = 인자
#       self.속성 = 리터럴값
#       self.속성 = (인자값1, 인자값2,...) # 튜플형태
#
#   일반 메서드 정의
#   def 메서드명(self, 인자):
#       명령문
#       returen 문


class Cat:
    # 속성 정의 : 생성자 메서드
    def __init__(self, kind, name, age, gender):
        self.kind = kind
        self.name = name
        self.age = age
        self.gender = gender
        self.animalKind = '고양이'

        # 속성 출력 메서드

    def printInfo(self):
        print(f'====== {self.animalKind} =========')
        print(f'kind = {self.kind}')
        print(f'name = {self.name}')
        print(f'age = {self.age}')
        print(f'gender = {self.gender}')

    # 동작과 관련된 메서드 정의
    def run(self):
        print(f'{self.animalKind} {self.name}가 달리다.')

    def eat(self, food):
        print(f'{self.animalKind} {self.name}가 {food}를(을) 먹는다.')

    def sleep(self, where):
        print(f'{self.animalKind} {self.name}가 {where}에서 잔다.')
        '''잠을 자는 동작입니다.'''

    # 정의된 메서드를 이용해서 메서드 정의
    # 정의된 메서드 호출 가능
    # self.메서드명(인자)
    def actionPrint(self):
        print(f'{self.animalKind} {self.name}의 아침')
        self.eat('물')
        self.eat('사료')
        self.run()
        self.sleep('캣타워')

# 객체화
# 객체인스턴스명 = 클래스명(값...)
cat1 = Cat('스핑크스','줄리아',1,'여')
cat2 = Cat('코캣', '나비', 10, '남')
# 메서드 호출
# 객체인스턴스명.메서드(인자)
cat1.printInfo()
cat1.sleep('침대')
cat1.run()
cat1.eat('우유')
cat1.actionPrint()


class Test:
    # 클래스 변수 = 공용변수
    # 생성자 함수안에 정의하지 않고 별도 정의
    # 클래스변수 = 값
    msg = 'Hello World'

    # 생성자 함수 = 속성 정의
    def __init__(self, color):
        self.name = '테스트 클래스'
        self.color = color

    # 출력 메서드
    def print_info(self):
        print(f'{self.name}, {self.color}, {self.msg}')

# 상속이란?
# 부모클래스의 속성이랑 메소드를 그대로 가진다.
# class 클래스이름(부모클래스1,부모클래스2...)
# 다중 상속이 가능하다.
# 코드 재사용

# 부모클래스1 - 아파트, 차
# 부모클래스2 - 오피스텔, 전동스쿠터
# 자식클래스 - 아파트, 차 , 오피스텔, 전동스쿠터

# 부모 클래스1 생성
class Papa:
    # 속성 정의
    def __init__(self):
        self.firstName1 = '홍'
    # 메서드 정의
    def info1(self):
        print('Papa - 아파트, 차')

# 부모 클래스2 생성
class Mama:
    # 속성 정의
    def __init__(self):
        self.firstName2 = '김'
    # 메서드 정의
    def info2(self):
        print('Mama - 오피스텔, 전동스쿠터')


# 2개의 클래스를 상속받은 자식 클래스 생성
class Child(Papa, Mama):
    # 생성자 함수 정의
    def __init__(self):
        # 부모클래스의 속성을 사용할 수 있게 생성자 함수 정의
        # 부모클래스명.__init__(self)
        Papa.__init__(self)
        Mama.__init__(self)
        # 새로운 속성 정의
        self.myname = '길동'



# 부모 클래스 객체 인스턴스화
papa1 = Papa()
print(papa1.firstName1)
papa1.info1()
print('-'*30)
mama1 = Mama()
print(mama1.firstName2)
mama1.info2()
print('-'*30)
# 자식클래스 객체 인스턴스화
child1 = Child()
# 부모 클래스의 메서드를 바로 호출할 수 있다.
child1.info1()
child1.info2()


# 부모 클래스의 속성을 호출할 수 있다.
# 상속받은 부모클래스의 속성
print(child1.firstName1, child1.firstName2)
# 자신의 클래스의 속성
print(child1.myname)
# 자신의 클래스의 메서드
child1.info3()
print('-'*30)
# 부모 클래스의 메서드 호출 테스트
papa1.test1('좋은 하루되길...')
child1.test1('편안한 하루되길 ')

class Animal:
    def __init__(self, objName, leg):
        self.objName = objName
        self.leg = leg

    def info(self):
        print(f'종류: {self.objName} \n다리 수: {self.leg}')

    def run(self):
        print(f'{self.objName}이(가) 달린다.')

    def eat(self, food):
        print(f'{self.objName}이(가) {food}을(를) 먹는다.')

class Dog(Animal):
    def __init__(self, objName, leg):
        Animal.__init__(self, objName, leg)

    def printName(self, name):
        print(f'{self.objName}의 이름은 {name}이다.')

    def shout(self, sound):
        print(f'{self.objName}이(가) {sound} 짖는다.')


