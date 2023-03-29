# boj 1759 암호만들기 골5
# 백트래킹 기초문제 . . .
# 순서대로, 모음이 1개 이상, 자음이 2개 이상이라면 출력

cons = ['a','e','i','o','u'] #모음 리스트

def back(cnt, idx):
    if cnt==L: #암호를 만들었을 때
        vo, co = 0,0 #모음, 자음 개수 체크
        for i in range(L):
            if ans[i] in cons:
                vo+=1
            else:
                co+=1
        if vo>=1 and co>=2:
            # print("".join(ans))
            answer.append("".join(ans))
        return

    for i in range(idx, C):
        ans.append(lst[i])
        back(cnt+1, i+1) #백트래킹
        ans.pop()


L,C = map(int,input().split())
lst = sorted(list(map(str, input().split()))) #증가하는 순서로 배열->우선 정렬
ans = []
answer = []
back(0,0)

# 정답까지도 정렬해주어야 해서... 따로 리스트 만들어서 냄
answer.sort()
for i in range(len(answer)):
    print(answer[i])

