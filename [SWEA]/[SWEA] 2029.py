# swea 2029. 몫과 나머지 출력하기 D1
num = int(input())
for i in range(1, num+1):
    a,b = map(int, input().split())
    print(f'#{i} {a//b} {a%b}')