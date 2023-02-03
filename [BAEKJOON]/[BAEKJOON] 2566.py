# [BAEKJOON] 2566 최댓값

arr = [list(map(int, input().split())) for _ in range(9)]

max = -1 #0으로 설정하면 런타임 에러(전부 0이 들어올 경우 고려 안함)
for i in range(9):
    for j in range(9):
        if arr[i][j] > max:
            max = arr[i][j]
            point = [i,j]
print(max)
print(point[0]+1, point[1]+1) #index는 좌표보다 1 작으니까