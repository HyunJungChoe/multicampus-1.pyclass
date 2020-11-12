# 단어 추가 
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

# 단어읽기 함수
def readWord():
    print('[단어 모두 출력]')
    with open('output/word.txt', 'r', encoding='utf-8') as f:
        data_list = f.readlines()
        print(f'추가된 단어는 총 {len(data_list)}개 입니다')
        for item in data_list:
            print(item)