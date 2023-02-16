# 문제가 swea에 없음  https://qrlagusdn.tistory.com/80
# 퀵소트처럼 반반 나눠서 진행해야함.
# 홀수??

# 반반 나누는 함수
def devide(start,end):
    if start==end:  #한 명 남았다는 뜻
        return start

    a = devide(start, (start+end)//2)
    b = devide((start+end)//2+1, end) #앞에 나누고 +1 해서 홀수도 잘적용됨.
    return mjp(a,b) #가위바위보 ㄱㄱ

# 가위바위보 함수
def mjp(a,b):
    if card[a]==card[b]: return a #비김 -> 앞순서인 a가 먼저임
    elif card[a]-card[b]==1 or card[a]-card[b]==-2: return a #a가 이김
    else: return b


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split())) #1 가위 2 바위 3 보
    winner = devide(0, N-1) +1 #앞에건 인덱스번호고 1번부터 세니까 +1
    print(f'#{tc} {winner}')