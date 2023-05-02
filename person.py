class Person:
  # Constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self, prefix):
    print(f'{prefix}, {self.name}')
