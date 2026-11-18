#실습 1 
print("가동 점검표","\n", "1.\t온도\t확인", "\n", "2.\t압력\t확인")
print("""가동 점검표
 1.	온도	확인
 2.	압력	확인""")

#실습 2 
eqp1 = "Pump_A"
status = "normal"
date = "2025-01-01"
print(eqp1,status,date,sep="/")
print(eqp1 + "/" + status + "/" + date)
print("in progress", end="...")
print("done")