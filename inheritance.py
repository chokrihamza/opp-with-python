class Person:
  def __init__(self, fname, lname) -> None:
    self.fname = fname
    self.lname = lname

  def __call__(self):
      print("Hi am the Person class")

  def printname(self):
    print(self.fname, self.lname)


person1 = Person('Jhon', 'Doe')
person1.printname()

# inherit from Person


class Student(Person):
  def __init__(self, fname, lname, age, type) -> None:
      #self.fname = fname
      #self.lname = lname
      #self.age = age
      #self.type = type
      # Note that in real world we can use super() to refer to the Parent class
      super().__init__(fname, lname)
      self.age = age
      self.type = type

  def __call__(self):
      print("Hi am the Student class inhert form Person")

  def printname(self):
    super().printname()
    print(f'your age is {self.age}, and you are  {self.type}')


student = Student('Alex', 'Smith', 20, 'first class')
student.printname()

person1()
student()
