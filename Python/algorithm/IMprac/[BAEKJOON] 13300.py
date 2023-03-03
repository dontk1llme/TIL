# [BAEKJOON] 13300 방 배정

N, K = map(int, input().split())
std = [[0,0]for _ in range(7)]
room = 0

for i in range(N):
    s, y = map(int, input().split())
    std[y][s]+=1

for i in std:
    for k in i:
        if k>0:
            if k%K==0:#사람 수가 나누어떨어지면
                room+=k//K
            else: room+=k//K+1


print(room)