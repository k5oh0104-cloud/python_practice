# 실습 1 심화
print("== 실습 1 ==")
code = input("코드를 입력하시오:")
a = code.startswith("SEC")
print("조건1:",a)
b = len(code)==15
print("조건2:",b)
c = code[4:8]=="2026"
print("조건3:",c)
d = code.endswith(("X" or "Y"))
print("조건4:",d)
e = int(code[9:13]) >= 1000 and int(code[9:13]) <= 9999
print("조건5:",e)
f = code.count("-") == 3
print("조건6:",f)
print(code, ", 최종 결과:",a and b and c and d and e and f)

code = "SEC-2026-0833-X"
a = code.startswith("SEC")
b = len(code)==15
c = code[4:8]=="2026"
d = code.endswith(("X" or "Y"))
e = int(code[9:13]) >= 1000 and int(code[9:13]) <= 9999
f = code.count("-") == 3
print("SEC-2026-0833-X , 최종 결과:",a and b and c and d and e and f)