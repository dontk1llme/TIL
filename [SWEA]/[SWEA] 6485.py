#6485. 삼성시의 버스 노선 D3

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    alist=[]
    blist=[]
    for n in range(N):
        a, b = map(int, input().split())
        alist.append(a)
        blist.append(b)
    P = int(input())
    plist=[]
    for p in range(P):
        c = int(input())
        plist.append(c)
    #이제 입력 끝............


    print(f'#{tc}', end=' ')
    for i in plist:
        cnt=0
        for j in range(N):
            if i>=alist[j] and i<=blist[j]: cnt+=1
        print(cnt, end=' ')
    print() #테케가 하나라 엔터 안 쳐서 틀렸다고 됨 ;;



