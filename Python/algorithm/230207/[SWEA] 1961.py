T = int(input())

# 90도 회전하는 함수
def rotation(a, N):
    new_arr = [[0] * N for _ in range(N)]  # NxN 빈 배열 먼저 만들기
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = a[N-1-j][i]
    return new_arr

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rot_90 = rotation(arr, N)
    rot_180 = rotation(rot_90, N)
    rot_270 = rotation(rot_180, N)

    print("#{}".format(tc))
    for i in range(N):
        print("".join(map(str, rot_90[i])), end=" ")
        print("".join(map(str, rot_180[i])), end=" ")
        print("".join(map(str, rot_270[i])), end=" ")
        print()

#-----------------------------
# 같은 코드인 것 같은데 왜 위는 되고 아래는 안 되는?

# T = int(input())

# #90도 회전하는 함수
# def rotation(a,N):
#     newarr=[[0]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             newarr[i][j]=a[N-1-j][i] #인덱스 생각 좀...
#     return newarr

# for t in range(1, T+1):
#     num = int(input())
#     # arr=[]
#     # for j in range(num):
#     #     arr.append(list(map(int, input().split()))) 이 세 줄을 아래 한 줄로
#     arr = [list(map(int, input().split())) for _ in range(num)]

#     #90, 180, 270
#     rot_90= rotation(arr, num)
#     rot_180= rotation(rot_90, num)
#     rot_270= rotation(rot_180, num)

#     print(f'#{t}')
#     for k in range(num):
#         print("".join(map(str, rot_90[t])), end=" ")
#         print("".join(map(str, rot_180[t])), end=" ")
#         print("".join(map(str, rot_270[t])), end=" ")
#         print()
    
