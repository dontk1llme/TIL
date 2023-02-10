# 1946. 간단한 압축 풀기 D2
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = []
    for i in range(N):
        chr, cnt = map(str, input().split())
        for j in range(int(cnt)):
            lst.append(chr)

    print(f'#{tc}')
    cnt = 0
    while len(lst)>0:
        print(lst.pop(0),end='')
        cnt+=1
        if cnt==10:
            print()
            cnt=0
    print()
