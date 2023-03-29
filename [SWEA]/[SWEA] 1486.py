# swea 1486 장훈이의 높은 선반
#함수 인자 조심, 포함여부 조심

T = int(input())

def check(idx,height): #자꾸 lst를 통쨰로 주려고 하는데 그러지 말고 인덱스를 줘라
    global ans

    if B<=height<ans: #최소값 갱신
        ans = height
    if idx==N: #종료 (끝까지 왔으면 안되는거) #얘가 갱신 위에 있어도 안됨. 가지치기가 아니라서
        return

    #해당 인덱스의 키를 포함시키지 않는 경우
    check(idx+1, height)
    #포함시키는 경우
    check(idx+1, height+lst[idx])


for tc in range(1, T+1):
    N,B = map(int, input().split())
    lst = list(map(int, input().split()))

    # 높이가 B 이상인 탑 중에서 높이가 가장 낮은 탑
    ans = 20*10000 #N최대20, B최대10000 # 최소값을 찾아야 되기 땜에 . ..
    check(0, 0) #0번째 인덱스부터, 시작의 height은 0이니까

    print(f'#{tc} {ans-B}')