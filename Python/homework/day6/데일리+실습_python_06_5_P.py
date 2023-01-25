# 1451. 데일리실습 6-5. 크롤링을 통한 서비스 개발 예제5

#반복문 활용
def sum_of_digit(num):
    num=str(num)
    sum=0
    for i in range(len(num)):
        sum += int(num[i])
    return sum

print(sum_of_digit(3904)) # 16

#반복문 활용하지 않음 -> 재귀
def sum_of_digit_2(num):
    if num<10: return num
    return sum_of_digit_2(num//10)+(num%10)
    

print(sum_of_digit_2(3904))