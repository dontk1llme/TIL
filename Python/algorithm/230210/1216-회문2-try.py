# swea 1216. [S/W 문제해결 기본] 3일차 - 회문2 D3
#회문1 코드 우려먹기... 근데 이제 교수님거
#답은 맞는데 시간초과!!!!!!!!!!!!!!!!!!!!!!!!!!!


# 1차원 배열에 str으로 입력받기
# 진행은 함수 만들어서 할게요...
# 가로는 그냥 진행하면 됨
# 세로는 새로운 str 배열 만들어서 진행해주면 되겟죠?
def count(arr):
    cnt = 0
    for lst in arr:
        for i in range(N - M + 1):
            # if lst[i:i + M] == lst[i:i + M][::-1]: #시간초과라서 반잘라서하면 된다그럼
            # cnt=M
            if i%2==0:
                if lst[i:(i+M)//2]==lst[(i+M)//2:i+M][::-1]: #안되자나 ㅁㅊ
                    cnt = M
            else:
                if lst[i:(i+M)//2]==lst[(i+M)+1//2:i+M][::-1]: #안되자나 ㅁㅊ
                    cnt = M
    return cnt


# T = int(input())
T = 10
for _ in range(T):
    test_case=int(input())
    ans = 0
    N = 100
    arr = [list(input()) for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))
    for i in range(N):
        M=i
        mx = max(count(arr), count(arr_t))
        if mx>ans:
            ans=mx

    print(f'#{test_case} {ans}')

