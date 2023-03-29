# 중요한 문제!!

def dfs(n, sm, s):
    global ans
    if ans <= sm:
        return

    if n == N:
        # 지금까지의 비용 + 복귀비용
        ans = min(ans, sm + arr[s][1])
        return

    for j in range(N, 1, -1):
        if v[j] == 0:
            v[j] = 1
            dfs(n + 1, sm + arr[s][j], j)
            v[j] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    # 위쪽과 왼쪽에 여분공간으로 문제 그림과 번호 맞춤
    arr = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    v = [0] * (N + 1)
    ans = 100 * N

    # 방문구역수, 사용량, 시작구역번호
    dfs(1, 0, 1)

    print(f'#{test_case} {ans}')