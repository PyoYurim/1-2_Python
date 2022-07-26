sem1=float(input("1학기 학점:"))
sem2=float(input("2학기 학점:"))
time=int(input("봉사시간:"))

if (sem1+sem2)/2>=3.5 and time>=8:
    print("장학금 대상자 입니다.")
else:
    print("장학금 대상자가 아닙니다.")
