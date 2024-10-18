#week03_01.py

#예시 1
target = int(input("아메리카노 금액 :"))
count = int(input("주문자 수 :"))
total = target * count
print("-" * 10)
print(" 총 금액 : ", total , "원")

#예시 2
target = input("아메리카노 금액")
count = input("주문자 수")
total = int(target) * int(count)
print("-" * 10)
print(" 총 금액 : " + str(total) + "원")

