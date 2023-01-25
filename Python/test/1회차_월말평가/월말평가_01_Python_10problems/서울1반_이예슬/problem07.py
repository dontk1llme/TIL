# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    n = len(numbers) #입력값의 개수
    if n==0: return 0
    elif n==1: #입력값=반지름 길이. return 원 넓이
        return numbers[0]*numbers[0]*3.14
    elif n==2: #합이 홀수면 삼각형 넓이 계산, 짝수면 사각형 넓이 계산
        if sum(numbers)%2==1:
            return numbers[0]*numbers[1]/2
        else: return numbers[0]*numbers[1]
    elif n>=3: #(합, 평균)
        hap=0
        for i in numbers:
            hap+=i
        avg=hap/n
        return (hap, avg)
    


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0