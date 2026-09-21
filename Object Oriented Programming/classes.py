class ClassExample:
    pass
object_1 = ClassExample()
print(type(ClassExample))
object_1.name = 'John Doe'
object_1.address = 'California'
print(object_1.name)
object_2 = ClassExample()
object_2.name = 'Jane Doe'
object_2.address = 'Dallas'
print(object_2.name)


######### Adding Attributes to Your Class #############

# class Details:
#     #kids = 0 #class object variable
#     def __init__(self,your_name,your_address):#this is a constructor
#         self.name = your_name
#         self.address = your_address
#         #self.kids = 0

# person_1 = Details('John Doe', 'California')
# person_2 = Details('Jane Doe', 'Dallas')
# print(person_1.name, person_1.address)
# print(person_2.name, person_2.address)
# print(person_1.kids)

######### Adding Methods to your Class ##############

class Details:
    kids = 0 #class object variable
    def __init__(self,your_name,your_address):#this is a constructor
        self.name = your_name
        self.address = your_address
    def display(self):#(self,age)
        print('hi')
        #print(f'my name is {self.name} and my address is {self.address}')
        #print(f'my age is {age}')
    def update_kids(self):
        self.kids +=1

person_1 = Details('John Doe', 'California')
person_2 = Details('Jane Doe', 'Dallas')
person_1.display()#(29)
person_1.update_kids()
print(person_1.kids)
#print(person_2.kids)
