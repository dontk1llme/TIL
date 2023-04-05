# boj 2661 좋은수열 ????????
# 백트래킹
# https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-2661%EB%B2%88-%EC%A2%8B%EC%9D%80-%EC%88%98%EC%97%B4-Python
# https://namhandong.tistory.com/148

def check(res, cnt):
    for k in range(cnt):
        stmp = res[k:]
        for i in range(1, len(stmp)//2+1):
            checkV = stmp[:i]
            if checkV == stmp[i:i+i]:
                return False
    return True

def backTracking(cnt):
    # 나쁜 순열이면 종료
    if not check(res, cnt):
        return -1
    if cnt==N:
        print(*res, sep='')
        return 0
    for i in range(1,4): #123 순서
        res.append(i)
        if backTracking(cnt+1)==0: #찾앗으면 즉시리턴
            return 0
        res.pop()

N = int(input())
res = []
backTracking(0)
