#하림언니
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    sq = [list(map(str, input())) for _ in range(n)]
    idx1, idx2 = [], []
    for i in range(n):
        for j in range(n):
            if sq[i][j] == '#':
                idx1.append([i, j])
                idx2.append([j, i])
    idx2.sort()
    if idx1 == idx2 and len(idx1) == (idx1[-1][0] - idx1[0][0] + 1) ** 2:
        ans = 'yes'
    else:
        ans = 'no'
    print(f'#{tc} {ans}')

#수형님코드

T = int(input())
for t in range(1, T + 1):
    n, ans, k_l = int(input()), "yes", []
    arr= [input() for _ in range(n)]
    for i in arr + list(map(lambda x: "".join(x), zip(*arr))):
        k = i.count("#")
        if k:
            k_l.append(k)
            if "#" * k not in i:
                ans = "no"
                break
    if int((sum(k_l)//2)**0.5) != k_l[0] or len(set(k_l)) - 1: ans = "no"
    print(f"#{t} {ans}")