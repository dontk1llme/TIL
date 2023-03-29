# 연습문제 베이비진 게임 (제출용) D2

T = int(input())

def check(lst):  # run triplet 확인
    cnt = 0
    # 0:3 또는 3:6 값이 run, triplet
    for i in range(0, N, 3):
        if lst[i] == lst[i + 1] == lst[i + 2] or lst[i] + 2 == lst[i + 1] + 1 == lst[i + 2]:
            cnt += 1
    return cnt == 2  # true false

def dfs(n, tlst):  # 그냥 백트래킹!
    global ans

    if ans: #답을 찾은 경우 : 가지치기기
       return

    if n == N:
        if check(tlst):
            ans = 1
        return
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n + 1, tlst + [lst[j]])
            v[j] = 0


for tc in range(1, T + 1):
    lst = list(map(int, input()))
    # print(lst)
    N = 6
    v = [0] * N
    ans = 0
    dfs(0, [])  # 0부터, tmplst
    print(f'#{tc} {ans}')
