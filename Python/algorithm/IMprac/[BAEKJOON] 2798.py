# boj 2798 블랙잭

N,M = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
#범위 주의!!!!!!! +1, -2,-1 안 하면 틀림.
for i in range(len(lst)-2):
    for j in range(i+1,len(lst)-1):
        for k in range(j+1, len(lst)):
            now = lst[i]+lst[j]+lst[k]
            if ans<now<=M:
                ans = now
print(ans)