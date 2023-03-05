# [BAEKJOON] 11399 ATM
N = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
ans =0
i = 0
while i<N:
    turn = 0
    for j in range(i,N):
        turn+=lst[j]
    ans+=turn
    i+=1
print(ans)