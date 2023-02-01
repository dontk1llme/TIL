# 가장 큰 값을 출력하기
# input
# 3
# 5
# 55 7 78 12 42
# 6
# 55 6 68 100 42 1
# 7 
# 55 7 78 12 42 2 90

# output
# #1 78
# #2 100
# #3 90

T = int(input())
for tc in range(1, T+1): # tc = testcase
    N = int(input())
    arr = list(map(int, input().split()))
    maxV=arr[0] # 첫 원소를 최대로 가정
    for i in arr:
        if maxV < i:
            maxV = i
    print(f'#{tc} {maxV}')



