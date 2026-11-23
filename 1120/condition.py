score = 82
if score > 90:
    print("excellent")
elif score > 70:
    print("par")
else:
    print ("sub-par")

score = 91
if score > 90:
    print("excellent")
elif score > 70:
    print("par")
else:
    print ("sub-par")

score = 20
if score > 90:
    print("excellent")
elif score > 70:
    print("par")
else:
    print ("sub-par")

# score = int(input("please enter your score:"))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

age = 29
if age >= 20:
    print("you are of age")
else:
    print("you are underage")

#===== 삼항 연산자 ======
n = 5
if n%2 == 0:
    print("even")
else:
    print("odd")

# 참 일때 값 if 조건 else 거짓일때 값
result = "even" if n%2 == 0 else "odd"

print(result)

# match ~ case 
color = input("choose from red, yellow, green").strip()
# if red banned
# yellow warning
# green pass

match color:
    case "red":
        print("ban")
    case "yellow":
        print("caution")
    case "green":
        print("pass")
    case _:
        print("")

data = ["PUMP-01", 85, "WARNING"]

match data:
    case [name, temp, "WARNING"]:
        print(f'{name}: 온도 {temp}도, 주의상태입니다.')
    case [name, temp, "NORMAL"]:
        print(f'{name}: 온도 {temp}도, 정상상태입니다.')

id = "asdf"
pw = "1234"

in_id = input("enter your id")
in_pw = input("enter your pw")

if in_id == id and in_pw == pw:
    print("log in successful")
else:
    print("wrong id or pw")
    