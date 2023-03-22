#BOJ 2805 나무 자르기
#시간초과 -> N의 범위가 너무 큼. 이중 for문 시도하면 안됨
# -> 효과적인 탐색이 필요함 -> 이분탐색
# N, M = map(int, input().split())
# hlst = list(map(int, input().split()))
#
# h = max(hlst)
#
# while h>0:
#     sum = 0
#     for i in hlst:
#         if i-h>=0:
#             sum += i-h
#     if sum>=M:
#         break
#     h-=1
#
# print(h)

N, M = map(int, input().split())
hlst = list(map(int, input().split()))
start, end = 1, sum(hlst)

while start<=end:
    mid = (start+end)//2 #중간
    cnt=0
    #나무 자르기
    for i in hlst:
        if i>mid: #나무의 높이가 절단기 높이보다 크면
            cnt+=i-mid
    if cnt>=M: #자른 나무들의 길이가 목표값 이상이면 시작점 조정
        start=mid+1
    else: #이하라면 끝점 조정
        end = mid-1
print(end)