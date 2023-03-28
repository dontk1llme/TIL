# 전형적인 백트래킹 유형
# 최소값 찾기에서 무조건 먹히는 가지치기!

def dfs(n, sm):
    global ans
    # [3] 가지치기는 가장 위, 가장 나중에 고민/추가
    if ans <= sm:
        return

    # [1] 종료조건 처리
    if n == N:  # 종료조건(n관련): 반드시 이곳에서만 정답처리!
        ans = min(ans, sm)  # 최소값 갱신
        return

    # [2] 하부호출(정해지지 않은 개수인 경우 for문)
    for j in range(N):
        if v[j] == 0:
            v[j] = 1
            dfs(n + 1, sm + arr[n][j])
            v[j] = 0  # 호출후 반드시 clear!


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 10 * N  # 최소값을 구하는 문제 => 가장 큰 값으로 초기화
    v = [0] * N
    dfs(0, 0)

    print(f'#{test_case} {ans}')