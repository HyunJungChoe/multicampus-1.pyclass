
# 0으로 나누면 에러 발생 => ZeroDivisionError: division by zero

try:
    num = int(input('숫자입력 => '))
    # print(10/0)
    print(10/num)
# e는 에러메세지
# except ZeroDivisionError as e:
#     print(e, '0으로 나눌수 없어요')
except:
    print('나눌수 없어요')

print('-'*20)