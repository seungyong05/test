# week06_02.py
students = []
titles = ["국", "영", "수"]

#students = [[10,20,30],[1,2,3]]
#students = [[10,1],[20,2],[30,3]] #따로 꼭 볼 것

number = int(input("인원:"))
for n in range(number):
    print(f"{n+1} 학생>>")
    scores = []
    for t in titles:
        # students.append(float(input(f"{t} 과목:")))
        score = float(input(f"{t} 과목:"))
        scores.append(score)
    students.append(scores)

for value in enumerate(students):
    print(value)
    print(value[0], value[1])

a, b = (1, 2)
print(a, b)

for i, e in enumerate(students):
    print(i, e)

for i, e in enumerate(students):
    print(f"{i+1}:")
    for j, s in enumerate(e):
        print(f"{titles[j]}:{s}")







    
