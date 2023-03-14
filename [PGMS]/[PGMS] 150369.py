# PGMS 150369 kakao - 택배 배달과 수거하기
# 최대한 멀리 가서 돌아오면서 해야 이동횟수 최소한임. -> 배열 뒤집기, 정답에 x2 해주기
# 문제 다시 생각해 보기
# https://oh2279.tistory.com/147

def solution(cap, n, deliveries, pickups): #프로그래머스는 이렇게 입력받네,, 여기 안에 코드
    # cap 최대 택배 n 집 개수 del 배달 pick 수거
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    deli = 0
    pick = 0
    for i in range(n):
        deli += deliveries[i]
        pick += pickups[i]

        while deli>0 or pick>0: #아래 연산들이 음수면 해당 위치의 배달/픽업 값이 cap보다 적은 것 -> 추가적으로 배달/픽업 가능.
            deli-=cap
            pick-=cap
            answer += (n - i) *2

    return answer

