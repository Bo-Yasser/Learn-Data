
import sys
sys.path.append("h:/Programing/Python/DataStructure")




from Queue import linked_queue as lq

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.value, end=" ")
            self.in_order(root.right)

    
    def pre_order(self, root):
        if root:
            print(root.value, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.value, end=" ")

    def level_order(self, root):
        if root is None:
            return
        
        queue = lq.LinkedQueue()
        queue.enqueue(root)
        
        while not queue.is_empty():
            current = queue.dequeue()
            print(current.value)

            if current.left:
                queue.enqueue(current.left)

            if current.right:
                queue.enqueue(current.right)



tree = BinaryTree("A")
tree.root.left = Node("B")
tree.root.right = Node("C")
tree.root.left.left = Node("D")
tree.root.left.right = Node("E")
tree.root.right.left = Node("F")


tree.post_order(tree.root)