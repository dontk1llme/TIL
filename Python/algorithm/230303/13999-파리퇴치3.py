# 파리퇴치3 (제출용) D2

# +
d1= [(1,0),(-1,0),(0,1),(0,-1)]
# x
d2 = [(1,1),(-1,-1), (1,-1),(-1,1)]

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            cnt1 = cnt2 = 0
            cnt1+=lst[i][j]
            cnt2+=lst[i][j]
            for d in range(4):
                for k in range(1,M): #k->k칸만큼 보는 거니까 당연히!
                    ni1, nj1 = i+d1[d][0]*k, j+d1[d][1]*k
                    if 0<=ni1<N and 0<=nj1<N:
                        cnt1+=lst[ni1][nj1]
                    ni2, nj2 = i+d2[d][0]*k, j+d2[d][1]*k
                    if 0<=ni2<N and 0<=nj2<N:
                        cnt2+=lst[ni2][nj2]
            if ans<cnt1:
                ans = cnt1
            if ans<cnt2:
                ans=cnt2

    print(f'#{tc} {ans}')