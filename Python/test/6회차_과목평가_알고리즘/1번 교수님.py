T = int(input())
for tc in range(1,T+1):
    N = int(input())
    bits = int(input(),16)

    cnt = 0
    ans = 0
    for j in range(4*N): #4비트니까 bit0 ~ MSB(최상위 비트)까지 체크
        if bits&(1<<j): #bit j가 0이 아닌 경우
            cnt+=1
            ans = max(cnt,ans)
        else:
            cnt=0
    print(f'#{tc} {ans}')



