import random


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


l = []
players = [
    {
        "name": "MuhammadAmin",
        "score": 0
    },
    {
        "name": "NurMuhammad",
        "score": 0
    }]
for player in players:
    obj = Player(name=player['name'], score=player['score'])
    l.append(obj)


class Issue:
    def init(self, easy=False, medium=False, hard=False):
        self.easy = easy
        self.medium = medium
        self.hard = hard

    def random_issue(self):
        misol = ""
        if self.easy == True:
            for i in range(2):
                misol += str(random.randrange(1, 100))
                amal = random.choice(["-", '+', "*"])
                if not i == 1:
                    misol += amal
        elif self.medium == True:
            for i in range(4):
                misol += str(random.randrange(1, 100))
                amal = random.choice(["-", '+', "*"])
                if not i == 3:
                    misol += amal
        elif self.hard == True:
            for i in range(6):
                misol += str(random.randrange(1, 100))
                amal = random.choice(["-", '+', "*"])
                if not i == 5:
                    misol += amal
        return misol


while True:
    print("Level:")
    print("1)Easy")
    print("2)Medium")
    print("3)Hard")
    print("4)exit")
    choice = input("Enter your level ! : ")
    if choice == "1":
        count = int(input("Enter your count issue: ")) * len(l)

        for i in range(count):
            if i % 2 == 0:
                session = 0
            else:
                session = 1
            print("Player -> " + l[session].name)
            issue = Issue(easy=True).random_issue()
            answer = int(input(f"{issue}="))
            if answer == eval(issue):
                print("Correct answer ! ✅")
                l[session].score += 1
            else:
                print(f"Incorrect answer ❌ Right: {eval(issue)}")
                l[session].score -= 1

        for i in l:
            print(f"{i.name} -> {i.score} ", end=' | ')
        choice = input("Continue ? Y/n : ")
        if choice == "n":
            break
    elif choice == "2":
        count = int(input("Enter your count issue: ")) * len(l)

        for i in range(count):
            if i % 2 == 0:
                session = 0
            else:
                session = 1
            print("Player -> " + l[session].name)
            issue = Issue(medium=True).random_issue()
            answer = int(input(f"{issue}="))
            if answer == eval(issue):
                print("Correct answer ! ✅")
                l[session].score += 1
            else:
                print(f"Incorrect answer ❌ Right: {eval(issue)}")
                l[session].score -= 1

        for i in l:
            print(f"{i.name} -> {i.score} ", end=' | ')
        choice = input("Continue ? Y/n : ")
        if choice == "n":
            break

    elif choice == "3":
        count = int(input("Enter your count issue: ")) * len(l)

        for i in range(count):
            if i % 2 == 0:
                session = 0
            else:
                session = 1
            print("Player -> " + l[session].name)
            issue = Issue(hard=True).random_issue()
            answer = int(input(f"{issue}="))
            if answer == eval(issue):
                print("Correct answer ! ✅")
                l[session].score += 1
            else:
                print(f"Incorrect answer ❌ Right: {eval(issue)}")
                l[session].score -= 1

        for i in l:
            print(f"{i.name} -> {i.score} ", end=' | ')
        choice = input("Continue ? Y/n : ")
        if choice == "n":
            break
    elif choice == "4":
        print("Goodbye!")
        break
