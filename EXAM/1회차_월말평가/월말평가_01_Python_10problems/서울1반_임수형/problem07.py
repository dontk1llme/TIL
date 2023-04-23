# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    '''
    초기 numbers 튜플의 길이를 변수 l에 저장하고 if, elif로 조건을 나눈다.
    제곱은, pow를 활용한다.
    주어진 조건에 맞는 계산기를 만들어 보자.
    '''
    pi = 3.14
    l = len(numbers)

    if l == 0:
        return 0

    elif l == 1:
        return pow(int(numbers[0]) ,2) * pi
    
    elif l == 2:
        a, b = numbers
        if (a + b) % 2 == 1:
            return a * b / 2
        else:
            return a * b
    
    else:
        li = list(numbers)
        s = sum(li)
        return (s, s/l)


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0