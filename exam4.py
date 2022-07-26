import datetime

cur_year = datetime.datetime.today().year
cur_month = datetime.datetime.today().month

socnum = input("주민등록번호:")
ymd = socnum[:6]
y = int(socnum[:2])
g = int(socnum[7])

if g <=2:
    y += 1900
else:
    y += 2000

age = (cur_year - y) + 1
print("너의 나이는..." + str(age)) #이거 뭐야?


