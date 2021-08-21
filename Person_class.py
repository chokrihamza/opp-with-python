class Person:
    def __init__(self, name, lastName, age) -> None:
        self.name, self.lastName, self.age = name, lastName, age

    def showName(self):
        print("hello", self.name, self.lastName)


p1 = Person("jhon", "doe", 15)

print(p1.age, p1.lastName, p1.name)
p1.showName()

# del p1.age
#print(p1.age) if u run the code there is an error
#del p1
#print(p1)
