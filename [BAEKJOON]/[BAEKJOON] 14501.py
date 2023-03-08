# boj 14501 퇴사
# https://great-park.tistory.com/48
# DP

N = int(input())
lst = [list(map(int, input().split()))for _ in range(N)] #걸리는 시간 T, 금액 P

#bottom-up
dp = [0 for _ in range(N+1)] #i번쨰 일까지 일했을 때 얻을 수 있는 최대 수익
for i in range(N):
    for j in range(i+lst[i][0], N+1): #j: 상담이 가능한 모든 날짜
        if dp[j]<dp[i]+lst[i][1]:
            dp[j]=dp[i]+lst[i][1] #최대 수익 저장

print(dp[-1])