T = int(input()) #test_case 수

for t in range(1, T + 1):
    N = int(input()) #전체 노선 수
    count = [0] * 1001
    for n in range(1, N + 1):
        each_bus = list(map(int, input().split()))
        if each_bus[0] == 1:
            while each_bus[1] != each_bus[2] + 1:
                count[each_bus[1]] += 1
                each_bus[1] += 1
        elif each_bus[0] == 2:
            while each_bus[1] < each_bus[2]:
                count[each_bus[1]] += 1
                each_bus[1] += 2
        else :
            if each_bus[1] % 2 == 0: #A가 짝수라면
                for i in range(each_bus[1], each_bus[2]+1):
                    if i % 4 == 0:
                        count[i] += 1
                    else :
                        pass
            else: #A가 홀수라면
                for j in range(each_bus[1], each_bus[2]+1):
                    if (j%3 == 0) and (j%10 != 0):
                        count[j] += 1
                    else:
                        pass
    print(count[:15])
    print(f'#{t} {max(count)}')