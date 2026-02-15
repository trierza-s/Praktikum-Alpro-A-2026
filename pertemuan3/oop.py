# Buat tiga objek dari kelas MyClass:
class MyClass:
  x = 5

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

# Metode __init__()
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)

# Self parameter
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()


# Python Properti
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)

# Class Metode
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())

