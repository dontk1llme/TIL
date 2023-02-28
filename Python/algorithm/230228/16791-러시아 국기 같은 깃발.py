# 러시아 국기 같은 깃발 (제출용) D3
# 첫줄 흰줄, 마지막줄 빨간줄
# 흰->파: 개수 세서 적게 바꿔야 되면 파. 파 1줄 나왓으면 빨간줄로 갈 때도 마찬가지로
# W -> B -> R
# DFS!!!!를 왜 하지를 못하니? 근데 for문으로도 가능은 함
# 모든 경우의 수 찾아 주면 되는데 귀찮아서 안햇음..


T = int(input())
for tc in range(1, T+1):
    #입력
    N,M = map(int, input().split())
    lst = [list(input()) for _ in range(N)]

    #화이트 레드 블루로 바꾸려면 몇 번 바꿔야 하는지 배열에 저장
    cntlst=[]
    for row in lst:
        w = M-row.count('W')
        b = M-row.count('B')
        r = M-row.count('R')
        cntlst.append([w,b,r])

    ans=99999999
    # w,r은 0부터, b는 최소 1부터
    for w in range(0, N-3+1):
        for b in range(1, N-2+1-w):
            r = N-w-b-2
            #정해진 라인 수만큼 자신의 색깔로 바꾸는 카운트 세기
            cnt=0
            for i in range(w):
                cnt+=cntlst[1:-1][i][0]
            for j in range(w,w+b):
                cnt+=cntlst[1:-1][j][1]
            for k in range(w+b, w+b+r):
                cnt+=cntlst[1:-1][k][2]

            ans = min(ans,cnt)
    ans+=cntlst[0][0]+cntlst[-1][2]

    print(f'#{tc} {ans}')

 # # B가 k번째 줄에 나오는지, W가 몇 번째 줄에 나오는지...
 #    now = 0  # 0이면 W->B, 1이면 B->R
 #
 #    for i in range(1, N - 1):
 #        cW = cntlst[i][1] + cntlst[i][2]
 #        cB = cntlst[i][0] + cntlst[i][2]
 #        cR = cntlst[i][0] + cntlst[i][1]
 #        ncW = cntlst[i + 1][1] + cntlst[i + 1][2]
 #        ncB = cntlst[i + 1][0] + cntlst[i + 1][2]
 #        ncR = cntlst[i + 1][0] + cntlst[i + 1][1]
 #        if now == 0:
 #            if cW > cB:
 #                totalcnt += cB
 #            else:  # B가 한줄이상 있어야 되니까 같으면 그냥 일단 B해봐 -> 안되네..
 #                totalcnt += cW
 #                now = 1
 #        elif now == 1:
 #            if cR > cB:
 #                totalcnt += cB
 #            else:
 #                totalcnt += cR
 #                now = 1
 #    totalcnt = 0
 #    cntlst = [[0] * 3 for _ in range(N)]  # W, B, R
 #    for i in range(N): #첫줄, 막줄 개수 / WBR 개수 세기
 #        for j in range(M):
 #            if i==0: #첫줄
 #                if lst[i][j] != 'W':
 #                    totalcnt+=1
 #            elif i==(N-1): #막줄
 #                if lst[i][j] != 'R':
 #                    totalcnt += 1