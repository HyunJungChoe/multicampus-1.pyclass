



# #1
# sum = 0
# for i in range(1,101):
#     sum =+ i
# print(f'1부터 100까지 합은 {sum}입니다.')
#
# #2
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j}', end = '\t')
#
#     print('\n')

f = open("C://새파일.txt", 'a')
print('종료 하려면 q를 눌러주세요')
while(1):

    txt = input()
    if txt == 'q':
        break
    f.write(txt)
f.close()