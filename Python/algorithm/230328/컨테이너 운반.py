# [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반 (제출용) D3
# 교수님 코드
# 그리디->규칙성(정렬 후)->전체 적용.
# 1. 정렬 -> 무거운 순으로 (내림차순)
# 2. 화물 하나씩 꺼내서 가능한 경우 트럭으로 이동

T = int(input())

for tc in range(1,T+1):
    N,M = map(int, input().split()) #f
    wj = list(map(int, input().split())) #화물의 무게, len=N
    tj = list(map(int, input().split())) #트럭의 적재용량 len=M

    #내림차순 정렬
    wj.sort(reverse=True)
    tj.sort(reverse=True)

    #하나씩 짐 내리면서 현재 트럭에 가능한지 체크
    i = ans = 0
    for n in wj:
        if n<=tj[i]: #현재 트럭에 적재 가능
            ans+=n   #누적
            i+=1     # 다음 트럭
            if i==M:
                break

    print(f'#{tc} {ans}')