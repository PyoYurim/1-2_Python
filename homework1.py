people = {}
while True:
    sel = int(input("추가기능은 1이고 검색기능은 2이고 종료기능은 0입니다. 하나를 선택해주세요 :"))
    if sel == 1:
        while True:
            name = input("이름 : ")
            if not name:
                for name in people.keys():
                    print(f"=====연락처목록=====")
                    print(f"이름 : {name}")
                    print(f"연락처 : {people.get(name)}")
                break
            tel = input("연락처 : ")

            people[name] = tel

    elif sel == 2:
        name1 = input("검색할 이름을 입력하세요 : ")
        result = people.get(name1)
        if result == None:
            print("해당 이름의 연락처를 찾을 수 없습니다.")
        else:
            print(f"{name1}의 연락처 : {result}")

    elif sel == 0:
        print("프로그램을 종료합니다.")
        break













