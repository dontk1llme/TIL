# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금 D3
# 백트래킹
# https://hyunse0.tistory.com/321

def change(num, time):
    global ans
    tmp = ''
    for n in num:
        tmp+=n
    if int(tmp) in ans[time]:
        return
    else:
        ans[time].append(int(tmp))

    if time==0:
        return

    l = len(num)
    for i in range(l):
        for j in range(i+1, l):
            num[i], num[j] = num[j], num[i]
            change(num, time-1)
            num[i], num[j] = num[j], num[i]


T = int(input())
for tc in range(1, T+1):
    nums, time = input().split()
    num = list(nums)
    ans = [[] for _ in range(int(time)+1)]  #0번쨰 인덱스가 time번 바뀐 애들. time번째 인덱스가 처음 시작한 애
    change(num, int(time))

    print(f'#{tc} {max(ans[0])}')