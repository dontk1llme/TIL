# 1206. [S/W 문제해결 기본] 1일차 - View

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    around = [-2,-1,1,2] #주변건물 인덱스용
    ans = 0
    for i in range(2, N-2): #맨 왼쪽 두 칸과 맨 오른쪽 두 칸에 있는 건물은 항상 높이가 0
        nl = [] #주변건물 높이
        for j in around:
            nl.append(arr[i-j]) #around 이용해서 저장해용
        near = max(nl)
        if arr[i] > near:
            ans += arr[i]-near
    print(f'#{tc} {ans}')