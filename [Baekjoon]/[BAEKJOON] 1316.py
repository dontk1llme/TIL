#[BAEKJOON] 1316 그룹 단어 체커

n = int(input())
cnt=0
for i in range(n):
    str = input()
    arr=''
    for j in str:
        if j not in arr: arr+=j
        elif j == arr[-1]: arr+=j
        elif j != arr[-1]: pass

    if arr==str: cnt+=1

print(cnt)
