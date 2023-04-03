# 15649

def dfs():
    if len(lst)==M: #수열의 길이가 m이 되면 다 출력
        print(' '.join(map(str, lst)))
        return
    for i in range(1,N+1): #1부터 N까지의 숫자를 모두 확인하는 것
        if i not in lst:
            lst.append(i)
            dfs()
            lst.pop()


N,M = map(int, input().split())
lst = []
dfs()