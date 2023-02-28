# BOJ 1991 트리 순회

#전위순회
def preord(root):
    if root!='.':
        print(root, end='')
        preord(tree[root][0])
        preord(tree[root][1])

#중위순회
def inord(root):
    if root != '.':
        inord(tree[root][0])
        print(root, end='')
        inord(tree[root][1])

#후위순회
def postdrd(root):
    if root != '.':
        postdrd(tree[root][0])
        postdrd(tree[root][1])
        print(root, end='')


#입력
N = int(input())
tree = {} #딕셔너리 써야 입력받기 쉬움
for _ in range(N):
    n,l,r = input().split()
    tree[n] = [l,r] #바로 저장대죠?

preord('A')
print()
inord('A')
print()
postdrd('A')
