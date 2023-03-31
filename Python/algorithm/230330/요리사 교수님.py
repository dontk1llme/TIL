def cal(lst1, lst2):
    # 같은 재료값인 경우 0이므로, 모든 조합: 누적
    sm1 = sm2 = 0
    for i in range(M):
        for j in range(M):
            sm1 += arr[lst1[i]][lst1[j]]
            sm2 += arr[lst2[i]][lst2[j]]
    return abs(sm1 - sm2)


def dfs(n, tlst1, tlst2):
    global ans
    if len(tlst1) > M or len(tlst2) > M:
        return

    if n == N:
        if len(tlst1) == M:
            ans = min(ans, cal(tlst1, tlst2))
        return

    dfs(n + 1, tlst1 + [n], tlst2)  # 요리 1 선택
    dfs(n + 1, tlst1, tlst2 + [n])  # 요리 2 선택


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    M = N // 2
    ans = 20000 * N * N
    dfs(0, [], [])

    print(f'#{test_case} {ans}')