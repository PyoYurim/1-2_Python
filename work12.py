students={
    '12210001':{'name' : '김인하', 'major' : '컴퓨터'},
    '12210011':{'name' : '김슈슉', 'major' : '전자'},
    '12210111':{'name' : '김슈욱', 'major' : '물류'},
}

for number, info in students.items() :
    print(f"학번:{number}")
    print(f"이름:{info['name']}")
    print(f"전공:{info['major']}")
    print()