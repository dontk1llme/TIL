# [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기 (제출용) D2

# 그냥 N을 10이랑 20으로 나눠서. 대신 모든 경우.
# 경우의 수 나왔다 하면 규칙부터 찾기...
# --> DP!!!!!!
# if 20: 3, 30: 5, 40: 11, 50: 21
#-> f(N) = 2*f(N-2)+f(N-1)
# 앞의 거에서 경우를 더해 준다고 생각. 

#////////////////////////////////////////////////////
# https://velog.io/@wltn39/SWEA-4869-%EC%A2%85%EC%9D%B4%EB%B6%99%EC%9D%B4%EA%B8%B0
#재귀
# def tape(N):
#     if N%10==0:
#         if N==10:
#             return 1
#         elif N==20:
#             return 3
#         else:
#             return(tape(N-10)+2*(tape(N-20)))

# T = int(input())
# for tc in range(1, T+1):
#     #가로:20, 세로:N
#     N = int(input()) #10의 배수
#     print(f'{tc} {tape(N)}')
#///////////////////////////////////////////////
# https://velog.io/@yunhlim/SWEA-4869.-%ED%8C%8C%EC%9D%B4%EC%8D%AC-SW-%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0-%EA%B8%B0%EB%B3%B8-4%EC%9D%BC%EC%B0%A8-%EC%A2%85%EC%9D%B4%EB%B6%99%EC%9D%B4%EA%B8%B0-D2
#DP
T = int(input())
dp = [0,1,3]
for tc in range(1,T+1):
    N=int(input())//10
    while N>=len(dp):
        dp.append(2*dp[len(dp)-2]+dp[len(dp)-1])
    print(f'#{tc} {dp[N]}')


