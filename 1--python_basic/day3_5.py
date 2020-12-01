#
# #
# # 반복문 : while
#
# # 변수 = 초기값
# # while 조건:
# #      실행명령
# #      변수증감
# # 조건이 True 이면 명령을 실행해라
#
# # Hello world n번 출력
# # cnt = 1
# # while cnt<=10:
# #     print(f'{cnt} => Hello Wrold')
# #     cnt += 1
# # print('while Test Finish')
#
#
# # # 숫자 역순 출력 (10 ~ 1)
# # cnt = 10
# # while cnt>0:
# #     print(cnt, end=' ')
# #     cnt -= 1
# # print('while Test Finish')
#
# print('-'*20)
# # 퀴즈 1~100까지 합구하기
# # 1~100까지의 합은... 5050
# cnt = 1
# tmp = 0
# while cnt <= 100:
#     tmp = cnt + tmp
#     cnt += 1
# print(tmp)
#
# # 1~50까지 짝수만 출력하기
# # 짝수는 n%2 == 0
# print('-'*20)
# cnt = 1
# while cnt<=50:
#     if cnt%2 == 0:
#         print(cnt)
#     cnt += 1
#
# print('-'*20)
# cnt = 2
# while cnt<=50:
#     print(cnt, end=' ')
#     cnt += 2
#
# # n단 출력하기
# '''
# 3 X 1 = 3
# 3 X 2 = 6
# ...
# 3 X 9 = 27
# '''
# num = int(input('숫자입력 ====> '))
# cnt = 1
# while cnt<=9:
#     print(f'{num} X {cnt} = {num*cnt}')
#     cnt += 1
# print('-'*20)
#
# # while 문 이용해서 리스트 요소 출력하기
# list1 = ['사과', '바나나', '수박', '포도']
# cnt = 0
# while cnt < len(list1):
#     print(f'{cnt+1} 번째 요소 => { list1[cnt] }')
#     cnt += 1
# print('-'*20)
#
# # 짝수번째 글자만 출력하기
# txt1 = '가나다라마바사'
# cnt = 1
# while cnt < len(txt1):
#     print('\t'*cnt, txt1[cnt])
#     cnt += 2
# print('-'*20)
#
# # 점선 출력후 문단 3번찍기 반복하기
# cnt1 = 1
# # cnt2 = 1
# while cnt1<=4:
#     cnt2 = 1
#     while cnt2<=3:
#         print('\t Hello World')
#         cnt2 += 1
#
#     print('-'*20)
#     cnt1 += 1
#
# # 2~9단 출력하기
# cnt1 = 2
# while cnt1<=9:
#     print(f' { cnt1 } 단')
#
#     cnt2 = 1
#     while cnt2<=9:
#         print(f' {cnt1} X {cnt2} = {cnt1*cnt2}')
#         cnt2 += 1
#
#     print('-'*20)
#     cnt1 += 1
#
#
# # 퀴즈 ) 리스트에서 가장 큰 값을 구한 후 큰 값을 리스트에서 삭제하여라
# # 리스트에서 요소 삭제
# # 리스트변수.pop() : 마지막 삭제
# # 리스트변수.pop(인덱싱값) : 인덱싱값에 해당하는 아이템 삭제
# # 리스트변수.remove(값) : 값에 해당하는 아이템 삭제
#


# break
# 반복문 안에서 사용
# 명령문 실행시 제어문에서 탈출한다.
# 명령문이 실행되면 하단 명령문들은 실행되지 않는다.
# 무한루프의 종료 조건시 사용

# continue
# 제어문 안에서 사용
# 명령문이 실행되면 하단 명령문들은 실행되지 않는다.

# 값을 입력받아서 리스트에 삽입한다.
# q를 입력하면 리스트를 출력한다.
result = []
while True:
    item = input('리스트 값 입력 (q를 입력하면 입력 종료)....')
    if item == "q":
        break
    else:
        result.append(item)
print(result)

# continue
# 반복문안에서 사용
# 명령문이 실행되면 하단 명령문들은 실행되지 않는다.
# 1~30까지 숫자중에서 3의 배수만 미출력
cnt = 0
while cnt < 30:
    cnt += 1
    if cnt%3 == 0:
        continue
    print(cnt, end=' ')
print('\ncontinue Test 종료')
