class Person:
  def __init__(self, name, lastName, age) -> None:
      self.name, self.lastName, self.age = name, lastName, age

  def showName(self):
    print("hello", self.name, self.lastName)


p1 = Person("hamza", "choki", 26)

print(p1.age, p1.lastName, p1.name)
p1.showName()
