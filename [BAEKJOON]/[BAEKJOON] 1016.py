# 1016 - 제곱 ㄴㄴ수
# 에라토스테스의 체 <- 이거 모르면 틀림(시간초과)
# ㄴ> 제곱수의 배수까지 싹 지워주면서 진행해야 됨
# https://velog.io/@superhong/%EB%B0%B1%EC%A4%80-1016%EB%B2%88-%EC%A0%9C%EA%B3%B1-%E3%84%B4%E3%84%B4-%EC%88%98-Python
#https://imksh.com/69


N,M = map(int, input().split())
ans = M-N+1
bscnt = [False]*(M-N+1)
for i in range(2, int(M**0.5+1)): #에라토스테네스
    square = i**2 #제곱수
    for j in range((((N - 1) // square) + 1) * square, M + 1, square): #ㅔ??
        if not bscnt[j - N]:  # 해당 인덱스 값이 False라면
            bscnt[j - N] = True  # True 바꿔준 뒤
            ans -= 1  # answer에서 1을 빼줌
    # 다음 반복에서는 나뉘어 떨어지더라도 이미 TRUE이기 때문에 answer에서 1이 빼지지 않음.
print(ans)