num= int(input("명수:"))
order=int(input("피자주문수량:"))
slice=int(input("조각:"))
result=(f"인당 {order*slice//num}조각이고, 남은 조각은 {order*slice%num}조각입니다.")
print(result)