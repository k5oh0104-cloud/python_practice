#1
data1 = "pump-07 | 08:30 | TEMP=085.5C | STATUS=normal "
data2 = "PUMP_07,09:00,92.0C,WARNING"

data1_mod = data1.strip().replace("TEMP=","").replace("STATUS=","").replace("C","").lower().split(" | ")
data2_mod = data2.replace("_","-").replace("C","").lower().split(",")
data1_mod[2] = data1_mod[2].replace("0","")

print("==== 센서 데이터 비교 ====")
print("설비 코드:", data1_mod[0])
print("최초 측정:", (" / ").join(data1_mod[1:4]))
print("최근 측정:", (" / ").join(data2_mod[1:4]),"\n")
data1_mod[2] = float(data1_mod[2])
data2_mod[2] = float(data2_mod[2])
print(f'동일 설비 여부 : {data1_mod[0]==data2_mod[0]}')
print(f'온도 변화량 (C) : {(data2_mod[2] - data1_mod[2])}C')
print(f'온도 상승률 (%) : {(data2_mod[2] - data1_mod[2])/data1_mod[2]*100:.2f}%')
print(f'온도 급상승 여부 : {(data2_mod[2] - data1_mod[2])>6}')