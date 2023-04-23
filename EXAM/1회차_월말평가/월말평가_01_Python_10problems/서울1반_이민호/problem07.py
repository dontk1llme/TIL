# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    if len(numbers) == 1 :
        r = numbers[0]
        return r * r * 3.14
    if len(numbers) == 2 :
        a, b = numbers
        if (a + b) % 2 == 1 :
            return a * b * 0.5
        else :
            return a * b
    if len(numbers) >= 3 :
        return (sum(numbers), sum(numbers)/len(numbers))
    if not numbers :
        return 0
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0