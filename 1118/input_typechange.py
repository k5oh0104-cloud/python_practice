#입력 함수 
age = int(input("나이를 입력하세요: "))
name = input("이름을 입력하세요: ")
print("제 이름은 " + name + "입니다.")
print("제 나이는 " + str(age) + "살입니다.")

number_A = input("첫 번째 숫자를 입력하세요: ")
number_B = input("두 번째 숫자를 입력하세요: ")
print("두 수의 합은 " + number_A + number_B + "입니다.")


# 형 변환
# int() : 정수형으로 변환, float() : 실수형으로 변환, str() : 문자열로 변환

##### 입력함수 input()
# name = input("이름을 입력해주세요.")
# print("제 이름은", name, "입니다.")

# age = input("나이를 입력해주세요.")
# print("제 나이는 " + age + "입니다.")

# number_A = input("덧셈 연산을 할 첫번째 숫자를 입력해주세요:")
# number_B = input("덧셈 연산을 할 두번째 숫자를 입력해주세요:")
# print(number_A + number_B) # 10 + 5 = 105
# # number_A, number_B의 자료형 확인 직접 해보기
# print("입력되는 숫자의 데이터타입(자료형):", type(number_A)) # <class 'str'>
# => 실제 숫자 연산을 하기 위해선 형변환을 해야함.

# ======== 형변환 =========
# int(), float(), str()


print("==== float() 확인 ====")
print("int -> float", float(25)) # 25.0
print("정수형 str -> float", float("25")) # 25.0
print("실수형 str -> float", float("25.5")) # 25.5
print("==== int() 확인 ====")
print("float-> int", int(25.8)) # 25
print("정수형 str -> int", int("25")) # 25
# print("실수형 str -> int", int("25.8")) # ValueError
print("==== str() 확인 ====")
print("int -> str", str(25))
print("float -> str", str(25.2))

# 형변환 입력 같이 써보기!!
# number_A = input("첫번째 숫자를 입력해주세요")
# number_B = input("두번째 숫자를 입력해주세요")
# number_A = int(number_A)
# number_B = int(number_B)
# print("덧셈 결과:", number_A + number_B)

# n1 = int(input("숫자를 입력해주시오(1)"))
# n2 = int(input("숫자를 입력해주시오(2)"))
# print("n1, n2 자료형 확인", type(n1))
# print("뺄셈 결과:", n1 - n2)

height = int(input("당신의 키를 입력해주세요.: ")) # float("188.5")
age = int(input("당신의 나이를 입력해주세요.: "))
print("당신의 키는", height, ", 나이는", age, "입니다.")

name = input("당신의 이름을 입력해주세요.: ")
print("안녕하세요", name, "님.")