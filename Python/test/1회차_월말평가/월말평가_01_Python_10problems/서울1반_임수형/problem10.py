# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    # 여기에 코드를 작성하여 함수를 완성합니다.
    '''
    방향 M에 따라 position 튜플은 인덱싱하여 1을 더해주고,
    변화 후의 위치가 0 ~ N-1 안에 있는지 확인한다.
    bool 값 is_safe의 값을 반환한다.
    '''

    if M == 0:
        if position[0] - 1 < 0:
            is_safe = False
        else:
            is_safe = True
    elif M == 1:
        if position[0] + 1 > N - 1:
            is_safe = False
        else:
            is_safe = True
    elif M == 2:
        if position[1] - 1 < 0:
            is_safe = False
        else:
            is_safe = True
    else:
        if position[1] + 1 > N - 1:
            is_safe = False
        else:
            is_safe = True

    return is_safe
    

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
    
