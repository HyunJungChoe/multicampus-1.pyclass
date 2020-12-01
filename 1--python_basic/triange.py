
class Triangle:
    # 생성자 메서드
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height

    # 속성 출력 메서드
    def printInfo(self):
        print(f'이름 = {self.name}')
        print(f'밑변 = {self.width}')
        print(f'높이 = {self.height}')
        print('====================')

    # 넓이 구하기 메서드
    def printArea(self):
        print(f'삼각형 넓이 = {(self.width*self.height)/2:.2f}')
        print('====================')