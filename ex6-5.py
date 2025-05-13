class Person:
  def __init__(self, fuame, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
    
  def __str__(self):
    return f"my first name is {self.firstname} , my last name  is {self.lastname}"
    
class Student(Person):
  pass
  
x = Student("mike", "Olsen")
print(x)
#print(x.firstname)
#print(x.lastname)
x.printname()
