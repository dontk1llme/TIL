def solve(arr):
    # 가능한 모든 기준위치를 순회
    for si in range(1, N + 1):
        for sj in range(1, N + 1):
            # 4방향, 뻗어가면서
            for di, dj in ((-1, 1), (0, 1), (1, 1), (1, 0)):
                for mul in range(5):
                    ni, nj = si + di * mul, sj + dj * mul
                    if arr[ni][nj] != 'o':
                        break
                else:  # 모두 'o'인 경우
                    return 'YES'
    return 'NO'


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = ['.' * (N + 2)] + ['.' + input() + '.' for _ in range(N)] + ['.' * (N + 2)]
    ans = solve(arr)
    print(f'#{test_case} {ans}')

#//////////////////////////
def cnt(i, j):
    i, j = i, j
    for di, dj in ((1, 0), (0, 1), (-1, 1), (1, 1)):
        cnt = 0
        for k in range(5):
            ni, nj = i + di * k, j + dj * k
            if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'o':
                cnt += 1
        if cnt == 5:
            return 1
    else:
        return 0


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    ans = 'NO'
    for i in range(n):
        if ans == 'YES':
            break
        for j in range(n):
            if cnt(i, j):
                ans = 'YES'
                break
    print(f'#{tc} {ans}')