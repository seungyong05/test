#week05_03.py
socnum = input("주민등록번호")

a = "-" in socnum
gender = int(socnum[7]) % 2
    
b = "-" not in socnum
gender = int(socnum[7]) % 2

if gender == 0:
    msg = "여성"

else:
    msg = "남성"

print("성명 : [msg]")
