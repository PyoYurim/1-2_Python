file = "c:/abc/abc.txt"
try:
    f = open(file, "r")
    f.close()
except:
    print("파일 경로가 이상해요:"+file)

try:
    mod = int(input("숫자:"))
    abc = 10 / mod
    kor = int("팔십")
except ZeroDivisionError:
    print("0넣지마")
except ValueError:
    print("정수형 문자열을 반드시 넣어주세요.")
except:
    print("뭘까?")