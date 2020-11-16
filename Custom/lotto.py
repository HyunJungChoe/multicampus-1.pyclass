# Custom 패키지의 lotto.py
import random

def lottoNumber() :
    lottoList = []
    while True:
        if len(lottoList)>= 6:
            break
        else:
            data = random.randint(1,45)
            if data not in lottoList:
                lottoList.append(data)
    print(lottoList)

lottoNumber()

if __name__ =="__main__":
    print('Main 으로  실행되었음')