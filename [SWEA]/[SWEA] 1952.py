# swea 1952 수영장
# 3월, 1년 경우 나누는 게 어렵다 인덱스 전달을 어케 해줘야 계산이랑 저거랑 따로하지??
# https://ryuwc.tistory.com/121

T = int(input())

def cal(idx, ssum):
    global ans
    if ssum>ans: return #가지
    if idx>=12: #종료
        ans = min(ans,ssum)
        return

    if plan[idx]: #for문없이 그냥 해도 되는군아....
        cal(idx+1, ssum+(plan[idx]*fee[0]))
        cal(idx+1, ssum+fee[1])
        cal(idx+3, ssum+fee[2])
        cal(idx+12, ssum+fee[3])
    else:
        cal(idx+1, ssum)


for tc in range(1, T+1):
    fee = list(map(int, input().split())) #1일, 1달, 3달, 1년
    plan = list(map(int, input().split()))

    ans = fee[0]*365 #최대값
    cal(0,0)
    print(f'#{tc} {ans}')


#/////////////////////////////////////
# 나의 망한코드
# T = int(input())
#
# def cal(plan,feeidx): #계산
#     if feeidx==0:
#         return plan*fee[feeidx]
#     elif feeidx==1:
#         return fee[feeidx]
#
# def dfs(idx, ssum):
#     global ans
#
#     if ssum>=ans: #가지치기
#         return
#     if idx==11: #종료
#         ans = ssum
#
#     if plan[idx]:
#         for i in range(len(fee)):
#             if i == 0: #일일
#                 tmp = plan[idx] * fee[i]
#                 dfs(idx+1, ssum+tmp)
#             elif i == 1: #한달
#                 tmp = fee[i]
#                 dfs(idx+1, ssum+tmp)
#             elif i == 2 and idx<10: #세달
#                 tmp = fee[i]
#                 dfs(idx+3, ssum+tmp)
#             elif i==3: #1년
#                 dfs(11, fee[i])
#
#
#
#
# for tc in range(1, T+1):
#     fee = list(map(int, input().split())) #1일, 1달, 3달, 1년
#     plan = list(map(int, input().split()))
#
#     ans = fee[0]*365 #최대값
#     dfs(0,0)
#     print(f'#{tc} {ans}')