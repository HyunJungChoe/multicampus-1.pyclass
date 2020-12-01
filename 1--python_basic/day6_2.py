
# 퀴즈 1
# 'data/coding.txt' 문서를 읽고 코딩이라는 단어가 들어간 어구를 리스트화 한 후
# 총 갯수를 출력하는 함수를 코딩하여라.
# 특정단어  in 리스트

'''
파일명 :  data/coding.txt
코딩이라는 글자가 들어간 어구 출력
: ['코딩을', '코딩을', '코딩에', '코딩을', '코딩을', '코딩을', '코딩도', '코딩에', '코딩은', '코딩을', '코딩도', '코딩', '코딩도', '코딩을', '코딩을']
총 갯수는? 15
'''

print('퀴즈 1')
def fileread(fileUrl, op):
    f = open(fileUrl,'r', encoding=op)
    # String
    data = f.read()
    # print(data)
    # 문자열변수.split() =>공백을 기준으로 리스트화
    myList = data.split()
    # print(myList)
    # 특정 글자가 삽입된 리스트 생성
    resultList = []
    for item in myList:
        if '코딩' in item:
            resultList.append(item)
    print('*'*30)
    print('파일명 : ', fileUrl)
    print(f'코딩이라는 글자가 들어간 어구 출력 : {resultList}')
    print(f'총 갯수는? {len(resultList)}')
    f.close()

fileread('data/coding.txt', 'utf-8')




# 퀴즈 2
# 퀴즈1에서 작성한 코딩소스를 이용하여 문서경로, 단어, 인코딩 값을 함수로 전달한 후
# 다음과 같은 결과가 출력되도록  함수를 변경하여라

# # 함수 호출
# fileread2('data/coding.txt', '습관', 'utf-8')
# fileread2('data/color.txt', '주황', 'utf-8')

'''
******************************
파일명 :  data/coding.txt
습관 글자가 들어간 어구 출력 : ['습관', '습관을', '습관을', '습관이', '습관을']
총 갯수는? 5


******************************
파일명 :  data/color.txt
주황 글자가 들어간 어구 출력 : ['주황을', '주황을', '주황은', '주황을']
총 갯수는? 4
'''


print('퀴즈 2')
def fileread2(fileUrl, word, op):
    f = open(fileUrl,'r', encoding=op)
    # String
    data = f.read()
    # print(data)
    # 문자열변수.split() =>공백을 기준으로 리스트화
    myList = data.split()
    # print(myList)
    # 특정 글자가 삽입된 리스트 생성
    resultList = []
    for item in myList:
        if word in item:
            resultList.append(item)
    print('*'*30)
    print('파일명 : ', fileUrl)
    print(f'{word} 라는 글자가 들어간 어구 출력 : {resultList}')
    print(f'총 갯수는? {len(resultList)}')
    f.close()

# 함수 호출
fileread2('data/coding.txt', '습관', 'utf-8')
fileread2('data/color.txt', '주황', 'utf-8')





# 퀴즈 3
# readline()를 이용하여 문서에서 첫줄만 출력하고 아래와 같이
# 첫줄의 공백과 공백 사이, 앞과 뒤에 특정 문자열을 삽입하여라
'''
******************************
파일명 :  data/coding.txt

 첫줄만 출력 : 
 코딩을 잘하는 사람의 특징


 첫줄을 변경하여 출력 : 
 **코딩을 / 잘하는 / 사람의 / 특징**
'''

print('퀴즈3')
def readFirstLine(fileUrl, op):
    f = open(fileUrl,'r', encoding=op)
    # 1행만 문자열로 데이타 저장
    data = f.readline()
    print('*' * 30)
    print('파일명 : ', fileUrl)
    print('\n 첫줄만 출력 : \n', data)
    # data_list = data.split()
    # print(data_list) # ['코딩을', '잘하는', '사람의', '특징']
    # '구분자'.join(문자열/문자열리스트/튜플리스트)
    # print('** ' + (' / '.join(data_list)) + ' ** ')
    data = '**' + ' / '.join(data.split()) + '** '
    print('\n 첫줄을 변경하여 출력 : \n' , data)
    f.close()

readFirstLine('data/coding.txt', 'utf-8')





# 퀴즈 4
# readlines()를 이용하여 문서에서 특정 행부터 행까지를 출력하도록
# 함수를 코딩하여라
#

'''
# readFirstLines('data/color.txt', 'utf-8', 13, 15) 함수 호출시 

파일명 :  data/color.txt

13행부터 15행 까지 출력
******************************
13 행 : ORANGE를 좋아하는 사람

14 행 : * 심성이 착하고, 다른 사람들과 함께 있기를 좋아하고, 귀가 엷고 충성심이 강하며 솔선 수범형.

15 행 : * 인정이 많다. 유쾌한 성격.

'''

'''
# readFirstLines('data/Yesterday.txt', 'cp949', 8, 12) 함수 호출시

파일명 :  data/Yesterday.txt
총 행 수 :  30

8행부터 12행 까지 출력
******************************
8 행 : There's a shadow hanging over me
9 행 : Oh, yesterday came suddenly
10 행 : Why she had to go,
11 행 : I don't know She wouldn't say
'''


print('\n 퀴즈4 ')
def readFirstLines(fileUrl, op, row1, row2):
    f = open(fileUrl,'r', encoding=op)
    data = f.readlines()
    print('*'*30)
    print('\n\n파일명 : ', fileUrl)
    print(data)
    print( '총 행 수 : ',len(data) )
    print( f'\n {row1}행부터 {row2}행 까지 출력' )
    print('*' * 30)
    for i in range(row1, row2+1):
        print(f'{i} 행 : {data[i]}')
    f.close()

readFirstLines('data/color.txt', 'utf-8', 12, 15)
readFirstLines('data/Yesterday.txt', 'cp949', 7, 12)





# 퀴즈 5
# n개의 단어를 입력받은 후 output.txt 파일로 저장하여라
'''
# inputWriteFile(5, 'output/output.txt', 'utf-8') 함수 호출시 결과

단어를 입력하세요 ... 장발장
단어를 입력하세요 ... 신데렐라
단어를 입력하세요 ... 콩쥐팥쥐
단어를 입력하세요 ... 라푼젤
단어를 입력하세요 ... 선녀와 나뭇꾼
입력된 단어 리스트는 ['장발장', '신데렐라', '콩쥐팥쥐', '라푼젤', '선녀와 나뭇꾼'] 입니다.
5 개의 단어가 모두 저장되었습니다.
'''

'''
# inputWriteFile(2, 'output/output.txt', 'utf-8') 함수 호출시 결과물 
단어를 입력하세요 ... 오늘도 좋은 하루 
단어를 입력하세요 ... 꽃길만 걷자
입력된 단어 리스트는 ['오늘도 좋은 하루 ', '꽃길만 걷자'] 입니다.
2 개의 단어가 모두 저장되었습니다
'''



def inputWriteFile(n, url, op):
    wordList = []
    for i in range(0, n):
        wordList.append(input('단어를 입력하세요 ... '))
    print(f'입력된 단어 리스트는 {wordList} 입니다.')

    f = open(url,'w', encoding=op)
    for item in wordList:
        data = item+'\n'
        f.write(data)
    print(n, '개의 단어가 모두 저장되었습니다.')
    f.close()

# inputWriteFile(5, 'output/output1.txt', 'utf-8')
# inputWriteFile(2, 'output/output2.txt', 'utf-8')




# 퀴즈 6
# black.txt 파일에 white.txt 파일의 내용을 추가하여라

with open('data/black.txt','r', encoding='utf-8') as f1:
    temp = f1.read()
    print(temp)

with open('data/white.txt','a', encoding='utf-8') as f2:
    f2.write('\n\n'+temp)
    print('내용 추가가 완료되었습니다. ')


# 퀴즈7 파일읽기, 쓰기, 추가 기능을 이용하여 다음과 같은 프로그램을 작성하여라.
# 파일에 추가되는 단어의 글자수는 2글자로 제한한다.

'''
** 퀴즈7 **

------------------------------
메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   1

[단어 추가]
두 글자로 구성된 단어를 입력하세요송아지
두글자가 아닙니다.
두 글자로 구성된 단어를 입력하세요사과
단어가 입력되었습니다.

메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   1

[단어 추가]
두 글자로 구성된 단어를 입력하세요자두
단어가 입력되었습니다.

메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   2

[단어 모두 출력]


추가된 단어는 총 2 입니다.
사과

자두



메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   3

[파일 내용 모두 삭제]
단어 목록을 모두 삭제하였습니다.

메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   2

[단어 모두 출력]


추가된 단어는 총 0 입니다.


메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료   4


프로그램을 종료합니다.
'''

# 단어추가 함수
# 단어 길이가 2이어야 한다.
def addWord():
    print('[단어 추가]')
    with open('output/word.txt', 'a', encoding='utf-8') as f:
        while True:
            word = input('두 글자로 구성된 단어를 입력하세요...').strip()
            if len(word) == 2:
                f.write(word+'\n')
                print('단어가 추가되었습니다.')
                break
            else:
                print('두글자의 단어가 아닙니다.')


# 추가 기능 - 스터디
# 1) 단어 연속 추가
# 2) 폴더와 초기 파일(word.txt) 생성

# 단어읽기 함수
def readWord():
    print('[단어 모두 출력]')
    with open('output/word.txt', 'r', encoding='utf-8') as f:
        dataList = f.readlines()
        print(f'\n추가된 단어는 총 {len(dataList)} 입니다.')
        for i in dataList:
            print(i, end='')

# 단어모두삭제 함수
def clearWord():
    print('[단어 모두 삭제]')
    with open('output/word.txt', 'w', encoding='utf-8') as f:
        f.write('')
        print(f'단어 목록을 모두 삭제하였습니다.')


def start():
    while True:
        # 문자열.strip() = 입력글자옆에 공백이 들어간 경우 공백 삭제
        ans = input('메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료 ...').strip()
        if ans == '1':
            addWord()
        elif ans == '2':
            readWord()
        elif ans == '3':
            clearWord()
        elif ans == '4':
            print('프로그램을 종료합니다.')
            break
        else:
            print('1~4 입력 숫자가 아닙니다.')

print('-'*50)
# 초기 단어장 파일 생성
# with open('output/word.txt', 'w', encoding='utf-8') as f:
#     f.write('')
# 프로그래밍 시작
start()

