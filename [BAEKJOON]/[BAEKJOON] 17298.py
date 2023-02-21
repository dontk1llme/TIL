# boj 17298 오큰수

N = int(input())
lst = list(map(int, input().split()))
nge = [-1] * N #답 저장할 리스트
stk = []

stk.append(0) #처음 검사할 인덱스
for i in range(1,N):
    while stk and lst[stk[-1]]<lst[i]:
        nge[stk.pop()] = lst[i]
    stk.append(i)
print(*nge)


# 시간초과 니먼ㄴ데 (38%) -> for문 2번 쓰면 O(N^2)여서 시간초과. 한번만 돌리는 방법 찾아야함 -> 스택
# https://hongcoding.tistory.com/40
# for i in range(N):
#     for j in range(i,N):
#         if lst[i]<lst[j]: #큰애 나오면 걍 리스트에 넣어주고 바로 종료
#             nge[i]=lst[j]
#             break
