#week05_02.py
toeic = int(input("Toeic:"))
age = int(input("AGE:"))
grade = int(input("GRADE:"))
temp = int(input("EMPERATURE:"))
height = int(input("HEIGHT:"))
socnum = int(input("SOC NUMBER:"))

a = toeic >= 800 and age < 30
b = toeic >= 800 or age < 30
d = temp < 10 or temp > 28

c = not (age = 30) and toeic < 600

e = height >= 120 and height <=160

print(a, b,c, d,e)

cars = ["audi","tesla","안승용","kia","안승용2","hyundai"]
car = "kia"
print(car in cars)
print(car not in cars)
print(car.lower() in cars)
print(car.lower() not in cars)
print("*" * 30)


