# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    position=list(position)
    if M==0:position[0]-=1
    elif M==1: position[0]+=1
    elif M==2: position[1]-=1
    elif M==3: position[2]+=1

    torf=True
    if position[0]>=0 and position[0]<N and position[1]>=0 and position[1]<N: 
        torf=True
    else: 
        torf=False
    return torf


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
