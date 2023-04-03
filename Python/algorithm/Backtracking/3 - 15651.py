# 15651
# 2번에서 중복 가능, 사전 증가 순으로 출력
# 사전 증가 순 신경 안 쓰고 1번에서 if문만 빼줘도 괜찮음

def dfs():
    if len(tmp)==M:
        # if tmp not in ans:
            # ans.append(tmp)
        print(' '.join(map(str, tmp)))
        return


    for i in range(1, N+1):
        tmp.append(i)
        dfs()
        tmp.pop()


N,M = map(int, input().split())
tmp = []
# ans = []
dfs()
# sorted(ans)
# for i in range(len(ans)):
#     print(' '.join(map(str, ans[i])))

#//////////////////////////////


