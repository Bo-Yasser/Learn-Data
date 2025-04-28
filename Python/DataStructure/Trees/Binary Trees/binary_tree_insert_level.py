import sys
sys.path.append("h:/Programing/Python/DataStructure")
from Queue.linked_queue import LinkedQueue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.__root = None
        self.__count = 0
    
    def __len__(self):
        return self.__count

    def insert_lev(self, value):
        new_node = Node(value)
        if self.__root is None:
            self.__root = new_node
            return
        queue = LinkedQueue()
        queue.enqueue(self.__root)

        while not queue.is_empty():
            current = queue.dequeue()
            if current.left is None:
                current.left = new_node
                return
            else:
                queue.enqueue(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.enqueue(current.right)

    def level_order(self):
        def _level_order(root):
            if root is None:
                return
            
            queue = LinkedQueue()
            queue.enqueue(root)
            l = []
            while not queue.is_empty():
                current = queue.dequeue()
                l.append(current.value)
                if current.left:
                    queue.enqueue(current.left)
                if current.right:
                    queue.enqueue(current.right)
            return l
        return _level_order(self.__root)
        


b = BinaryTree()

b.insert_lev(10)
b.insert_lev(8)
b.insert_lev(6)
b.insert_lev(5)
b.insert_lev(3)
b.insert_lev(1)
b.insert_lev(20)
b.insert_lev(30)




print(b.level_order())
