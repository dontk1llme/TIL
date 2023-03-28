# swea 2817 부분 수열의 합 D3
# https://serendipity24.tistory.com/112

T = int(input())

def check(idx, sum):
    global ans

    if idx >= N:
        return

    tmp = sum + lst[idx]
    if tmp==K:
        ans+=1

    check(idx+1, sum) #다음 인덱스로 넘어가서 인덱스에 해당하는 값과 sum의 합이 입력 받은 K와 같은지 비교
    check(idx+1, tmp) #위와 같긴 한데 인덱스에 해당하는 값과 이전의 인덱스에 있던 값들을 모두 더해서 K와 같은지 비교

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 0
    check(0, 0)
    print(f'#{tc} {ans}')