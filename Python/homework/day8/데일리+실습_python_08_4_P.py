# 1464. 데일리실습 8-4. OOP의 다중 상속 예제 1 Lv4

class PublicTransport:
    nowpassengers= 0
    totalpassengers=0
    
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare
    
    def get_in(self, num):
        PublicTransport.nowpassengers+=num
        PublicTransport.totalpassengers+=num
    
    def get_off(self, num):
        PublicTransport.nowpassengers-=num
    
    def profit(self):
        return PublicTransport.totalpassengers*self.fare
    

class Bus(PublicTransport):
    def get_in(self, num):
        super().get_in(num)
        max = 30
        if PublicTransport.nowpassengers > 30: 
            print('더이상 탑승할 수 업슴니다')
            del self
        else: print('ㅇㅇ 타')

b = Bus ('1차', 1000)
b.get_in(10)
b.get_in(50)
print(b.nowpassengers)
