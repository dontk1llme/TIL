# Tree_연습문제1: 전위순회 (제출용) D2

def preorder(root):
    try:
        print(root, end=' ')
        preorder(tree[root][0])
        preorder(tree[root][1])
    except: #안 하면 인덱스에러. 완전트리 아닌데 하나의 리스트에 노드를 받았기 때문에.
            # 나눠서 받았으면 그냥 if root로 해서 해도 됨
        return

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 정점의 개수
    lst = list(map(int, input().split()))

    #1번 정점이 root
    tree=[[] for _ in range(N)]
    for i in range(0,len(lst),2):
        a,b = lst[i], lst[i+1]
        tree[a].append(b)

    print(f'#{tc}', end= ' ')
    preorder(1)
    print()

#////////////////////// 나눠서 받은 경우 - 송준우 //////////////
def pre(T):
    if T:
        print(T, end=' ')
        pre(left[T])
        pre(right[T])


T = int(input())
for tc in range(1, T + 1):
    V = int(input())
    lst = list(map(int, input().split()))
    left = [0] * (V + 1)
    right = [0] * (V + 1)
    for i in range(V - 1):
        p = lst[i * 2]
        c = lst[i * 2 + 1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    print(f'#{tc}', end=' ')
    pre(1)

