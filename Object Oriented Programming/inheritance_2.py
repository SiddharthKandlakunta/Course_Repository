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

class Mother:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
    def is_male(self):
            return False
    def job(self):
            print('Yes, I work')
    def eat(self):
        print('Yes, I can eat')
    def printname(self):
            print(self.firstname, self.lastname)

class Son(Father,Mother):
    def __init__(self, firstname, lastname,age):
        super().__init__(firstname, lastname)
        self.age = age
    def is_male(self):
        return True

son_1 = Son('John','Junior',25)
son_1.printname()
print(son_1.is_male())