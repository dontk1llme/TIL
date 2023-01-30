class Person:
    nowyear = 2023
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_age(self, year): #두가지 생성 어케함? ㅅ
        self.age = Person.nowyear - year
        return self.age
     
    def check_age(self):
        if self.age > 19: return True
        else: return False


#Driver's code
person1 = Person('Mark', 20)
person2 = Person.get_age('Rohan', 1992)

print(person1.name, person1.age) 
print(person2.name, person2.age)
print(person1.check_age())
print(person2.check_age())
