class Person:
  def __init__(self, fname, lname) -> None:
    self.fname = fname
    self.lname = lname

  def printname(self):
    print(self.fname, self.lname)


person1 = Person('Jhon', 'Doe')
person1.printname()
