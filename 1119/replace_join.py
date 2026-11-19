print(" 정 상 가 동".replace(" ",""))
print(" 정 상 가 동".replace(" ","-"))
print("fault".replace("fault",'고장'))

#3,000 > 3000
print("3,000".replace(",",""))
#010-1234 5678
print("010-1234 5678".replace("-","").replace(" ","")) 

# 문자열.split(생략가능 구분자)
list = [10, 20, 30, "hello", False]
print(list[3])

coffee = "에스프레소 카페라테 아이스아메리카노"
list1 = coffee.split(" ")
print(list1)

# print

date = "2015-01-15"
day = date.split("-")[2]
print(day)
print(coffee.split(" ",1))
#1
status = "설비 정상 가동"
print(status.replace('정상','점검'))

#2
eqp = "PUMP A 03"
print(eqp.split(" "))

#3
letters = 'a,b,c,d'
print(letters.split(','))

#4
print(letters.split(',',1))

#구분자가될문자열.join([리스트])

list2 = ["2026", "11", "19"]
print("-".join(list2))
print(".".join(list2))

#1
list3 = ["2025", "01", "15"]
print("-".join(list3))

#2
date2 = "2025·1·15"
print(date2.replace("·","-"))
print(date2.replace("·",","))

#3
date3 = "2025/01/15"
date3_mod = date3.split("/")
print(("-").join(date3_mod))

word = "1, NORMAL, 25.3"
print(word.split(",")[1].strip().lower())

#practice
'''
1. text = "   PyThOn   " ->"python"

2. phone = "  010 - 1234 - 5678  " -> "01012345678"

3. name = "   kIM    cHUL   sOO   " -> "Kim Chul Soo"

4. filename = "  Sensor Data 2026.CSV  " -> "sensor_data_2026.csv"

5. data = "TEMP----PRESSURE----STATUS" -> "TEMP-PRESSURE-STATUS"
'''

#1
text = "   PyThOn   "
print(text.strip().lower())

#2
phone = "  010 - 1234 - 5678  "
print(phone.replace(" ","").replace("-",""))

#3
name = "   kIM    cHUL   sOO   "
print(" ".join(name.lower().title().split()))

#4
filename = "  Sensor Data 2026.CSV  "
print(filename.strip().replace(" ","_").lower(),"\n")


#5
print("#5")
data = "TEMP----PRESSURE----STATUS"
print("-".join(data.split("----")))

value = 25.1234

print(f'{value:.2f}측정값')