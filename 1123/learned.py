a = int(input("국어점수를 입력하세요: "))
b = int(input("영어점수를 입력하세요: "))

match a, b:
  case (x,y) if x >= 90 and y >= 90:
    print("excellent")
  case (x,y) if x >= 90 or y >= 90:
    print("good")
  case _:
    print("bad")


print('changes')
