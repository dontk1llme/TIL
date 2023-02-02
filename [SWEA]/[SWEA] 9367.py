# 9367. 점점 커지는 당근의 개수 D1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    size = list(map(int, input().split()))
    cnt = [1] * len(size)
    count=0
    for i in range(1, len(size)):
        if size[i]>size[i-1]:
            cnt[count]+=1
        else: count+=1
    print(f'#{tc} {max(cnt)}')