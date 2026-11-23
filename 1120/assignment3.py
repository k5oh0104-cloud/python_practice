#1
num1 = input('첫번째 숫자를 입력하시오: ')
num2 = input('두번째 숫자를 입력하시오: ')
num1 = float(num1)
num2 = float(num2)
oper = input('연산자를 입력하시오: ')
case = [num1, num2, oper]
example = ['-', '+', '*', '/']
if type(num1) == float and type(num2) == float and oper in example:
    match case:
        case [num1, num2, '-']:
            print(num1-num2)
        case [num1, num2, '+']:
            print(num1+num2)
        case [num1, num2, '*']:
            print(num1*num2)
        case [num1, num2, '/']:
            if num2 != 0.0:
                print(num1/num2)
            else:
                print("Can't divide by zero")
else:
    print("error")