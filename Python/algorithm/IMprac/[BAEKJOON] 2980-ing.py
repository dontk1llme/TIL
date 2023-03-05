# [BAEKJOON] 2980 도로와 신호등

N,L = map(int,input().split())
lst = [-1]*(L+1)
for i in range(N):
    D,R,G = map(int,input().split())
    lst[D] = R
