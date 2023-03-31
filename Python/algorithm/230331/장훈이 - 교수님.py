def dfs(n, sm):
    global ans
    # 최소값 구할때 항상(?) 성공하는 가지치기
    # if ans<=sm-B:
    #     return
    if ans == 0:  # 이미 만점!
        return

    if n == N:
        if sm >= B:
            ans = min(ans, sm - B)
        return

    dfs(n + 1, sm + lst[n])  # 포함
    dfs(n + 1, sm)  # X


T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = N * 10000
    dfs(0, 0)

    print(f'#{test_case} {ans}')