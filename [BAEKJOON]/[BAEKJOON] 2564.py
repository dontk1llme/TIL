#[BAEKJOON] 2564 경비원
# 절대값으로 구간 구하고 총 거리에서 구한 거리 빼면 반대거리겟죠?
#------------------------------------------------------------------------
#(0,0)에서의 길이를... 재요. 단 오른쪽으로 가는거
def get_dst(x,y):
    if x == 1: #북
        return y #0에서부터의 거리 y
    elif x==2: #남
        return w + h + w -y #0에서부터의 거리 y
    elif x==3: #서
        return w+h+w+h-y #0에서부터의 거리 y
    elif x==4: #동
        return w+y #얘도 걍 0에서부터라서 더해주면됨
#입력
w,h = map(int, input().split()) #가로, 세로
shopnum = int(input())
shop = [list(map(int, input().split())) for _ in range(shopnum)]
me = list(map(int, input().split())) #방향, 거리

cnt=0
for i in shop:
    my = get_dst(me[0], me[1])
    to = get_dst(i[0], i[1])
    to1 = abs(my-to)
    to2 = 2*(w+h)-to1
    # print(min(to1, to2))
    cnt+= min(to1, to2) #dst
    # me = i #이거왜함? 바보임? 문제이해못함??
print(cnt)
