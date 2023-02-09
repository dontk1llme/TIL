# [BAEKJOON] 10994 별 찍기 - 19
# https://ansohxxn.github.io/boj/10994/
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=kckyoung2&logNo=221040753895
# https://m.blog.naver.com/repeater1384/222094535029



# line이 홀수일 때와 짝수일 때의 규칙이 다름.
# 홀수: 인덱스 1, -2 -> 1,3,-4,-2 이렇게 바꾸면서 출력.
#       근데 줄도 마찬가지.로... 0,-1 / 2,-3 이렇게 

N = int(input())
# line = 1+4*(N-1) # 얘를 함수 안에 넣어 놔야 계속 갱신 가능함. 아니면 인덱스에러. 밑에 넣어둠
star = [[' ']*(1+4*(N-1)) for _ in range(1+4*(N-1))] #나와야 되는 만큼 배열 만들기

def starf(N,x,y):
    if N == 1:
        star[y][x]= '*' 
        return #함수탈출
    line = 1+4*(N-1) #이거 찾아낸 게 진짜 다행임 ;; 
                     
    for i in range(line):
        star[y][x+i]='*' #상
        star[y+i][x]='*' #좌
        star[y+line-1][x+i]='*' #하
        star[y+i][x+line-1]='*' #우
    starf(N-1, x+2, y+2) #두 칸 안에 다시 시작하니까!

starf(N, 0, 0) #(0,0): 시작 좌표.
for i in star:
    print(''.join(i))












# 줄 기준이 아니라 상하좌우 기준으로 풀어도 됨.
# 좌표도 찍엇음.
# star = [[' ']*(line) for _ in range(line)]
# def star(N,x,y):
#     if N == 1:
#         star[y][x]= '*'
#         return
    

#     #출력
#     for i in range(line):
#         for j in range(line):
#             print(star[i][j], end='')
#         print()

# while N>0:
#     if N%2==1:
#         print('*')*N
#     else: 
#         print('*', ' '*N, '*')
#         print()
