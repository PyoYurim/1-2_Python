score = int(input("점수를 입력하세요: "))
if score > 100:
    print(f"점수를 출력할 수 없습니다.")
elif score < 0:
    print(f"점수를 출력할 수 없습니다.")
elif score >= 90:
    print(f"A학점입니다.")
elif score >= 80:
    print(f"B학점입니다.")
elif score >= 70:
    print(f"C학점입니다.")
elif score >= 60:
    print(f"D학점입니다.")
elif score < 60:
    print(f"F학점입니다.")
