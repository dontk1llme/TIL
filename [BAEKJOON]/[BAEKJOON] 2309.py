# [BAEKJOON] 2309 일곱 난쟁이

lst = []
for _ in range(9):
    lst.append(int(input()))

realbreak = False
for i in range(9):
    for j in range(i+1,9):
        new = lst[:]
        del new[j]
        del new[i]
        if sum(new)==100:
            new = sorted(new)
            print(*new, sep='\n')
            realbreak = True
            break
    if realbreak==True:
        break