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