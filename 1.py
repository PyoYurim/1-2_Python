#number = input("주민등록번호 :")
#print(f"연월일 :{number[0:6]}")
#print(f"성별 : {number[7]}")

#fir = input("1st :")
#sec = input("2nd :")
#thi = input("3rd :")
#
#fir1 = int(fir)
#sec1 = int(sec)
#thi1 = int(thi)
#
#avg = (fir1 + sec1 + thi1) / 3
#
#print(f"{fir},{sec},{thi}의 평균은 {avg:.2f}입니다.")

put = int(input("투입한 돈:"))
pri = int(input("물건의 가격:"))
cha = put - pri
print(f"거스름돈: {cha}")
print(f"500 동전 개수 : {cha // 500}")
print(f"100 동전 개수 : {cha % 500 // 100}")

