#4자리의 정수를 받는다.
#문자열 -> 정수..
#4번, 3번, 2번, 1번 각 자리별 숫자를 뽑는다.
#//, %
#각 자리의 수의 합을 계산하거
#출력한다

number = int(input("4자리의 정수 입력:"))
#"1234" => 1234
# 1 + 2 + 3 + 4 = 10

n4 = number // 1000 # 1234//1000 = 1
number = number % 1000 # 1234 % 1000 = 234

n3 = number // 100  # 234 // 100 = 2
number = number % 100  # 234 % 100 = 34

n2 = number // 10    # 34 // 10 = 3
number = number % 10  # 34 % 10 = 4

n1 = number // 1  # 4 // 1 = 4
number = number % 1  # 4 % 1 = 0

result = n4 + n3 + n2 + n1

print(result)