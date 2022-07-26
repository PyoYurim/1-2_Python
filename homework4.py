import os
from score import Score

path_name = "c:/202144033"
full_filename = path_name + "/list.txt"

scores = []

if not os.path.isdir(path_name):
  os.makedirs(path_name)

elif os.path.isfile(full_filename):
  f = open(full_filename, "r")
  students = []

  while True:
      line = f.readline()
      if not line:
          break

      data = line.strip().split(',')
      if len(data) == 4:
          a = Score(data[0], data[1], data[2], data[3])
          a_1 = (Score.file_contant(a)).replace(" ","").replace("\n","")
          scores.append(a_1)
  f.close()
  print(f"기존 등록되어 있는 학생은 {len(scores)}명 입니다.")

while True:
  print("1. 입력")
  print("2. 검색하기")
  print("3. 전체출력하기")
  print("4. 파일에서 다시 읽어오기")
  print("0. 종료")

  menu = input(">").strip()

  if menu == "1":
      f = open(full_filename, "a")
      while True:
          print("이름, 국어점수, 영어점수, 수학점수를 입력하세요.")
            name = input("이름을 넣어주세요(종료시: 바로 엔터) : ").strip()
            if name == "":
                break

            kor = int(input("국어점수:"))

            eng = int(input("영어점수:"))

            mat = int(input("수학점수:"))

            b = Score(name, kor, eng, mat)
            b_1 = (Score.file_contant(b)).replace(" ", "").replace("\n", "")
            scores.append(b_1)

        f.write(Score.file_contant(b))
    f.close()

elif menu == "2":
        global s_1
        while True:

            print("원하는 이름으로 검색하세요.(빈 칸이면 종료)")

            in_name = input("이름:").strip()
            if in_name == "":
                break
            test_name = ' '.join(scores)

            if in_name in test_name:
                for i in range(len(scores)):
                    if in_name in scores[i]:
                    word = scores[i]
                    word_li = word.replace(" ", "").split(',')
                    c = Score(word_li[0], word_li[1], word_li[2], word_li[3])
                    print(Score.__str__(c))
            else:
                print(f"{in_name}의 정보가 없습니다.")

    elif menu == "3":
            print(f"현재 등록되어 있는 {len(scores)}명의 학생의 정보입니다.")
            for i in scores:
                student = i
                student_li = student.replace(" ", "").split(',')
                d = Score(student_li[0], student_li[1], student_li[2], student_li[3])
                print(Score.__str__(d))

    elif menu == "4":
        print("현재 이 기능은 구현되지 않습니다, 죄송합니다.")

    elif menu == "0":
        break
