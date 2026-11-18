# 실습 1
print("== 실습 1 ==")
a = 17
b = 5
print("a+b:",a+b)
print("a-b:",a-b)
print("a*b:",a*b)
print("a/b:",a/b)
print("a/b 몫:",a//b)
print("a/b 나머지:",a%b)
print("a^b:",a**b)
print("")

# 실습 2
print("== 실습 2 ==")
a = int(input("첫번째 숫자"))
b = int(input("두번째 숫자"))
c = int(input("세번째 숫자"))
sum = a + b + c
print("평균:", sum/3, "직육면체의 부피:", a*b*c)
print("")

# 실습 5
print("== 실습 5 ==")
prod = 500
defect = 23
time = 24
operation = 21
print("불량률:",(defect/prod)*100,"%")
print("가동률:",(operation/time)*100,"%")

print("")

# 실습 6
print("== 실습 6 ==")
min = 500
print(min//60, "시간", min%60, "분")
print("")

# 실습 7
print("== 실습 7 ==")
sec = 98765
day = sec//86400
hr = sec//3600 - day*24
minu = sec//60 - day*24*60 - hr*60
print(day, "일", hr, "시간", minu, "분", sec%60, "초")
print("")

# 실습 8
print("== 실습 8 ==")
temp_sensor = 85
temp_check = temp_sensor >= 60 and temp_sensor <= 90
pres_sensor = 5
pres_check = pres_sensor >= 3 and pres_sensor <= 7
result = temp_check and pres_check
print("온도 정상:", temp_check, "압력 정상:", pres_check, "종합 결과:", result)
print("")