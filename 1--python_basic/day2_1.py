
# 문자열 반복
# 방법1
print('파이썬')
print('파이썬')
print('파이썬')
print('*'*30)

# 방법2
#  \n 개행, \t 왼쪽 여백
print('파이썬\n'*3)
print('*'*30)

# 방법3
print('파이썬\n파이썬\n파이썬')
print('*'*30)

# 방법4 - 문자열 멀티라인 기법
multiline = '''
파이썬
파이썬
파이썬
'''

# 퀴즈 2
# 홍길동 씨의 과목별 점수는 다음과 같다.
# 홍길동 씨의 평균 점수를 소숫점 둘째자리까지 출력하여라
'''
국어 : 86
영어 : 77
수학 : 55
평균 :
'''
kor = 86
eng = 77
math = 55
avg = (kor+eng+math)/3
print(f'평균 : {avg:.2f}')

# 퀴즈 3
# 변수 a,b를 입력문을 이용하여 데이터를 저장한다.
# == 을 이용하여 a,b 가 같은지 True, False 로 출력하여라
'''
a ? 10
b ? 10
True
'''
# 변수명 = input(메세지)
a = input('a ? ')
b = input('b ? ')
print(a==b)
print('='*30,'\n')

n1 = int(input('첫번째 숫자를 입력하세요?'))
n2 = int(input('두번째 숫자를 입력하세요?'))

print('\n\n결과 : ')
# print(' 문자열 %자료형1 %자료형2 ' % (변수1, 변수2))
print('%d + %d = %d' % (n1, n2, n1+n2))
print('%d - %d = %d' % (n1, n2, n1-n2))
print('%d * %d = %d' % (n1, n2, n1*n2))
print('%d / %d = %d' % (n1, n2, n1/n2)) # 34 / 56 = 0
print('%d / %d = %.2f' % (n1, n2, n1/n2)) # 34 / 56 = 0.61

# 퀴즈 5
# 홍길동씨의 주민등록번호는 881120-1068234
# 연월일과 숫자 부분을 나누어서 출력하여라.
'''
연월일 : 881120
숫자 : 1068234
'''
jumin = '881120-1068234'
num1 = jumin[0:6]
num2 = jumin[7:]
print('-'*20)
print(f'연월일 : {num1}')
print(f'숫자 : {num2}')

