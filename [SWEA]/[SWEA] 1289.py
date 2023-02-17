# 1315. 오목 판정 D3
# 입력받은 리스트의 앞에서부터 lst[i]와 org[i]가 다르면 org[i~N]까지 쭉 변경
# str인지 int인지 주의!
# 변경한 후 cnt+1

T = int(input())
for tc in range(1,T+1):
    ans = 0
    lst = list(map(int, input()))
    org = [0]*len(lst)
    for i in range(len(lst)):
        if lst[i]!=org[i]:
            n=i
            while n<len(lst):
                org[n]=lst[i]
                n+=1
            ans+=1

    print(f'#{tc} {ans}')
