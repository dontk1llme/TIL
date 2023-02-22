# [파이썬 S/W 문제해결 기본] 8일차 - subtree (제출용) D2

def pre(n):
    global cnt
    try:
        cnt+=1
        pre(tree[n][0])
        pre(tree[n][1])
    except:
        return


T = int(input())
for tc in range(1, T+1):
    E,N = map(int,input().split())
    lst = list(map(int, input().split()))
    tree = [[] for _ in range(E+2)]
    for i in range(0,len(lst),2):
        p,c = lst[i], lst[i+1]
        tree[p].append(c)
    cnt = 0
    pre(N)
    print(f'#{tc} {cnt}')
