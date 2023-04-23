# 1462. 데일리실습 8-2. OOP의 상속과 오버라이딩 예제 2 Lv2
class Person:
    nowyear = 2023

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_age(name, year): 
        #두가지 생성이 아니라 새로운 person 객체를 반환하는 어이없는 예제
        age = Person.nowyear - year
        return Person(name,age)
     
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
