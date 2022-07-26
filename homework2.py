import os

path_name = "c:/202144033"
full_filename = path_name + "/list.txt"

if os.path.isfile(full_filename): #꼭 파일이 있나 확인해야함
    f = open(full_filename, 'r')

score = []

while True:
    line = f.readline()
    if not line:
        break

    data =line.strip().split(',')

    if len(data) == 4:
        avg = (int(data[1]) + int(data[2]) + int(data[3])) / 3
        scores = {'name':data[0], 'kor':data[1], 'eng':data[2], 'mat':data[3], 'avg':avg}
        score.append(scores)

f.close()

for index in range(len(score)):
    print(f"이름:{score[index]['name']} 국어:{score[index]['kor']}"
          f"영어:{score[index]['eng']} 수학:{score[index]['mat']}" 
          f"평균:{score[index]['avg']}")



