#  [BAEKJOON] 10431 줄세우기

T = int(input())
for _ in range(1,T+1):
    lst = list(map(int, input().split()))
    newlst = [lst[1]]
    cnt =0
    for i in range(2,len(lst)):
        now = lst[i]
        up = 21
        for j in range(len(newlst)):
            if newlst[j] > now:
                up = j
                break
        newlst.append(now)
        if up>=0:
            for k in range(len(newlst)-1, up, -1):
                newlst[k], newlst[k-1] = newlst[k-1], newlst[k]
                cnt+=1
    print(lst[0], cnt)

