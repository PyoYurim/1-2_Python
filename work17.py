favorite_books = {
    '80일간의 세계일주' : {'feature1':'삼성출판사 편집부','feature2':'삼성출판사','feature3':'2017년'},
    '흐르는 편지' : {'feature1':'김숨','feature2':'현대문학','feature3':'2018년'},
    '인간 없는 세상' : {'feature1':'앨런 와이즈먼','feature2':'랜덤하우스코리아','feature3':'2007년'}
                  }
for name, info in favorite_books.items() :

    print(f"제가 좋아하는 책은 {name}입니다.")
    print(f"이 책의 작가는 {info['feature1']}입니다.")
    print(f"이 책의 출판사는 {info['feature2']}입니다.")
    print(f"이 책의 출판년도는 {info['feature3']}입니다.")
    print(f"")