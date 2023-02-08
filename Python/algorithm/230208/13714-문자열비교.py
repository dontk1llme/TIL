T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    ans = 0
    start = 0

    for i in range(0, len(str2)-len(str1)+1):
        if str2[start:start+len(str1)] == str1:
            ans=1
        start+=1

    print(f'#{tc} {ans}')