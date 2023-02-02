# Greedy로 풀기
# 나중에는 순열로도 풀라고함

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    cnt = [0] * 12  #9까지의 수인데 12개 만드는 이유: run의 경우일 때 3개 비교해야 하는데 인덱스에러 안 나게
    for i in range(6):
        cnt[num % 10] += 1 #맨 앞 숫자가 0일 때도 더해짐. 6번 반복하니깐...
        num //= 10
    i = trp = run = 0

    while i<10:
        if cnt[i]>=3:
            cnt[i]-=3
            trp+=1
            continue   #만약 cnt[i]가 6개이면 얘를 또 돌아야 하기 때문에 continue 해 줘서 i++가 되지 않도록

        if cnt[i]>=1 and cnt[i+1]>=1 and cnt[i+2]>=1:
            cnt[i] -= 1
            cnt[i + 1] -= 1
            cnt[i + 2] -= 1
            run+=1
            continue
        i+=1
    if trp + run == 2:
        print(f'#{tc} 1')
    else: print(f'#{tc} 0')


