a = input("투입한 돈:")
b = input("물건의 가격:")
aa = int(a)
bb = int(b)
c = aa - bb
print(f"거스름 돈:{c}")
print(f"500 동전 개수:{c // 500}")
print(f"100 동전 개수:{c // 500 % 100}")
