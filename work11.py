fav_fruits = {
    '김인하' : ['딸기', '오렌지'],
    '이물류' : ['귤', '무화과'],
    '최컴정' : ['복숭아','귤', '배'],
    '박정석' : ['키위','자두']
}

for name, fruits in fav_fruits.items():
    print(f"{name}이 좋아하는 과일 >>")
    for fruit in fruits:
        print(f"\t{fruit}")






bibimbap = {
    '양념' : '고추장',
    '고명' : ['버섯', '계란', '콩나물', '시금치', '육회']
}

print(f"당신이 주문한 비빔밥의 양념은 {bibimbap['양념']}이고, 고명은", end = "")
print(",".join(bibimbap['고명']), end="입니다. \n")


