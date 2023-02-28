ip = int(input())
dct = {'W': 0, 'B': 1, 'R': 2}
for case in range(1, ip+1):
    n, m = map(int, input().split())
    lst = list(input() for _ in range(n))
    cnt = [[0, 0, 0] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            cnt[i][dct[lst[i][j]]] += 1
    mn = 10**4
    for i in range(1, n-1): #b 개수
        for j in range(1, n-i): #b 시작줄
            ans = 0
            for k in range(1, n-1):
                if k < j:
                    ans += cnt[k][1] + cnt[k][2]
                elif j <= k < j+i:
                    ans += cnt[k][0] + cnt[k][2]
                else:
                    ans += cnt[k][1] + cnt[k][0]
            if ans < mn:
                mn = ans
    mn += cnt[0][1] + cnt[0][2] + cnt[-1][0] + cnt[-1][1]
    print(f'#{case} {mn}')