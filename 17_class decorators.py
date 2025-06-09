def add_greeting(cls):
     def greet(self):
         return"Hello from Decorator!"
     
     cls.greet = greet
     return cls

@add_greeting

class Person:
     def __init__(self, name):
         self.name = name
         
     def introduce(self):
         print(f"Hi, I'm {self.name}")

p = Person("John")
print(p.greet())