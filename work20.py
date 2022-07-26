import random
number = random.randint(1, 100)
tries = 0

print("+++숫자를 맞쳐보세요.(1~100)+++")

for _ in range(10):
    guess = int(input("입력: "))
    tries += 1
    if number == guess:
        print(f"{number}가 정답입니다. 도전 횟수는 {tries}회 입니다.")
        break
    elif number < guess:
        print("숫자가 작습니다.")
    elif number > guess:
        print("숫자가 큽니다.")

    if tries > 10:
        print("주어진 기회를 모두 사용하였습니다.")
