# 2001. 파리 퇴치 D2

T = int(input())
for tc in range(1, T+1):
    N, M= map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    sumlst=[]
    for i in range(N-M+1):
        for j in range(N-M+1):
            sums=0
            for k in range(M): #생각좀해
                for l in range(M):
                    sums+=lst[i+k][j+l]

            sumlst.append(sums)
    print(f'#{tc} {max(sumlst)}')