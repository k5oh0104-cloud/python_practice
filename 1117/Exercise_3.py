# 실습 1
print("== 실습 1 ==")
count = 3
print("count:", count)
temp = 25.5
print("temp:", temp)
name = "line 3"
print("name:", name)
is_ok = temp <= 27.0
print("is_ok:", is_ok)
print("")
print("machine status:")
if is_ok == True:
    print("OK")
else:
    print("NG")

print("")

# 실습 2
print("== 실습 2 ==")
print("count data type:", type(count))
print("temp data type:", type(temp))
print("name data type:", type(name))
print("is_ok data type:", type(is_ok))
print("")

# 실습 3
print("== 실습 3 ==")
# 1. 100은 소수점이 없는 숫자이므로 int 자료형으로 예상됨
# 2. 100.0은 소수점을 포함한 숫자이므로 float 자료형으로 예상됨
# 3. "100"은 숫자를 포함하나 "" 안에 있으므로 str 자료형으로 예상됨
print("100 data type:", type(100))
print("100.0 data type:", type(100.0))
print('"100" data type:', type("100"))
print("")

# 실습 4
print("== 실습 4 ==")
print(3 + 4)
print("3" + "4")
print("24" + "58")
# 숫자끼리의 연산은 우리가 알고 있는 1 + 1 = 2이고, 문자열끼리의 연산은 안 + 녕 = 안녕 이므로
# 문자열의 3 + 4 = 34, 같은 원리로 24 + 58 = 2458
print("")

# 실습 5
print("== 실습 5 ==")
print("3 > 2:", 3 > 2)
print("5 = 5:", 5 == 5)
print('"5 = 5" data type:',type(5==5))
print("")

# 실습 6
print("== 실습 6 ==")
a = 100
print("100 data type:",type(a))
a = 100.0
print("100.0 data type:",type(a))
a = "a"
print('"a" data type:',type(a))

print("")

# 실습 7
print("== 실습 7 ==")
device_temp = 24.5
print("device temp:", device_temp)
check_count = 2
print("check count:", check_count)
device_name = "slot die"
print("device name:", device_name)
is_normal = device_temp <= 27.0
print("device status:", is_normal)
print("")