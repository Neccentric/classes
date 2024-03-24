# Intro to OOP.
    # Functional programming and Object-Oriented Programming.
# Different styles of coding are also known as "Paradigms". A common style is called Functional programming or FP for short.

def getTotal(a, b):
    return a + b
num1 = 2
num2 = 3
total = getTotal(num1, num2)
print(total)

# In the FP style, we keep data and functionality separate. We pass data into functions whenever we want something.

def getDistance(mph, h):
    return mph * h
mph = 60
h = 2
distance = getDistance(mph, h)
# In fp, functions return new values and then use those values somewhere else in the code.
print(distance)

# In OOP, we group data and functionality as properties and methods inside objects.

class Virtual_Pet:
    def __init__(self, color, name) -> None:
        self.color = color
        self.name = name

rocky = Virtual_Pet("brown", "rocky")
print(rocky.color)
print(rocky.name)    

# OOP is useful for modeling objects, real-life or not. Objects have properties and methods that we treat as one thing.

class Car:
    mileage = 12000

    def drive(self, miles):
        self.mileage += miles

tesla = Car()
tesla.drive(100)
print(tesla.mileage)
# In OOP, we use methods to update existing values of an object, like here where we use eat() to update the value of hungry.
class Dog:
    hungry = True 

    def eat (self):
        self.hungry = False
        return 
dog = Dog()
dog.eat()
print(dog.hungry)

class Piggy:
    value = 0
    def addMoney(self, amount):
        self.value = self.value + amount

myPiggy = Piggy()
myPiggy.addMOney(100)
print(myPiggy.value)