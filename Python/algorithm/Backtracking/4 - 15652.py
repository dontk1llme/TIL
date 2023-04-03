# 15652
# sorted 쓰면 시간초고ㅏ
# https://zidarn87.tistory.com/336

def dfs(cnt, idx):
    if cnt-1 == M:
        print(' '.join(map(str, lst)))
        return
    for i in range(idx, N+1):
        lst.append(i)
        dfs(cnt+1, i)
        lst.pop()

N,M = map(int, input().split())
lst = []
dfs(1,1)
# /////////////////////////////////
# 시간초과 코드
# def dfs():
#     if len(lst)==M:
#         if lst == sorted(lst):
#             print(' '.join(map(str, lst)))
#         return #리턴 위치 조심
#
#     for i in range(1, N+1):
#         lst.append(i)
#         dfs()
#         lst.pop()
#
#
# N,M = map(int, input().split())
# lst = []
# dfs()