#  연습문제 베이비진 게임 (제출용) D2
# 완전탐색 리스트! 해서
# 베이비진 검사하기
# https://m.blog.naver.com/ojeongeuni/221325229337

def bbg(i,k): #i: 값을 결정할 자리, k: 결정할 개수
    global ans
    if i==k: #babygin 판별
        now = lst
        if (now[0]+1==now[1] and now[1]+1==now[2]) or (now[0]==now[1]==now[2]):
            if (now[3]==now[4]==now[5]) or (now[3]+1==now[4] and now[4]+1==now[5]):
                ans = 1
                return

    else: #리스트 만들기
        for j in range(i,k): #자신부터 오른쪽 원소들과 교환
            lst[i], lst[j] = lst[j], lst[i]
            bbg(i+1,k)
            lst[i],lst[j] = lst[j],lst[i] #원래대로


T = int(input())
for tc in range(1,T+1):
    lst = list(map(int, input()))
    ans = 0
    bbg(0,len(lst))

    print(f'#{tc} {ans}')