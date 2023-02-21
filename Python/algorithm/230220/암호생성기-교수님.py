T = 10
for tc in range(1, T+1):
    _ = input()
    q = list(map(int, input().split()))
    n = t = 1
    while t:
        t = q.pop(0)-n
        if t<0:         # t = max(0, t)
            t=0
        q.append(t)
        n = n%5 + 1
    print(f'#{tc}', *q)