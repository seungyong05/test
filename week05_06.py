#week05_06.py
while  True:
    name = input("이름: ").strip().lower()
    if name == "an":
        break
    elif name == "안":
        continue
     else:
         print (name)
