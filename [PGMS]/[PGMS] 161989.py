# PGMS 161989 덧칠하기
from collections import deque 
def solution(n, m, section):
    dq=deque(section)
    cnt=1
    # section[0]부터 m의 롤러의 길이만큼 벽을 칠함
    flag=section[0]+m-1
    
    while dq:
        # flag보다 작으면 dq.pop()
        if dq[0]<=flag:
            dq.popleft()
        #아닐경우 falg 재지정
        else:
            cnt+=1
            flag=dq[0]+m-1
    return cnt