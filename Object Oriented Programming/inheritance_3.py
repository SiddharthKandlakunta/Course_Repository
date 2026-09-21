#Single Inheritance
class Animal:
    def eat(self):
        print('Animal is eating')

class Dog(Animal):
    def bark(self):
        print('Dog is barking')

dog = Dog()
dog.eat()
dog.bark()

#Multiple Inheritance

class Camera:
    def take_photo(self):
        print('Taking Photo')

class Phone:
    def make_call(self):
        print('Making Call')

class SmartPhone(Camera,Phone):
    def browse_internet(self):
        print('Browsing Internet')

phone = SmartPhone()
phone.take_photo()
phone.make_call()
phone.browse_internet()

#MultiLevel Inheritance
class Animal:
    def eat(self):
        print('Animal is eating')

class Dog(Animal):
    def bark(self):
        print('Dog is barking')

class Puppy(Dog):
    def play(self):
        print('Playing')

p = Puppy()
p.eat()
p.bark()
p.play()

#Hierarchical Inheritance
class Animal:
    def eat(self):
        print('Animal is eating')

class Dog(Animal):
    def bark(self):
        print('Dog is barking')

class Cat(Animal):
    def meow(self):
        print('Cat is meowing')

d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.meow()

#Hybrid Inheritance
class A:
    def show(self):
        print('A')

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

obj = D()
obj.show()

#Method Resolution Order
#MRO determines the order in which Python searches classes for a method or attribute.
class A:
    def show(self):
        print('A')

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

print(D.mro())
print(D.__mro__)#C3 linerization algorithm

#Super Function

class Parent:
    def show(self):
        print('Parent Show')

class Child(Parent):
    def show(self):
        super().show()
        print('Child Show')

c = Child()
print(Child.mro())
c.show()

#inheritance with constructors

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name,course):
        super().__init__(name)
        self.course = course

s = Student('Sid','AI/ML')
print(s.name)
print(s.course)

#isinstance(), issubclass()

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print(issubclass(Dog,Animal))