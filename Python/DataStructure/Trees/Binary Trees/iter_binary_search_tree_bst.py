import sys
sys.path.append("h:/Programing/Python/DataStructure")

from Queue import linked_queue as lq
from Stack import linked_stack as st

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.__root = None
        self.__count = 0
    
    def __len__(self):
        return self.__count
    
    def add(self, value):
        new_node = Node(value) 
        
        if self.__root == None:
            self.__root = new_node
            self.__count += 1  
            return

        current = self.__root
        parent = None 
        while current != None:
            parent = current
            if value < current.item:
                current = current.left
            else:
                current = current.right
       
        if  value < parent.item:
            parent.left = new_node
        else:
            parent.right = new_node
        self.__count += 1

    def in_order(self):
        current = self.__root
        stack = st.LinkedStack()
        result = []

        while current or not stack.is_empty():
            while current:
                stack.push(current)
                current = current.left

            current = stack.pop()
            result.append(current.item)  
            current = current.right
        return result

    def pre_order(self):
        current = self.__root
        if current is None:
            return []
        
        stack = st.LinkedStack()
        stack.push(current)
        result = []
        while stack:
            current = stack.pop()
            result.append(current.item)

            if current.right:
                stack.push(current.right)
            
            if current.left:
                stack.push(current.left)
    
        return result
    
    ## 2 ##
    # def pre_order(self):
    #     current = self.__root
    #     stack = st.LinkedStack()  

    #     while current or stack:
    #         while current:
    #             print(current.item, end=" ")  
    #             stack.push(current)
    #             current = current.left

    #         current = stack.pop()
    #         current = current.right
    
    def post_order(self):
        current = self.__root
        if current is None:
            return []
        
        stack = st.LinkedStack() 
        result = []
        last_visited = None
        
        while stack or current:
            while current:
                stack.push(current)
                current = current.left

            current = stack.top()

            if current.right is None or current.right == last_visited:
                result.append(current.item)
                last_visited = current
                stack.pop()
                current = None
            else:
                current = current.right

        return result
            
    def level_order(self):
        def _level_order(root):
            if root is None:
                return
            
            queue = lq.LinkedQueue()
            queue.enqueue(root)
            
            while not queue.is_empty():
                current = queue.dequeue()
                print(current.item, end= " ")
                if current.left:
                    queue.enqueue(current.left)
                if current.right:
                    queue.enqueue(current.right)
        _level_order(self.__root)

    def max(self):
        if self.is_empty():
            raise IndexError("Tree is Empty")
        current = self.__root
        while current.right:
            current = current.right

        return current.item
    
    def min(self):
        if self.is_empty():
            raise IndexError("Tree is Empty")
        current = self.__root
        while current.left:
            current = current.left

        return current.item
    
    def inorder_successor(self, value):
        successor = None
        current = self.__root
        while current:
            
            if value < current.item:
                successor = current
                current = current.left
            else:
                current = current.right
        
        return successor.item if successor else None
    
    def inorder_predecessor(self, value):
        successor = None
        current = self.__root
        while current:
            
            if value > current.item:
                successor = current
                current = current.right
            else:
                current = current.left
        
        
        return successor.item if successor else None

    def is_empty(self):
        return self.__count == 0       
    

b = BST()



b.add(10)
b.add(8)
b.add(12)
b.add(9)
b.add(7)
b.add(11)
b.add(40)

print(b.post_order())

# print(b.max())
# print(b.min())
# print(b.inorder_successor(8))

