#BOJ 1913 달팽이
# https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-1913-%EB%8B%AC%ED%8C%BD%EC%9D%B4-Brute-Force
# https://simsim231.tistory.com/m/179


N = int(input()) #홀수인 자연수
M = int(input()) #위치를 찾고자 하는 N2 이하의 자연수

arr = [[0]*N for _ in range(N)] #빈 표 만들기
num = list(range(1,N*N+1))

def snail(N):
    right = 1
    nmj = 2
    x = N // 2  # 시작 좌표 잡아주기
    y = N // 2  # 시작 좌표 잡아주기

    arr[x][y]=num[0] #일단 첨값은 넣어줌. 1
    i=1 #num 인덱스 1부터 시작하려고...

    while i<len(num):
        x-=1  # 새로 시작할 땐 무조건 1칸
        # 왜 x가 -1까지 감? -> while i<=len 해서. i<len 하니까 됨
        arr[x][y]=num[i]
        i+=1

        for r in range(right): # 우로 갈 땐 1->3->5 (1번)
            y+=1
            arr[x][y]=num[i]
            i+=1
        right+=2
        for n in range(nmj): # 하,좌,상으로 갈 땐  2->4->6 (3번)
            x+=1            # 하
            arr[x][y]=num[i]
            i+=1
        for m in range(nmj): # 하,좌,상으로 갈 땐  2->4->6 (3번)
            y-=1            #좌
            arr[x][y]=num[i]
            i+=1
        for j in range(nmj): # 하,좌,상으로 갈 땐  2->4->6 (3번)
            x-=1            #상
            arr[x][y]=num[i]
            i+=1
        nmj+=2
    
snail(N)

#M의 인덱스 출력용...
idxx=0
idxy=0

for i in arr: #요소 전부 출력.............
    for j in i:
        print(j, end=' ')
        if j == M:#M 인덱스 주기...
            idxx = arr.index(i) +1 #+1: 인덱스가 아니라 눈으로 보이는 좌표
            idxy = i.index(j) +1
    print()

print(f'{idxx} {idxy}')