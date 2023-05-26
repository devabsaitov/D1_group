class Dog:
    def make_sound(self):
        return "Vov-vov"

class Cat:
    def make_sound(self):
        return "Miyav-miyav"

class Hours:
    def make_sound(self):
        return "nimadir"

dog = Dog()
print(dog.make_sound())

cat = Cat()
print(cat.make_sound())

hours = Hours()
print(hours.make_sound())