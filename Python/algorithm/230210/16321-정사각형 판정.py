# 13732. 정사각형 판정 D3
# 연결되어 있고 / 가로세로 개수가 같은지. / #이 1개이면

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    ans='no'
    lst = [list(map(str, input())) for _ in range(n)]
    idx1, idx2 = [], []
    for i in range(n):
        for j in range(n):
            if lst[i][j] == '#':
                idx1.append([i, j])
                idx2.append([j, i])
    idx2.sort() #이거안하면안댐
    if idx1 == idx2 and len(idx1) == (idx1[-1][0] - idx1[0][0] + 1) ** 2: #제곱.......
        ans = 'yes'
    if lst==['#']:
        ans='yes'

    print(f'#{tc} {ans}')