# week02_03.py
# print() 함수는 모든 타입의 데이터를 출력
# 출력 타입은 '문자열'

print("I", "AM", "A", "BOY.")
print("I", "AM", "A", "BOY.", sep="")
print("I", "AM", "A", "BOY.", sep=";")
print("I", "AM", "A", "BOY.", sep="|n")
print("=" * 10)
 
print("I")
print("AM")
print("A")
print("BOY.")

print("I", end="")
print("AM", end= "|n")
print("A", end= "--")
print("BOY.")
print("=" * 10)

print() #줄만 바뀜
print(int(1)) # int 생성자 호출
print(str("1")) # str 생성자 호출
print(float(1.1)) #float 생성자 호출
print(bool(True)) # bool 생성자 호출
print([1,2,3]) # 리스트 자료형 
print("123") # '123'
print("1" "2" "3") # '123'
print("1", "2", "3") # '1 2 3'
print("1" + "2" + "3") # '123'
