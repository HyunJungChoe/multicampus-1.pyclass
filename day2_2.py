
# 샘플 문자열 만들기
# https://www.lipsum.com/
sampleTxt = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed id dolor vitae turpis auctor pretium. Integer nibh lectus, feugiat id lobortis consequat, condimentum id sapien. Quisque vitae dui massa. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Ut sit amet rhoncus elit. Proin et bibendum quam, et egestas dolor. Phasellus ac tempus nulla. Maecenas sollicitudin et ante eu efficitur. Donec sed eros vitae justo bibendum faucibus. Pellentesque rutrum diam non mauris tristique ultricies. Vestibulum luctus pulvinar nisi, sed rhoncus lorem lobortis quis. Duis mattis nulla mauris, nec efficitur mauris rutrum et.
Phasellus tincidunt justo elit, non pharetra purus sodales in. Mauris ultrices mauris at enim posuere convallis. Nunc tincidunt magna a sem rutrum, non maximus justo blandit. Proin purus ligula, pretium a dolor vitae, luctus placerat sapien. Sed elementum tortor massa, vitae semper felis aliquet a. In pretium, nibh ut luctus dictum, nisl orci commodo urna, eu maximus lectus metus vitae urna. Sed rhoncus, dui eu fringilla egestas, metus justo ultricies libero, eget tristique neque felis vitae nulla.
'''
print(sampleTxt)

# 특정 문자열의 갯수 출력
# 문자열변수.count(찾고자하는문자열)

# 특정 문자열의 시작인덱스 위치 반환
# 문자열변수.find(찾고자하는문자열)
# 찾고자 하는 문자열이 없다면 -1 반환
# 문자열변수.index(찾고자하는문자열)
# 찾고자 하는 문자열이 없다면 에러 발생
# 특정 문자열의 갯수 출력
# 문자열변수.count(찾고자하는문자열)
print('a 의 갯수', sampleTxt.count('a') )
print('dolor 의 갯수', sampleTxt.count('dolor') )
# 특정 문자열의 시작인덱스 위치 반환
# 문자열변수.find(찾고자하는문자열)
# 찾고자 하는 문자열이 없다면 -1 반환
# 문자열변수.index(찾고자하는문자열)
# 찾고자 하는 문자열이 없다면 에러 발생

print('첫번째 a의 위치값은?', sampleTxt.find('a')) # 23
print('첫번째 가의 위치값은?', sampleTxt.find('가')) # -1
print('첫번째 a의 위치값은?', sampleTxt.index('a')) # 23

print('-'*20)
print('sampleTxt is 의 갯수', sampleTxt.count('is') )
result = sampleTxt.replace('is', 'was')
print('sampleTxt is 의 갯수', sampleTxt.count('is') )
print('sampleTxt was 의 갯수', sampleTxt.count('was') )
print('result was 의 갯수', result.count('was') )

# 문자 개수 세기
a = "hobby"
print('b 개수 : ',a.count('b'))
# 연결 문자 .join()
word = "Python"
print(' * '.join(word))

# 좌우 공백 제거
# .strip()
# .lstrip()
# .rstrip()

word = "    Python    "
print('-'*20)

print(f'**{word}**')
print(f'**{word.rstrip()}**')
print(f'**{word.lstrip()}**')
print(f'**{word.strip()}**')
