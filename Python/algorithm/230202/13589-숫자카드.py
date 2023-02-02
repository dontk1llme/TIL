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

#교수님코드
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     lst = list(map(int, input()))
#
#     # [1] 빈도수 배열에 빈도 표시
#     cnts = [0] * 10
#     for n in lst:
#         cnts[n] += 1
#
#     # [2] 최대값의 index 찾기(같은 개수면 큰 값)
#     idx = 0
#     for i in range(1, 10):
#         if cnts[idx] <= cnts[i]:
#             idx = i
#
#     print(f'#{test_case} {idx} {cnts[idx]}')
