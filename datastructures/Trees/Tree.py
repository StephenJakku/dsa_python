from datastructures.Queue.Queue import Queue

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class Tree:
    def __init__(self,value):
        self.root=Node(value)

    def preorder(self):
        res=[]
        def traverse(node):
            if not node:
                return
            res.append(node.value)
            traverse(node.left)
            traverse(node.right)
        traverse(self.root)
        return res

    def inorder(self):
        res=[]
        def traverse(node):
            if not node:
                return

            traverse(node.left)
            res.append(node.value)
            traverse(node.right)
        traverse(self.root)
        return res

    def postorder(self):
        res = []

        def traverse(node):
            if not node:
                return

            traverse(node.left)

            traverse(node.right)
            res.append(node.value)
        traverse(self.root)
        return res

    def levelorder(self):
        res=[]
        q=Queue()
        q.enqueue(self.root)
        while not q.isEmpty():
            res.append(q.peek())
            node = q.dequeue()
            if (node.left):
                q.enqueue(node.left)
            if (node.right):
                q.enqueue(node.right)
        return res





tree=Tree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)

print(tree.preorder())
print(tree.inorder())
print(tree.postorder())
print(tree.inorder())

