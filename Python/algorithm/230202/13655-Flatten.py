# 1208. [S/W 문제해결 기본] 1일차 - Flatten D3

T = 10
for tc in range(1, T + 1):
    num = int(input())  # 덤프 횟수
    box = list(map(int, input().split()))

    for i in range(num):
        maxnum = max(box)
        minnum = min(box)
        idxmaxnum = box.index(maxnum)  # 값을 직접 +-하는 게 안 돼서 인덱스로...
        idxminnum = box.index(minnum)
        box[idxmaxnum] -= 1
        box[idxminnum] += 1
        if max(box) == min(box):  # 실행 수보다 적으면...
            break
    print(f'#{tc} {max(box) - min(box)}')


