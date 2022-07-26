students = {}
for i in range(5) :
    name = input("이름 : ")
    score = float(input('점수 :'))
    students[name] = score

for v in students.values() :
    i += v

avg = i / len(students.values())
print(f"평균: {avg}")


