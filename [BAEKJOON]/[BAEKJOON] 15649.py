#boj 15649 N과 M
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 어렵게 생각했는데... 백트래킹이래
# append, dfs, pop 순서 젭알 좀 외워라

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
