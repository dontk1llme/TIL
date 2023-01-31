# 1466. 데일리과제 8-2. 객체지향의 특성과 심화 사용 예제 1 Lv2
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectangle(Point):
    def __init__(self,po1,po2):
        self.po1 = po1
        self.po2 = po2  

    def get_area(self):
        return (self.po2.x-self.po1.x)*(self.po1.y-self.po2.y)
    
    def get_perimeter(self):
        return ((self.po2.x-self.po1.x)+(self.po1.y-self.po2.y))*2
    
    def is_square(self):
        if (self.po2.x-self.po1.x)==(self.po1.y-self.po2.y): return True
        else: return False

# 입력 예시
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

# 출력 예시
# 4
# 8
# True

# 9
# 12
# True