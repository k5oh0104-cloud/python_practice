#1
balance = input("현재 잔액: ")
withdrawal = input("출금액을 입력해주세요: ")

if withdrawal < 1000 or withdrawal > 10000:
    print("출금 실패, 1000원 이상, 10000원 미만으로 입력해주세요.")
elif balance < withdrawal:
    print("출금 실패, 잔액이 없습니다.")
elif str(withdrawal)[-3:] != "000":
    print("출금 실패, 1000원 단위로 출금해주세요.")
else:
    balance = balance - withdrawal
    print(f'출금성공!, 잔액은 {balance}입니다.')