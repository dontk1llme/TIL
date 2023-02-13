# 2005. 파스칼의 삼각형 D2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        lst[i][0] = 1
        lst[i][i]=1
        for j in range(i):
            if lst[i][j]==0:
                lst[i][j] = lst[i-1][j-1]+lst[i-1][j]
    for i in lst:
        for j in range(N):
            if i[j]==0:
                i[j]=''


    print(f'#{tc}')
    for i in lst:
        print(*i)

