# boj 17952 과제는 끝나지 않아!
# 스택 (최근 순서대로 하고 있기 때문)
# time 1인 경우는 나눠서 하려고 했는데 break 귀찮아서 그냥 쉽게 감
# 에엥 시간초과? -> pypy3으로 해야 시간초과 안 뜸. 이유는 몰루?

N = int(input()) #이번 학기가 몇 분인지
tp = []
ans = 0
for i in range(N):
    hw = list(map(int, input().split())) #한 줄씩 입력받을 거임 for문으로
    if hw[0]==1: #1이어야 과제.
        tp.append([hw[2],hw[1]]) #time, point
        
    if tp: #과제가 있든 없든 시간은 흐름.
        tp[-1][0] -=1
        if tp[-1][0]==0:
            p = tp.pop()[1]
            ans+=p

            
print(ans)





