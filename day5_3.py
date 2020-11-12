
import os
# # 현재 작업 폴더
# print(os.getcwd())
#
# # 작업 폴더 변경
# os.chdir('data')
# print(os.getcwd())
#
# # 목록을 리스트로 출력
# print(os.listdir(os.getcwd()))


# 파일 변수 생성
# f = open('data/Yesterday.txt','r')
# print(f, type(f))
# <_io.TextIOWrapper name='data/Yesterday.txt' mode='r' encoding='cp949'> <class '_io.TextIOWrapper'>

# 문서 전체 => 문자열
# data = f.read()
# print(type(data)) # <class 'str'>
# print(data)

# 첫 행
# print('-'*20)
# data = f.readline()
# print(type(data))
# print(data)

# 한 줄씩 리스트로 출력
# print('-'*20)
# data = f.readlines()
# print(type(data))
# print(data)
# print('-'*20)
# for i in range(0,5):
#     print(data[i])
#
# f.close()

# 특정 파일을 읽은 후
# 파일의 단어전체수와 3개의 단어가
# 표시되는 함수를 정의하여라

# >> 함수호출
# printWord('data/Yesterday.txt',utf-8)
# >> 결과값
# 파일명 : data/Yesterday.txt
# 단어 갯수 : 134
# 단어 3개 출력
# ['Yesterday', 'All', 'my']

def printWord(url, option):
    f =open(url, 'r', encoding=option)
    data = f.read()
    data_list = data.split()
    print('\n\n --결과 값--')
    print(f'파일 명:{url}')
    print(f'단어 개수 :{len(data_list)}')
    print(f'단어 3개 출력 :{data_list[0:3]}')
    f.close()

printWord('data/Yesterday.txt', 'utf-8')
printWord('data/color.txt', 'utf-8')






