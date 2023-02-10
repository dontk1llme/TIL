def count(arr):
    cnt = 0
    for lst in arr:
        for i in range(N - M + 1):
            if lst[i:i + M] == lst[i:i + M][::-1]:
                cnt += 1
    return cnt


# T = int(input())
T = 10
for test_case in range(1, T + 1):
    M = int(input())
    N = 8
    arr = [list(input()) for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))
    ans = count(arr) + count(arr_t)
    print(f'#{test_case} {ans}')