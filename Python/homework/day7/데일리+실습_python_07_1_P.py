# 1454. 데일리실습 7-1. OOP에 대한 개념 이해 예제 1 Lv1

class Nationality:
    def __init__(self, country) :
        self.country='나의 국적은 ' + country
        #init은 원래 return이 업슴


    def __str__(self): #얘를 몰라서 못했네...
        return self.country


korea_nationality = Nationality("대한민국")
print(korea_nationality) # 나의 국적은 대한민국 



