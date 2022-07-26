shapes = int(input("원하는 도형을 선택하세요 (사각형(1), 삼각형(2), 원(3)) : "))
if shapes == 1 :
    a = float(input("가로 입력 : "))
    b = float(input("세로 입력 : "))
    c = a*b
    print(f"도형의 넓이 : {c:0.2f}")

elif shapes == 2 :
    a = float(input("밑변 입력 : "))
    b = float(input("높이 입력 : "))
    c = a*b/2
    print(f"도형의 넓이 : {c:0.2f}")

else :
    pi = 3.141592
    a = float(input("반지름 입력 : "))
    c = pi * (a**2)
    print(f"도형의 넓이 : {c:0.2f}")


