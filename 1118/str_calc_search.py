print("설비" + "점검")
print("설비" + " " + "점검")
line = "="*20
print(line)

print(len("python"))
print(len("Strawberry Moon ~!"))

phone = "01012341234"
PhoneLength = len(phone)
print(PhoneLength)

hasWord = '고장' in '설비 고장을 예측하는 ~~'
hasWord2 = '고장' not in '설비 고장을 예측하는 ~~'

print(hasWord)
print(hasWord2)

message = "설비 고장 발생"
print("고장" in message)
print("정상" in message)

# 문자열a.count(문자열b) ; 문자열a에 문자열b가 몇개나 있는지 숫자값 반환
# 문자열a.find(문자열b) ; 문자열a에 문자열b가 언제 처음 등장하는지 반환 인덱스 번호 반환 없으면 -1 반환
# 문자열a.index(문자열b) ; 문자열a에 문자열b가 언제 처음 등장하는지 반환 인덱스 번호 반환 없으면 Error! 반환 

print("banana".count("a"))
print("banana".count("na"))

email = 'hong@company.com'
print("@의 인덱스 번호",email.find("@"))
print("@의 인덱스 번호",email.find("!"))

print("@의 인덱스 번호",email.index("@"))
# print("@의 인덱스 번호",email.index("!"))

aloha = "sensor-01-temp"
print(aloha.count("-"))
aloha1 = "temp_2024"
print(aloha1.find("_"))
print(aloha1.find("z"))