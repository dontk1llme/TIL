# 1220. [S/W 문제해결 기본] 5일차 - Magnetic D3
T = 10
for tc in range(1, T + 1):
    # input
    num = int(input())
    table = [list(map(int, input().split())) for _ in range(num)]  # 1:N, 2:S
    # to be easy to compare garo<->sero
    table = list(zip(*table))  # left: N(1), right=S(2)

    # check
    count = 0
    for i in range(len(table)):
        isN = False  # N
        for j in range(len(table)):
            if table[i][j] == 1:
                isN = True
            elif table[i][j] == 2:
                if isN:
                    count += 1
                    isN = False

    print(f'#{tc} {count}')