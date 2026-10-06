#what is abstraction?
#print("Hello World")
#What to do, not how it is done
#abc module - Abstract Base Class

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print('bark')

class Cat(Animal):
    def sound(self):
        print('meow')

dog_1 = Dog()
dog_1.sound()

cat_1 = Cat()
cat_1.sound()

#### Classes that inherit an abstract Class needs to be instantiated with the abstract method, if not they will throw an error##

#normal method and abstract method
#normal methods dont need overriding to work
#abstract methods need overriding to work
#normal methods can include complete implementation.
#abstract method delclares the required operation without providing implementation.

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass

class UPI(Payment):

    def pay(self, amount):
        print(f'Paid Rs.{amount} using UPI')

class Card(Payment):

    def pay(self, amount):
            print(f'Paid Rs.{amount} using Card')

class Cash(Payment):

    def pay(self, amount):
            print(f'Paid Rs.{amount} using Cash')

upi = UPI()
upi.pay(1000)

credit_card = Card()
credit_card.pay(15000)

cash = Cash()
cash.pay(5000)

#Shape - Circle, Rectangle and Triangle

import math

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return round(math.pi* self.radius**2,2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

c = Circle(5)
print(c.area())
r = Rectangle(10, 5)
print(r.area())
t = Triangle(10,4)
print(t.area())




