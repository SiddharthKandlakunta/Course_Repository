#inherit is pretty self explanatory, one class can inherit attibutes and methods from an already existing class
#Class which inherits is called called a derived class or child class or sub class
#The class from which we inherit is called base class, parent class or super class
#Sntax: class DerivedClassName(BaseClassName):
#               #statements

class Father:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def is_male(self):
        return True
    def job(self):
        print('Yes, I work')
    def eat(self):
        print('Yes, I can eat')
    def printname(self):
        print(self.firstname, self.lastname)



class Son(Father):
    def __init__(self, firstname,lastname,age):
        super().__init__(firstname,lastname)
        self.age = age


    def job(self):
        super().job()
        print('on my student projects')
#class Son(Father):
    def print_age(self):
         print(f'My age is {self.age}')
    #you can also method override by calling the same inherited method also can use super keyword
    # def job(self):
    #     super().job()
    #     print('on my student projects')
# son_1 = Son()
# son_1.job()

father_1 = Father('John','Doe')
father_1.printname()
son_1 = Son('John','Junior',25)
son_1.printname()
son_1.print_age()