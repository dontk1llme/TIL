# 1220. [S/W 문제해결 기본] 5일차 - Magnetic D3
# pointer -> 양쪽 끝이 자석이랑 다르면 삭제하기
# 사진에 낚이지 않기. 꼭 공중에 떠 있지 않아도 됨. 안에 잇는 애들끼리는 지장없음
# 몇개인지 안중요하니까 그냥 1,2 나오는 순간들만 세면 되는 거네...

T = 10
for tc in range(1, T+1):
    # input
    num = int(input())
    table = [list(map(int, input().split())) for _ in range(num)] # 1:N, 2:S
    # to be easy to compare garo<->sero
    table = list(zip(*table)) #left: N(1), right=S(2)

    #check
    count = 0
    for i in range(len(table)):
        isN = False #N
        for j in range(len(table)):
            if table[i][j]==1:
                isN = True
            elif table[i][j]==2:
                if isN:
                    count+=1
                    isN=False

    print(f'#{tc} {count}')








