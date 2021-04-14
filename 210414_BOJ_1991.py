class Node:
    def __init__(self, item, leftNode, rightNode):
        self.item = item
        self.leftNode = leftNode
        self.rightNode = rightNode


def preorder(node):
    print(node.item, end='')
    if node.leftNode != '.':
        preorder(tree[node.leftNode])
    if node.rightNode != '.':
        preorder(tree[node.rightNode])


def inorder(node):
    if node.leftNode != '.':
        inorder(tree[node.leftNode])
    print(node.item, end='')
    if node.rightNode != '.':
        inorder(tree[node.rightNode])


def postorder(node):
    if node.leftNode != '.':
        postorder(tree[node.leftNode])
    if node.rightNode != '.':
        postorder(tree[node.rightNode])
    print(node.item, end='')


n = int(input())
tree = {}

for _ in range(n):
    item, left, right = map(str, input().split())
    tree[item] = Node(item=item, leftNode=left, rightNode=right)

preorder(tree['A'])
print('')
inorder(tree['A'])
print('')
postorder(tree['A'])
