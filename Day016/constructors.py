class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11
print(point.x)


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def talk(self):
        print(f"I am talking to {self.first_name} {self.last_name}")

person = Person("Henry", "Owade")
person.talk()

person2 = Person("Bob", "Smith")
person2.talk()

