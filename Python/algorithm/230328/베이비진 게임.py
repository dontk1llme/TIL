#  [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임 (제출용) D3
# https://cys4585.tistory.com/19

T = int(input())

def bbg(player):
    global ans
    # 3개 뽑아서 조합 만들기
    for i in range(len(player)):
        for j in range(i+1, len(player)):
            for k in range(j+1, len(player)):
                #bbg 검사
                if player[i]==player[j]==player[k]:
                    return True
                sorted_now= sorted([player[i],player[j],player[k]])
                if sorted_now[0]+1==sorted_now[1] and sorted_now[1]+1==sorted_now[2]:
                    return True
    return False

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    player1=[]
    player2=[]
    ans = 0 #0 무승부, 1 승1, 2 승2
    for i in range(0,len(lst),2):
        player1.append(lst[i])
        player2.append(lst[i+1])
        #len 3 이상이 되면 run or triplet 검사
        if len(player1) >= 3 and bbg(player1):
            ans=1
            break
        elif len(player2) >= 3 and bbg(player2):
            ans=2
            break

    print(f'#{tc} {ans}')