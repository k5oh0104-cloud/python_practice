name = "홍길동"
age = 25
print("제 이름은 "+ name + ", 나이는 "+ str(age) + "살입니다.")
print(f'제 이름은 {name}, 나이는 {age}살입니다.')

'''
# ① 설비명·온도를 변수로 저장 → ② f-string을 사용해서 예상 결과와 같이 출력

# ① 세 점수를 변수로 저장 → ② f-string을 사용하여 평균을 구하는 계산식을 사용해 출력

# ① 측정값 87.456 저장 → ② 소수점 첫 번째 자리와 두 번째 자리까지 각각 출력

# ① 문자열 '  5 , sensor_2 , WARNING , 0.78912  ' 저장
# ② strip·split 후 각 조각 정리, 소수점은 두 번째 자리까지

'''

#1
print("1f")

eqp = "co"
temp = "83"
print(f"장비명 {eqp}, 온도 {temp}.")

#2
a = 1
b = 2
c = 3
print(f'평균 점수는 {a+b+c/3}')

#3
meas = 87.456
print(f"to first decimal {meas:.1f}")
print(f"to second decimal {meas:.2f}")

#4
list = '  5 , sensor_2 , WARNING , 0.78912  '
list = list.strip().split(" , ")
print(list)
print(f"{list[0]}, {list[1]}, {list[2]}, {float(list[3]):.2f}")
