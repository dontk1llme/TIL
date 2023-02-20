# [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기 (제출용) D3

# 피자 N개만큼 넣어서 돌리다가 0 되면 다음 피자 넣음
# 큐에 공간이 잇고 피자에 원소가 잇다면 큐에 추가
# 큐에 원소가 한 개 남을 때까지 반복

T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = list(enumerate(lst)) #인덱스 저장용

    # 들어간 핏자
    inpizza=lst[:N]
    # 나머지 핏자로 갱신
    lst = lst[N:]
    while len(inpizza)!=1:
        num,ch = inpizza.pop(0)
        ch //=2
        if ch: inpizza.append((num,ch)) #치즈 남앗으면 다시 넣기
        else: 
            if lst: inpizza.append(lst.pop(0)) #없으면 새 피자 넣기
    print(f'#{tc} {inpizza.pop()[0]+1}')














