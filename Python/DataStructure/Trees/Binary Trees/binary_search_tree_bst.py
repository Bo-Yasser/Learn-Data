import sys
sys.path.append("h:/Programing/Python/DataStructure")
from Queue import linked_queue as lq

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.__root = None
        self.__count = 0
    
    def __len__(self):
        return self.__count
    
    def __str__(self):
        return f"[{self.level_order}]"

    def __contains__(self, value):
        return self.is_found(value)
    
    def __iter__(self):
        def _in_order(root):
            yield from _in_order(root.left)
            yield root.value
            yield from _in_order(root.right)
        
        return _in_order(self.__root)

    def add(self, value):
        
        def _add(current, value):
            if value <= current.value:
                if current.left == None:
                    current.left = Node(value)
                else:    
                    _add(current.left, value)
            
            else:
                if current.right == None:
                    current.right = Node(value)
                else:
                    _add(current.right, value)
        
        if self.__root == None:
            self.__root = Node(value)
        else:
            _add(self.__root, value)
        
        self.__count += 1
            
    def delete(self, value):
        if self.is_empty():
            raise IndexError("Tree is Empty")
        def _delete(current, value):
            if current is None:
                return current
            
            elif value < current.value:
                current.left = _delete(current.left, value)

            elif value > current.value:
                current.right = _delete(current.right, value)

            else:
                if not current.left and not current.right:
                    return None
            
                elif current.right is None:
                    return current.left

                elif current.left is None:
                    return current.right

                else:
                    succesor = self.min(current.right)
                    current.value = succesor
                    current.right = _delete(current.right, succesor)

            return current

        _delete(self.__root, value) 

    def pre_order(self):
        def _pre_order(root):
            if root:
                print(root.value, end=" ")
                _pre_order(root.left)
                _pre_order(root.right)
        _pre_order(self.__root)

    def post_order(self):
        def _post_order(root):
            if root:
                _post_order(root.left)
                _post_order(root.right)
                print(root.value, end=" ")
        _post_order(self.__root)

    def in_order(self):
        def _in_order(root):
            if root:
                _in_order(root.left)
                print(root.value, end=" ")
                _in_order(root.right)
        _in_order(self.__root)

    def level_order(self):
        def _level_order(root):
            if root is None:
                return
            
            queue = lq.LinkedQueue()
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
                

    def search(self, value):
        if self.is_empty():
            raise IndexError("Tree is Empty")
        def _search(current, value):
            if current is None:
                return None
            if current.value == value:
                return current
            elif value < current.value:
                return _search(current.left, value)
            else:
                return _search(current.right, value)
        return _search(self.__root, value)
    

    def is_found(self, value):
        if self.is_empty():
            raise IndexError("Tree is Empty")
        def _is_found(current, value):
            
            if current is None:
                return False 
            if current.value == value:
                return True 
            
            elif value < current.value:
                return _is_found(current.left, value)
            
            else:
                return _is_found(current.right, value)
        
        return _is_found(self.__root, value)
                

    def min(self, root=None):
        if self.is_empty():
            raise IndexError("Tree is Empty")

        def _min(root):
            if root.left:
                return _min(root.left)

            return root.value
        if root:
            return _min(root)
            
        return _min(self.__root)
    
    def max(self, root=None):
        if self.is_empty():
            raise IndexError("Tree is Empty")

        def _max(root):
            if root.right:
                return _max(root.right)
            return root.value
        if root:
            return _max(root)      
        
        return _max(self.__root)

    def height(self, value=None):
        if self.__count == 0:
            return -1

        def _height(root):
            if root is None:
                return -1
            
            left_subtree = _height(root.left)
            right_subtree = _height(root.right)
            
            return max(left_subtree, right_subtree) + 1
        
        if value is None:
            return _height(self.__root)
        else:
            node = self.search(value)
            if node is None:
                raise IndexError("Value Not found")
            return _height(node)

    def is_empty(self):
        return self.__count == 0      


    def inorder_successor(self, value):
        
        successor = None
        def _inorder_successor(root, value):
            nonlocal successor
            if root is None:
                return

            if value < root.value:
                successor = root.value
                _inorder_successor(root.left, value)
            elif value > root.value:
                _inorder_successor(root.right, value)
            else:
                if root.right:
                    successor = self.min(root.right)

        
        _inorder_successor(self.__root, value)
        
        return successor
        

    def inorder_predecessor(self, value):
        predecessor = None
        def _inorder_predecessor(root, value):
            nonlocal predecessor
            if root is None:
                return

            if value > root.value:
                predecessor = root.value
                _inorder_predecessor(root.right, value)
            elif value < root.value:
                _inorder_predecessor(root.left, value)
            
            else:
                if root.left:
                    predecessor = self.max(root.left)

            
        _inorder_predecessor(self.__root, value)
        return predecessor
                

            


b = BST()



b.add(13)
b.add(11)
b.add(15)
b.add(12)
b.add(10)
b.add(6)

# b.add(10)


# print(b.level_order())

# print(f"\n{len(b)}")

# print(b.search(10))

# print(b.min())



# b.delete(40)
# print(b.level_order())

# b.delete(9)
# print(b.level_order())


# b.delete(11)
b.in_order()

# print(b.inorder_successor(15))
print(b.inorder_predecessor(1))

# print(b.search(1))



