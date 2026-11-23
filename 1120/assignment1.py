#1
temp = 78
vib = 3.2
current = 52
# temp = input("온도를 입력하세요: ")
# vib = input("진동을 입력하세요: ")
# current = input("전류를 입력하세요: ")

if temp > 80 or vib > 4.0:
    print('위험: 즉시 정지')
elif current > 60 and temp > 70:
    print('주의: 부하 점검')
elif vib > 2.5:
    print('주의: 진동 관찰')
else: 
    print('정상')