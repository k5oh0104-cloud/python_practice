###### 문자열의 대소문자 #######
word = 'python'
sentence = 'I Love python'

# upper(), lower() -> 전체 변경
# capitalize(), title() -> 앞글자만 대문자로 변경
print(word.upper()) # PYTHON
print(sentence.upper()) # I LOVE PYTHON
print(word.count('p')) # 1, 원본 문자열은 변경되지 않음.

print("normal".upper())
print("WARNING".lower())
print("WARNING 경고".lower()) # warning 경고 (한글이나 특수문자는 그대로 유지)
print("python is good. i have an apple.".capitalize())
# Python is good. i have an apple.

print("python is good. i have an apple.".title())
# Python Is Good. I Have An Apple.

print("hong gil-dong".title())
print('apple'.lower()=='Apple'.lower()) # True

# isupper(), islower()
print('Apple'.islower(),'Apple'.isupper()) # False False
print('apple'.islower()) # True
print('APPLE'.isupper()) # True

''' (10분) ~11:20
1. 'ready' 대문자로 바꾸기
2. 'WARNING' 소문자로 바꾸기
3. 'kim chul soo' -> 성과 이름 각각 첫자 대문자로 바꾸기
4. 'fault' 'FAULT' 각각 저장후 동등비교하여 같다는 결과 확인하기
5. 'ABC', 'abc', 'Abc' -> isupper, islower 각각 검사하기
6. Sensor_LOG.CSV
(소문자 변경 후) sensor로 시작하는지, .csv로 끝나는지 확인
'''
print('ready'.upper())
print('WARNING'.lower())
print('kim chul soo'.title())
f1 = 'fault'
f2 = 'FAULT'
print(f1.upper() == f2.upper())
print('ABC'.islower(), 'ABC'.isupper()) # F T
print('abc'.islower(), 'abc'.isupper()) # T F
print('Abc'.islower(), 'Abc'.isupper()) # F F
file_name = 'Sensor_LOG.CSV'
file_name = file_name.lower()

print("sensor로 시작하는지 확인", file_name.startswith("sensor"))
print("확장자 확인 .csv", file_name.endswith(".csv"))

###### 문자열 공백 처리 #######
# strip(): 앞뒤 공백 제거
# lstrip(): 앞쪽 공백 제거, rstrip(): 뒤쪽 공백 제거
sentence = '  안녕하세요. 저는 allie입니다.    '
print(sentence+"!!")
print(sentence.strip()+"!!")
print(sentence.lstrip()+"!!")
print(sentence.rstrip()+"!!")

print("======== 절취선 =========".strip("="))

# allie를 대문자로 -> 결과
# 앞뒤공백 제거
# 문자 개수를 세기
print(sentence.upper())
print(sentence.upper().strip())
print(len(sentence.upper().strip()))

''' ~11:40
7. '  가동중 ' 변수로 저장 후 -> '[가동중]' 출력해보기
8. ' 대기 ' 변수로 저장 후 -> [대기 ]/[ 대기] 각각 출력
9. ***경고**** 저장, '*' 제거 후 `경고`만 출력
10. '  WARNING ' -> 'warning' 체이닝으로 출력하기
'''
prac1 = '  가동중 '
print('['+prac1.strip()+']')

prac2 = ' 대기 '
print('['+prac2.lstrip()+']')
print('['+prac2.rstrip()+']')

prac3 = '***경고****'
print(prac3.strip('*'))

print('  WARNING '.strip().lower())