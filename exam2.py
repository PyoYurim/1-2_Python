#학생의 수를 입력받아, 그만큼의 학생이름과 성적을 받아, 딕셔너리 추가하고
#평균을 구하는

student = {}
count = int(input("학생 명수:"))
#sum = 0
for i in range(0, count):
    name = input("이름:")
    score = float(input("점수:"))
    students[name] = score
    #sum += score

    print(students)
    #avg = sum / count  으응? 이게 무슨 말이지?...함수랑 이름이 겹쳤다 어엉?...
    avg = sum(students.values()) / count
    print(f"평균:{avg:.2f}")
