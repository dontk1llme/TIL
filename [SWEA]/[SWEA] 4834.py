#4834 숫자카드 D1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = int(input())
    cnt = [0]*10
    for i in range(N):
        cnt[num % 10] += 1  # 맨 앞 숫자가 0일 때도 더해짐. 6번 반복하니깐...
        num //= 10

    card = -1
    count=0
    for i in range(10): #카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다. -> 나중에 i가 커졋을 때도 갱신하기 위해 for문 사용
                        #원래는 그냥 idx랑 max만 썻다가 위 조건 만족 못햇음
        if cnt[i]>=card:
            count=i
            card=cnt[i]

    print(f'#{tc} {count} {card}')
