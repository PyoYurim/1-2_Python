import os

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
            score = {} #비어있는 딕셔너리
            score['name'] = datas[0]
            score['kor'] = int(datas[1]) #정수형으로 바꿔줌~
            score['eng'] = int(datas[2])
            score['mat'] = int(datas[3])

            scores.append(score)


    f.close()

    for s in scores:
        avg = sum([s['kor'], s['eng'], s['mat']]) / 3
        line = f"이름:{s['name']} 국어:{s['kor']} 영어:{s['eng']}"\
               f" 수학:{s['mat']} 평균:{avg:0.2f}" #문자열로 표현
        print(line)