# 14888 연산자 끼워넣기

n = int(input())
number = list(map(int, input().split())) #숫자
op = list(map(int, input().split())) #연산자
minR = int(1e9)
maxR = -int(1e9)

answer = number[0]

def dfs(idx):
    global answer
    global minR, maxR

    if idx == n: #인덱스값이 N과 같으면 최대, 최소 찾기
        if answer > maxR:
            maxR = answer
        if answer < minR:
            minR = answer
        return

    for i in range(4): #연산
        tmp = answer
        if op[i] > 0:
            if i == 0:
                answer += number[idx]
            elif i == 1:
                answer -= number[idx]
            elif i == 2:
                answer *= number[idx]
            else:
                if answer >= 0:
                    answer //= number[idx]
                else:
                    answer = (-answer // number[idx]) * -1

            op[i] -= 1
            dfs(idx+1)
            # 원래 상태로 돌려주기 (백트래킹)
            answer = tmp
            op[i] += 1

dfs(1)
print(maxR)
print(minR)