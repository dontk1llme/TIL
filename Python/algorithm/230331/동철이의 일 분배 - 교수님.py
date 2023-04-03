def dfs(n, sm):
    global ans
    # 최대값이지만.. 최대값이 1이므로, 0~1 값을 곱하면 항상 작아짐..
    # 현재 ans보다 <= sm 경우 정답 갱신 가능성이 없음 => 가지치기
    if ans >= sm:
        return

    if n == N:
        ans = max(ans, sm)
        return

    for j in range(N):
        if v[j] == 0:  # 미방문
            v[j] = 1
            dfs(n + 1, sm * (arr[n][j] / 100))
            v[j] = 0


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    v = [0] * N

    dfs(0, 1)  # sm을 0으로 넘겨주면, 이후 곱해도 모두 0...
    print(f'#{test_case} {ans * 100:.6f}')