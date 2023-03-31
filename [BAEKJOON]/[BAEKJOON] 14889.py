# boj 14889 스타트와 링크 실2
# 요리사 문제랑 거의 비슷한 듯->거의가 아니라 걍 똑같음

def ability(a): # 능력치 계산해주는 함수
    score = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            score += lst[a[i]][a[j]] + lst[a[j]][a[i]]
    return score

def dfs(idx, k):
    global ans
    if idx==N//2: #반만 골라도 나머지는 자동이라 N//2
        S = []
        L = []
        for j in range(N):
            if v[j]: #방문내역 있으면 A, 아니면 B에 저장
                S.append(j)
            else:
                L.append(j)
        # 팀 능력치 계산
        s = ability(S)
        l = ability(L)
        if abs(s-l)<ans: #정답찾기
            ans = abs(s-l)
        return
    for i in range(k,N): #백트래킹
        if not v[i]:
            v[i]=1
            dfs(idx+1, i+1)
            v[i]=0


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

ans = 100*N*len(lst[0])
v = [0]*N
dfs(0,0)

print(ans)