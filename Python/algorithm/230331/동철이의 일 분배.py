# swea 1865. 동철이의 일 분배 D4

T = int(input())

def work(idx, p):
    global ans
    if p <= ans: return #가지치기
    if idx >= N:
        ans = p
        return
    for i in range(N):
        if not v[i]:
            v[i]=1
            work(idx+1, p*(lst[idx][i])/100) #확률!!
            v[i]=0

for tc in range(1, T+1):
    N = int(input()) #1<=N<=16
    lst = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    v = [0]*N
    work(0,100)
    # print(f'#{tc} {round(ans,6)}') #round 하면 뒤에 0까지 나오지가 않음
    print('#{} {:6f}'.format(tc, ans))