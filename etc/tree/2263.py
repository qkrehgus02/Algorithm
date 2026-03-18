import sys
sys.setrecursionlimit(300000)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

tree = [[-1 for _ in range(2)] for _ in range(n+1)]
inorder_idx = {v: i for i, v in enumerate(inorder)}

def find_tree(il, ir, pl, pr):

    if il > ir or pl > pr:
        return -1

    node = postorder[pr]
    point = inorder_idx[node]
    
    tree[node][0] = find_tree(il, point -1 , pl, pl + point - il - 1) #왼쪽 서브트리
    tree[node][1] = find_tree(point + 1, ir, pl + point - il, pr - 1) #오른쪽 서브트리
    
    return node

def preorder(tree, root):
    print(root, end = " ")
    if tree[root][0] != -1:
        preorder(tree, tree[root][0])
    if tree[root][1] != -1:
        preorder(tree, tree[root][1])

root = find_tree(0, n-1, 0, n-1)
preorder(tree, root)
