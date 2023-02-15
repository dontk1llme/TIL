# swea 4408. 자기 방으로 돌아가기 D4
# 윗줄 홀, 아랫줄 짝.
# 홀->홀, 짝->짝 갈때는 ㄱㅊ ex(1,3 / 3,7)
# 반대는 안됨 ex(1,4 / 3,6)
# 수 큰 방에서 작은 방으로 갈 수도 있음
#///////////
# ㄴㄴ 걍 400짜리 배열 만들어서 지나간 루트에 +1 해주면 됨.
# 그리고 그 배열에서 젤 큰 값 넣어 주면 됨.

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #돌아가야 할 학생들의 수
    cor = [0]*200 #지나간길 (근데 홀짝 반반 해서 하니까 200만 있어도 됨)
    #학생 한명씩 돌며 지나간 복도에 값 1씩 추가
    for _ in range(N):
        start, end = map(int, input().split()) #잇는방, 가야할방
        if start<=end:
            x = (start-1)//2
            y = (end-1)//2
        else:
            x = (end-1)//2
            y = (start-1)//2
        for idx in range(x,y+1):
            cor[idx]+=1

    max = 0
    for i in cor:
        if i > max:
            max = i
    print(f'#{tc} {max}')






