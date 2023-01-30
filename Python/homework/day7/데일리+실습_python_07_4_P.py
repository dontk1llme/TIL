# 1457. 데일리실습 7-4. OOP의 메서드에 대한 이해와 사용

def fee(num1, num2): # num1: 대여시간, num2: 주행거리
    total=0

    #대여요금
    dyyg = num1/10 * 1200

    #보험료
    if num1%30==0: 
        ins = (num1//30)*525
    else: ins = (num1//30+1)*525

    #주행요금
    if num2>100: 
        run = 170*100+85*(num2-100)
    else: run = 170*num2

    total = dyyg + ins + run

    return print(total)

    

fee(600, 50) #=> 91000 


fee(600, 110) #=> 100350
