# 15650

def dfs():
    if len(lst)==M:
        if lst==sorted(lst): #1번이랑 이 줄만 다름
            print(' '.join(map(str, lst)))
            return

    for i in range(1, N+1):
        if i not in lst:
            lst.append(i)
            dfs()
            lst.pop()

N,M = map(int, input().split())
lst = []
dfs()