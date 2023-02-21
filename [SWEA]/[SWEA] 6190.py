# 6190. 정곤이의 단조 증가하는 수 D3

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = -1

    for i in range(N):
        for j in range(i+1,N):
            orgnum=lst[i]*lst[j]
            num = lst[i]*lst[j]
            numlst = [] #ai*aj 자릿수가 역순으로 저장돼 잇음... 10으로 나눈 나머지를 저장하니까
            if num >= 10:
                while num>0:
                    numlst.append(num%10)
                    num//=10

            for k in range(len(numlst)-1):
                if numlst[k]>=numlst[k+1]: #역순이니까 걍 앞에서부터 4321인지
                    if k+1==len(numlst)-1:
                        if orgnum >= ans:
                            ans = orgnum
                else: break

    print(f'#{tc} {ans}')