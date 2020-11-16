
def testPrint():
    print('-'*40)
    print('test.py 에 등록된 testPrint() 호출')

def HelloMessage(m):
    print('test.py 에 등록된 HelloMessage() 호출')
    print(f'Hello {m}')

# 메인으로 실행될때만 특정 메세지 출력하기
if __name__ == '__main__':
    print('메인으로 실행됨')


