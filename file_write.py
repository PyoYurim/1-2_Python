file_full_name = "c:/myPython/test01.txt"

f = open(file_full_name, 'a') #열기

scores = {'math':90, 'kor':100, 'eng':40}

for key, value in scores.items():
    data = f"{key}:{value}\n"
    f.write(data)

f.close() #닫기