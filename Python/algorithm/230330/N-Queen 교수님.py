# 경우의 수는 가지치기가 안됨
# 룩업테이블! 생각하기
def dfs(n):
    global ans
    if n == N:
        ans += 1
        return

    for j in range(N):
        if v1[j] == v2[n + j] == v3[n - j] == 0:
            v1[j] = v2[n + j] = v3[n - j] = 1
            dfs(n + 1)
            v1[j] = v2[n + j] = v3[n - j] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    v1, v2, v3 = [[0] * (2 * N) for _ in range(3)]
    ans = 0
    dfs(0)
    print(f'#{test_case} {ans}')

#////////////////////////////////////////////////
