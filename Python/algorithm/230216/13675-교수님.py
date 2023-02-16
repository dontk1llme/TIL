
def dfs(n, sm, cnt):
    global ans
    # [0] 가지치기 제일 위쪽에!
    # 더 이상 진행해도 정답을 갱신할 가능성이 없는 경우
    if sm > K or cnt > CNT:
        return

    # [1] 종료조건: n에 관련된 무조건 종료되는 기준점
    # 가능하면 종료일때 정답 관련 처리를 진행
    if n == N:
        if sm == K and cnt == CNT:
            ans += 1
        return
    # [2] 하부함수(n+1) 호출: 호출시 등 += 1 값을 갱신하는 동작 금지!!!
    dfs(n + 1, sm + lst[n], cnt + 1)  # 포함하는 경우
    dfs(n + 1, sm, cnt)  # 포함하지 않는 경우


lst = [n for n in range(1, 13)]
T = int(input())
for test_case in range(1, T + 1):
    CNT, K = map(int, input().split())
    N = 12

    ans = 0
    dfs(0, 0, 0)
    print(f'#{test_case} {ans}')