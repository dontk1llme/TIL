#https://velog.io/@ohk9134/%EB%B0%B1%EC%A4%80-1991%EB%B2%88-%ED%8A%B8%EB%A6%AC-%EC%88%9C%ED%9A%8C-python-%ED%8A%B8%EB%A6%AC-%EA%B5%AC%ED%98%84
#boj1991 기준

N = int(sys.stdin.readline().strip())
tree = {}

for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]
# 1. 전위 순회 : 루트 -> 왼쪽 자식 -> 오른쪽 자식이므로 재귀함수 순서도 root출력문 -> 왼쪽 재귀함수 -> 오른쪽 재귀함수

def preorder(root):  # 루트 -> 왼쪽 자식 -> 오른쪽 자식 순으로 탐색
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left -> left가 새로운 root가 된다.
        preorder(tree[root][1])  # right -> right가 새로운 root가 된다.


# 2. 중위 순회 : 왼쪽 자식 -> 루트 -> 오른쪽 자식이므로 재귀함수 순서도 왼쪽 재귀함수 -> root 출력문 -> 오른쪽 재귀함수

def inorder(root):  # 왼쪽 자식 -> 루트 -> 오른쪽 자식 순으로 탐색
    if root != '.':
        # TEST CASE를 예로 들면 B에서 tree[root][0] = "D"이고 D의 tree(root[0]) = "."이 돼서 root인 D를 출력하고 right로 넘어간다.
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right


# 3. 후위 순회 : 왼쪽 자식 -> 오른쪽 자식 -> 루트이므로 재귀함수 순서도 왼쪽 재귀함수 -> 오른쪽 재귀함수 -> root 출력문

def postorder(root):  # 왼쪽 자식 -> 오른쪽 자식 -> 루트 순으로 탐색
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root

