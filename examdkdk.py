class Contact:
    def _init__(self, name, phone="", addr=""):
        self.name = name
        self.phone = phone
        self.address = addr

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.address}"

contact_list = []
contact1 = Contact("김미영", "000-0000-0000", "인천광역시 연수구")
contact2 = Contact("이미영")
contact4 = Contact(naem="박미영", addr="인천광역시 미추홀구")
contact_list.append(contact1)
contact_list.append(contact2)
contact_list.append(contact4)

for c in contact_list:
    #printf(f"{c.name} | {c.phone} | {c.address}")
    print(c)