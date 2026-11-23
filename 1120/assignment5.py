#1
num_input = input("다섯개의 숫자를 공백으로 나눠 입력해주세요.\n").split(" ")
numbers = [num_input[0], num_input[1], num_input[2], num_input[3], num_input[4]]
numbers_1 = numbers[:]
numbers_1.sort()

mid = len(numbers_1)//2
print("입력한 숫자: ", numbers)
print("입력한 숫자의 중앙값: ",numbers_1[mid])