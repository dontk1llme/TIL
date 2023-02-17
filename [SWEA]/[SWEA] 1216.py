# 1216. [S/W 문제해결 기본] 3일차 - 회문2 D3

def count(arr):
    cnt = 0
    for lst in arr:
        for i in range(N - M + 1):
            if lst[i:i + M] == lst[i:i + M][::-1]:
                cnt = M
    return cnt


# T = int(input())
T = 10
for _ in range(T):
    test_case = int(input())
    ans = 0
    N = 100
    arr = [list(input()) for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))
    for i in range(N):
        M = i
        mx = max(count(arr), count(arr_t))
        if mx > ans:
            ans = mx

    print(f'#{test_case} {ans}')