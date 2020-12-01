
import os
# 파일변수  = open(파일경로, 'r', encoding='utf-8/cp949')
# 파일변수.read() : 파일전체 문자열 구조 =>  문자열
# 파일변수.readline() : 파일에서 첫줄만 읽기 => 문자열
# 파일변수.readlines() : 각행이 리스트 구조로 변경 => 리스트

# 파일 목록 확인 [Ctrl]+[SpaceBar]
# UnicodeDecodeError: 'cp949' 인코딩 에러 encoding='utf-8'

f = open('data/color.txt', 'r', encoding='utf-8')
# print(f.readlines())
# print(type(f.readlines()))
data_list = f.readlines()
print(data_list)
print(len(data_list)) # 61
f.close()

def File_sumAvr(url, op):
    # 파일 변수 생성
    f = open(url, 'r', encoding=op)
    # 리스트화
    data_list = f.readlines()
    # 문자열 숫자 => 숫자 리스트로 변경
    temp = []
    for item in data_list:
        temp.append(int(item))
    # 합계구하기
    sum = 0
    for item in temp:
        sum += item
    # 평균구하기
    avg = sum / len(temp)
    print('\t', '-' * 30)
    print(f'\t파일명 = {url}')
    print(f'\t데이타 = {temp}')
    print(f'\t총합 = {sum}, 평균 {avg:.3f}')
    f.close()

def mkf():
    # output 폴더 생성
    # 현재 작업폴더를 기준으로 폴더 생성
    os.mkdir('output')
    folder_file_list = os.listdir(os.getcwd())
    print('output' in folder_file_list) # True

    # 빈파일 만들기
    f = open('output/test1.txt', 'w', encoding='cp949')
    f.close()

    # output 폴더안에 파일 생성되었는지 확인
    os.chdir('output')
    print(os.getcwd())
    folder_file_list = os.listdir(os.getcwd())
    print('test1.txt' in folder_file_list) # True

def p1():
    # for문 이용해서 파일 내용 추가하기
    f = open('output/test3.txt', 'w', encoding='utf-8')
    print('test3.txt 파일 쓰기가 시작되었습니다')
    f.write('='*40)
    f.write('\n Test \n')
    for i in range(1,11):
        f.write(f'{i} 번째 행입니다.\n')
    f.write('='*40)
    f.close()

def p2():
    # 리스트 요소를 파일 내용으로 쓰기
    foodList = ['라면', '김밥', '모밀', '초밥', '제육볶음']
    f = open('output/test4.txt', 'w', encoding='utf-8')
    f.write('=' * 40)
    f.write('\n Test \n')
    # TypeError: write() argument must be str, not list
    # f.write(foodList)
    f.write(str(foodList))
    for item in foodList:
        f.write('\n\t' + item)
    f.write('\n')
    f.write('=' * 40)
    f.close()

def quiz1():
    print('-'*20)
    f = open('data/Yesterday.txt', 'r', encoding='utf-8')
    data_list = f.readlines()[:10]
    # temp = []
    # for item in data_list:
    #     temp.append(item)
    # print(temp[:10])
    print(data_list)
    f.close()

    f2 = open('output/result-Yesterday.txt', 'w', encoding='utf-8')
    f2.write('=' * 40)
    f2.write('\n')
    for item in data_list:
        f2.write('\n\t' + item)
    f2.close()

def p3():
    # with 문과 파일 입출력
    # 파일.close() 를 사용할 필요가 없다.
    # with open(파일경로, 'a'/'w'/'r', encoding='utf-8/cp949')  as 파일변수:
    #   명령문

    print('---------------------')
    # with 명령어로 파일 읽기
    with open('data/color.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        print(data)

    # with 명령어로 파일 쓰기
    with open('output/test5.txt', 'w', encoding='utf-8') as f:
        # 10~1
        for i in range(10, 0, -1):
            f.write(str(i) + '\n')

    # with 명령어로 내용 추가하기
    with open('output/test5.txt', 'a', encoding='utf-8') as f:
        f.write('=' * 30)
        for i in range(1, 10):
            f.write('\n')
            f.write(f'{i} 단 \n')
            for j in range(2, 10):
                f.write(f'{i} X {j} = {i * j} \n')

def p4_del():
    # 파일 삭제 유무 확인후 삭제하기
    ans = input('output/deleteTest.txt 경로의 파일을 삭제하시겠습니까? (y)')
    if ans == 'y':
        os.remove('output/deleteTest.txt')
        print('파일이 삭제되었습니다.')

def p5_del():
    # 파일이 있다면 삭제하기
    print(os.getcwd())
    os.chdir('output')
    print(os.getcwd())
    fileList = os.listdir(os.getcwd())
    print(fileList)

    if 'deleteTest.txt' in fileList:
        os.remove('deleteTest.txt')
        print('파일이 삭제되었습니다.')
    else:
        print('파일이 이미 삭제된 상태입니다. ')


if __name__ == '__main__':
    # File_sumAvr('data/data_kor.txt', 'utf-8')
    # File_sumAvr('data/data_eng.txt', 'cp949')
    # mkf()
    # p1()
    # p2()
    # quiz1()
    # p3()
    # p4_del()
    p5_del()