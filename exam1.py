socnum = input("주민등록번호:")

#010202-1234567
ymd = socnum[0:6] #slicing
g=socnum[7]#indexing

data = socnum.split("-") #["010202", "123456"]
ymd1 = data[0]
g = data[1][0]

print("socnum:", id(socnum))
print("data:", id(data))
print("ymd1:", id(ymd))
print("ymd1:", id(ymd1))

