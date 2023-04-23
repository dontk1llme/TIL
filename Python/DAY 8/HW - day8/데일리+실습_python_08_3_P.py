# 1463. 데일리실습 8-3. OOP의 상속과 오버라이딩 예제 3 Lv3

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
    

        
        