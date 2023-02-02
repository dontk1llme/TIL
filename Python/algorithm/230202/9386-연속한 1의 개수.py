# SWEA 9386 연속한 1의 개수 D1
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int,input()))

    cnt=[0]*len(num)
    idx=0

    for i in range(1,len(num)):
        if num[i-1]==1: #앞 애가 1이면
            if num[i]==1: #근데 뒤 애도 1이면
                cnt[idx]+=1 #웅 세라
            else:
                cnt[idx] += 1 #아니어도 1 세야함 앞 애 케이스를 안 세서...
                idx+=1          #카운트 인덱스 넘겨용
    if num[-1] == 1 and num[-2]==1: #맨 마지막 애 비교할 위치가 애매해서...
        cnt[idx] += 1


    print(f'#{tc} {max(cnt)}')