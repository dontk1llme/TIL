# 1458. 데일리실습 7-5. OOP의 메서드에 대한 이해와 사
import random

class ClassHelper:
    def __init__(self, list):
        self.list = list

    def pick(self, num):
        return random.sample(self.list, num)
    
    def match_pair(self):
        newarr=[]
        oldarr=self.list
        while len(oldarr)>3:
            ranarr = random.sample(self.list, 2)
            newarr.append(ranarr)
            for j in ranarr:
                if j in oldarr:
                    oldarr.remove(j)
        else: newarr.append(oldarr)
                
        return newarr


ch = ClassHelper(['김해피', '이해킹', '조민지', '박영수', '정민수'])

print(ch.pick(1))
print(ch.pick(1))
print(ch.pick(2))
print(ch.pick(3))
print(ch.pick(4))

print(ch.match_pair())
