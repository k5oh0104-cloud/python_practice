#1
line1 = " LOT-A | 1,200 | 36 | 8h "
line2 = "lot_a,850,17,5h"
line1 = line1.replace(",","").replace("-","_").strip().upper().split(" | ")
line2 = line2.upper().split(",")

prod1 = int(line1[1])
def1 = int(line1[2])
time1 = int(line1[3].replace("H", ""))

prod2 = int(line2[1])
def2 = int(line2[2])
time2 = int(line2[3].replace("H", ""))

print(line1)
print(line2,"\n")

prod_total = prod1 + prod2
def_total = def1 + def2
def_rate1 = def1/prod1*100
def_rate2 = def2/prod2*100
def_rate_total = def_total/prod_total*100


prod_rate1 = prod1/time1
prod_rate2 = prod2/time2

print("==== 생산 데이터 분석 ====")
print(f'생산라인 코드: {line1[0]}')
print(f'라인 코드 일치: {line1[0] == line1[1]} \n')

print(f'[1차 생산] 생산량{prod1}개/불량품{def1}개')
print(f'불량률: {def_rate1:.2f}%\n')

print(f'[2차 생산] 생산량{prod2}개/불량품{def2}개')
print(f'불량률: {def_rate2:.2f}%\n')

print(f'[통합 분석] 생산량{prod_total}개/불량품{def_total}개')
print(f'통합 불량률: {def_rate_total:.2f}%')
print(f'시간당 평균 생산량: {prod_total/(time1 + time2):.2f}개\n')

print(f'불량률 개선 여부: {def2 <= def1}')
print(f'최종 판정: {def2 <= def1}')