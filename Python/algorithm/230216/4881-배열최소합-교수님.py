def dfs(n, sm, v):
    global ans
    # 가지치기는 제일 위! (최소값), 진행해도 정답 갱신 가능성 없을때.. 가지치기
    if ans <= sm:
        return

    # 종료조건: n에 관련된, 항상 종료될 수 있는 조건으로!
    # 종료시점에서 정답처리!
    if n == N:
        if ans > sm:
            ans = sm
        return

    # n+1 하부함수 호출
    for j in range(N):
        if j not in v:
            dfs(n + 1, sm + arr[n][j], v + [j]) #이렇게 하면 메모리랑 시간 더 먹음. 경우 따라 사용

        # if j not in v:        # [2]
        #     v.append(j)
        #     dfs(n+1, sm+arr[n][j])
        #     v.pop()

        # if not v[j]:        # [1] #시간은 얘가 젤 빠름
        #     v[j] = 1        # [1] 방문표시
        #     dfs(n+1, sm+arr[n][j])
        #     v[j] = 0        # [1]사용후 반드시 clear!


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 10 * N
    # v = [] #밑에 두 개 할 때는 얘 필요함 visited
    dfs(0, 0, [])
    print(f'#{test_case} {ans}')