# School -> project

# class -> Person , Student , Teacher , Administrator

# Person
#     name
#     age

# Student
#     name
#     age
#     sinf

# Teacher
#     name
#     age
#     subject

# Administrator
#     name
#     age
#     position


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, sinf):
        super().__init__(name, age)
        self.sinf = sinf


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


class Administrator(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position


student1 = Student("Botirjon", 12, "6-A")
student2 = Student("Islom", 15, "9-V")
student3 = Student("Abduazim", 14, "8-A")
student4 = Student("Lili", 17, "10-V")
student5 = Student("Merin", 17, "10-A")

teacher1 = Teacher("Gulnoza", 36, "Tarix")
teacher2 = Teacher("Navroz", 46, "Matematika")

admin1 = Administrator("Malohat", 30, "Direktor")
admin2 = Administrator("Fazlidin", 37, "Pisixolog")
admin3 = Administrator("Otabek", 37, "Zavuch")

persons = [student1, student2, student3, student4, student5,
           teacher1, teacher2,
           admin1, admin2, admin3]

while True:

    # Company
    text = """
    m -> Menegerlarni ko'rish
    r -> Reseptions ko'rish
    b -> Bugalteriya ko'rish
    a -> Axaranalar ko'rish
    f -> Filiallarni ko'rish
    d -> Dizaynerlar ko'rish
    e -> exit()
    >>>"""

    choice = input(text)

    if choice == 's':
        for i in persons:
            if isinstance(i, Student):
                print(i.name, i.age, i.sinf)
    elif choice == 't':
        for i in persons:
            if isinstance(i, Teacher):
                print(i.name, i.age, i.subject)
    elif choice == 'a':
        for i in persons:
            if isinstance(i, Administrator):
                print(i.name, i.age, i.position)
    elif choice == 'e':
        break
