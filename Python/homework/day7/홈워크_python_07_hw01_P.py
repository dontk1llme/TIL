# 1459. 데일리과제 7-2. 객체지향 프로그래밍의 이해와 기본

class Doggy:

    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, jong):
        self.name = name
        self.jong = jong
        # self.num_of_dogs+=1
        # self.birth_of_dogs+=1 이거아닙니다
        Doggy.num_of_dogs+=1
        Doggy.birth_of_dogs+=1
    
    def __del__(self):
        Doggy.num_of_dogs-=1

    def bark(self):
        print('왕왕왕왕왕왕')

    def get_status(self):
        print(f'bod: {self.birth_of_dogs}, nod: {self.num_of_dogs}')


dog1=Doggy('미애', '아기곰')
dog1.get_status()
dog1.bark()

dog2 = Doggy('잭슨' , '고양이')
dog2.get_status()

del dog2
dog1.get_status()