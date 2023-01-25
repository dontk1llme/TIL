# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calc_lunch_cost(lunch_cost):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    '''
    딕셔너리에서 value만 리스트로 만들고 sum() 메소드를 통해 합을 구해보자
    '''
    lunch_l = list(lunch_cost.values())
    s = sum(lunch_l)
    return s


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    lunch_cost = {
        '이싸피' : 12000,
        '김싸피' : 30000,
        '박싸피' : 10000,
        '최싸피' : 15000,
        '조싸피' : 18000, 
    }

    print(calc_lunch_cost(lunch_cost))  # 85000