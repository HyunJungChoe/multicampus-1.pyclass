# 자판기 클래스 정의
class Vending_machine:
    # 속성 => 지역, 메뉴, 가격
    # 생성자 함수 정의
    def __init__(self, v_name, product, price):
        self.v_name = v_name
        self.product = product
        self.price = price

    # 메뉴와 가격을 표시하는 메서드 정의
    # 메뉴와 가격은 자료형은 튜플
    def show_menu(self):
        print('='*40)
        print('\t',self.v_name)
        print('='*40)
        for i in range(len(self.product)):
            print(f'메뉴{i+1} : {self.product[i]} / {self.price[i]} 원')

    # 투입 금액에 따른 메세지 출력 메서드
    # input_money 메서드에서 투입금액 속성명(self.input_money)가
    # 메서드명하고 동일하면
    # 무한루프로 실행시 오류가 발생하오니
    # self.input_money 를 다른 이름으로 수정해주세요
    # 예) self.in_money

    def input_money(self):
        print('주문하실 메뉴의 금액을 입력해주세요')
        # 숫자 형태인지 판독
        while True:
            # 투입되는 금액은 클래스 속성으로 정의
            self.in_money = input('투입 => ').strip()
            if self.in_money.isdigit():
                # 자료형 변경
                self.in_money = int(self.in_money)
                # 투입금액이 메뉴의 최소금액보다 큰지 확인
                if self.in_money >= int(min(self.price)):
                    print('주문이 가능합니다.')
                    # 메뉴 선택과 주문 메서드 호출
                    self.get_drink()
                    break
                else:
                    print('주문이 불가능합니다.')
                    print(f'투입금액 환불 => {self.in_money}원')
                    # break
            else:
                print('주문이 불가능합니다. 다시 투입해주세요')

    # 메뉴 선택 후 선택 제품 완료 메세지
    def get_drink(self):
        # 1줄 메뉴 출력
        print('=' * 40)
        for i in range(len(self.product)):
            print(str(i+1)+'.'+ self.product[i], end='    ')
        print(' (환불 및 다시 시작 q')
        print('=' * 40)
        sel = input('선택 => ').strip()
        if (sel == 'q'):
            print(f'투입금액 환불 => {self.in_money}원')
            # break
        # 숫자 입력 : 1~메뉴길이
        elif sel.isdigit():
            sel = int(sel)
            # 올바른 메뉴 선택
            if 0 < int(sel) <= len(self.product):
                print(f'주문하신 {self.product[sel-1]}가 나왔습니다.')
            else:
                print('선택 번호의 메뉴가 없습니다.')
                self.get_drink()
        # 'q' 입력도 아니고 숫자도 아닌경우
        else:
            print('잘못된 입력입니다.')
            self.get_drink()

    # 실행 메서드 정의
    def start(self):
        # 첫화면
        self.show_menu()
        # 금액 투입
        self.input_money()



print('-'*50)
# 객체 인스턴스화
vm1 = Vending_machine('강남점',('아메리카노', '라떼'), (1200, 2000))
vm1.start()
# vm1.show_menu()
# vm1.input_money()

print('-'*50)
# vm2 = Vending_machine('부산역점',('수박쥬스','아이스아메리카노', '카푸치노', '탄산수'), (2000, 700, 1500, 1300))
# vm2.start()
# vm2.show_menu()
# vm2.input_money()
# print('-'*50)

#  주말 스터디
# 자판기 클래스 완성 - 추가 기능
#  - 금액이 맞지는 않는데 음료 주문이 된다?
#  - 투입 금액에 맞는 음료만 나오게 수정
#  - 잔돈이 있다면 잔돈 출력
#  - 자판기 프로그램은 무한루프로 진행
