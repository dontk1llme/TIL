# BOJ 2116 주사위 쌓기
#주사위 1만개라고 해서 전부 순회하는 게 맞나 싶었는데 맞아버렸던 거임

# ABCDEF -> AF/BD/CE
rotate = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}

N = int(input()) #주사위 개수
lst = [list(map(int, input().split())) for _ in range(N)]

max_ = 0
for i in range(6): #첫째 주사위
    res = []
    tmp = [1,2,3,4,5,6]
    tmp.remove(lst[0][i]) #주사위 아랫면
    next = lst[0][rotate[i]] #첫 주사위의 윗면
    tmp.remove(next)
    res.append(max(tmp)) #더할 값 중 최대값
    for j in range(1,N): #둘째 주사위부터
        tmp = [1, 2, 3, 4, 5, 6]
        tmp.remove(next) #현재 주사위의 아랫면
        next = lst[j][rotate[lst[j].index(next)]] #현재 주사위의 윗면
        tmp.remove(next)
        res.append(max(tmp))
    res = sum(res)
    if max_<res:
        max_=res
print(max_)



