#1456. 데일리실습 7-3. OOP에 대한 개념 이해 예제 3 Lv3

class Calculator:
    def __init__(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(self.num1+self.num2)

    def substract(self):
        print(self.num1-self.num2)

    def multiply(self):
        print(self.num1*self.num2)

    def divide(self):
        if self.num2==0: 
            print('0으로 나눌 수 없습니다')
        else:
            print(self.num1/self.num2)
            



c1 =Calculator(1,2)# 1 + 2
c1.add()

c2 = Calculator(2,1)# 2 – 1
c2.substract()

c3 = Calculator(3,4)# 3 * 4
c3.multiply()

c4 = Calculator(4,0)# 4 / 0
c4.divide()