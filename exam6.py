contacts = {}

def search(name):
    #phone = contacts[name]
    phone = contacts.get(name)
    return phone

def addition():
    while True:
        name = input("이름:").strip()

        if not name:
            break

        search = contacts.get(name)
        if not search:
            continue

        phone = input("연락처")
        contacts[name] = phone

    print("===연락처목록===")
    for name, phone in contacts.items():
        print(f"{name} : {phone}")


while True:
    print("=" * 20)
    print("[1] 추가")
    print("[2] 검색")
    print("[0] 종료")
    print("="* 20)

    sel_menu = input("선택:").strip()

    if sel_menu == "1":
        print("추가 기능 수행")
        addition()
    elif sel_menu == "2":
        print("검색 기능 수행")
        name = input("이름:").strip()
        phone = search(name)
        if phone:
            print(f"{name}:{phone}")
        else:
            print("없다")
    elif sel_menu == "0":
        print("\n\n프로그렘 종료")
        break