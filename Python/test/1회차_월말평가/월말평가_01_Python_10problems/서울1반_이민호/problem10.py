# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    x, y = position
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    nx, ny = x + move[M][0], y + move[M][1]
    if 0 <= nx < N and 0 <= ny < N :
        return True
    else :
        return False
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
