
# 55 7 78 12 42
# for i: n-1 -> 1 # 각 구간의 끝
#     for j: 0 -> i-1 # 비교할 왼쪽 원소
#         if arr[j] > arr[j+1]
#             arr[j]<->arr[j+1]

arr = list(map(int, input().split()))
N = len(arr) 
for i in range(N-1, 0, -1): #각 구간의 끝
    for j in range(i): #비교할 왼쪽 원소
        if arr[j]>arr[j+1]: #> 말고 < 하면 내림차순으로 가능
            arr[j],arr[j+1] = arr[j+1], arr[j] #큰 원소 오른쪽으로 (오름차)
print(*arr)