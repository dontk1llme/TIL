# [BAEKJOON] 2605 줄세우기

N = int(input())
lst = list(map(int, input().split()))
ans = []
for i in range(1,N+1):
    ans.append(i)
    l = len(ans)-1
    time = lst[l]
    for j in range(time):
        ans[l],ans[l-1] = ans[l-1], ans[l]
        l-=1

print(*ans)

