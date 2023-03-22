# boj 15954 인형들 - 카카오 어쩌구 문제
# K개 이상 완전탐색. pypy로 제출해야 함
# https://korinblog.tistory.com/3 설명 참고용 로직
# https://imksh.com/36 풀이
# https://www.acmicpc.net/board/view/29582 시간초과

import math

N, K = map(int, input().split())
lst = list(map(int, input().split())) #순서 고정임. 첨엔 sort 해야되는줄

#분산 반환하는 함수
def sd(ls):
    dis = 0
    avg = sum(ls)/len(ls) #평균
    for z in ls:
        dis+=(z-avg)**2
    return dis/len(ls) #분산

ans = list()
for i in range(N-K+1): #k개 이상: n-k
    for j in range(N-K-i+1): #해당 범위 리스트 보기
        tmp = lst[i:i+K+j]
        a = sd(tmp)
        ans.append(a)
print(math.sqrt(min(ans))) #표준편차 출력