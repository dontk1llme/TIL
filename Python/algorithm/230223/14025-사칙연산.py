#  [S/W 문제해결 기본] 9일차 - 사칙연산 (제출용) D4

#계산함수
def postord(n):
    if tree[n]: #노드가 존재하면
        if tree[n]=='+':
            return postord(ch1[n])+postord(ch2[n])
        elif tree[n]=='*':
            return postord(ch1[n])*postord(ch2[n])
        elif tree[n]=='-':
            return postord(ch1[n])-postord(ch2[n])
        elif tree[n]=='/':
            return postord(ch1[n])//postord(ch2[n])
        else: #연산자가 아닌 문자열(숫자)인 경우
            return int(tree[n])
    else: return 0

for tc in range(10):
    N = int(input()) #트리가 갖는 정점의 총 수
    # 저장 (완전이진트리 아님)
    tree, ch1, ch2 = [[0]*(N+1) for _ in range(3)]
    for _ in range(N):
        tlst = input().split()
        idx = int(tlst[0]) #노드번호
        tree[idx] = tlst[1] #연산자 또는 숫자(str)
        if len(tlst)>2:
            ch1[idx] = int(tlst[2])
            ch2[idx] = int(tlst[3])
    ans = postord(1)
    print(f'#{tc} {ans}')