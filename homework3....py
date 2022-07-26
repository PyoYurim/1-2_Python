import os
from score import Score

path_name = "c:/202144033"
full_filename = path_name + "/list.txt"''
scores = []

if not os.path.isfile(full_filename):
    print("파일이 없습니다. homework1.py를 실행하세요.")
else:
    f = open(full_filename, 'r')

    while True:
        line = f.readline()
        if not line:
            break

        datas = line.split(',')
        if len(datas) == 4:

            n = datas[0]
            try:
                k = int(datas[1])
                e = int(datas[2])
                m = int(datas[3])

                score = Score(n, k, e, m)
                scores.append(score)
            except:
                print("잘못된정보:"+line)
                continue


    f.close()

    for s in scores:
        print(s)
