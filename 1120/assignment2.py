#1
# numbers = "1"+" "+"3"+" "+"3"+" "+"4"+" "+"4"
numbers = input("다섯개의 수를 공백으로 구분하여 입력하시오: ")
numbers_1 = numbers
numbers = numbers.split(" ")
numbers[0] = int(numbers[0])
numbers[1] = int(numbers[1])
numbers[2] = int(numbers[2])
numbers[3] = int(numbers[3])
numbers[4] = int(numbers[4])
numbers.sort()

if numbers[4] == numbers[3]:
    numbers.pop(4)

if len(numbers) > 3 and numbers[3] == numbers[2]:
    numbers.pop(3)

if len(numbers) > 2 and numbers[2] == numbers[1]:
    numbers.pop(2)

if len(numbers) > 1 and numbers[1] == numbers[0]:
    numbers.pop(1)

print("입력된 5개의 숫자: ",numbers_1)
print("두번째로 큰 숫자: ",numbers[-2])
