import math


shape = int(input("도형 선택(1:사각형, 2:삼각형, 3:원): "))

if shape == 1:
    # 사각형의 넓이 계산
    width = float(input("가로 입력: "))  
    height = float(input("세로 입력: "))  
    area = width * height
    print(f"도형의 넓이: {area}")
    
elif shape == 2:
    
    base = float(input("밑변 입력: "))  
    height = float(input("높이 입력: "))  
    area = (base * height) / 2
    print(f"도형의 넓이: {area}")
    
elif shape == 3:
    
    radius = float(input("반지름 입력: ")) 
    area = math.pi * radius**2
    print(f"도형의 넓이: {area:.2f}")
    
else:
    print("잘못된 입력")
