import os
from score import Score

path_name = "c:/202144033"
full_filename = path_name + "/list.txt"

if os.path.isfile(full_filename):
    f = open(full_filename, "r")
    students = []

    while True:
        line = f.readline()
        if not line:
            break

        data = line.strip().split(',')
        if len(data) == 4:
            students.append(Score(data[0], data[1], data[2], data[3]))

    f.close()

    for i in students:
        print(i)