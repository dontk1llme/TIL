# 숫자 조작 (제출용) D3
# 부분어쩌구 해야되는데 어케하더라...

def makenum(strlst):
    n = ''
    for i in range(len(strlst)):
        n+=strlst[i]
    return int(n)

T = int(input())
for tc in range(1, T+1):
    N = list(input())
    min_ = makenum(N)
    max_ = makenum(N)
    for i in range(len(N)):
        for j in range(i, len(N)):
            nownum = list(str(makenum(N)))
            nownum[i], nownum[j] = nownum[j], nownum[i]
            if nownum[0]!='0':
                newnum = makenum(nownum)
                if newnum <= min_: min_ = newnum
                if newnum >= max_: max_ = newnum

    print(f'#{tc} {min_} {max_}')



