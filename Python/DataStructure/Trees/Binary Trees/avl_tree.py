import sys
sys.path.append("h:/Programing/Python/DataStructure")

from Queue import linked_queue as lq
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL:

    def __init__(self):
        self.__root = None
        self.__count = 0
    
    def __len__(self):
        return self.__count
    
    def __str__(self):
        return f"{list(self.level_order())}"
    
    def __bool__(self):
        return not self.is_empty()
    
    def __iter__(self):
        def _in_order(root):
            if root:
                yield from _in_order(root.left)
                yield root.value
                yield from _in_order(root.right)
        
        return _in_order(self.__root)
    
    def add(self, value):
        
        def _add(current, value):
            if not current:
                return Node(value)
            
            if value < current.value:
                current.left = _add(current.left, value)
            
            else:
                current.right = _add(current.right, value)

            current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))

            balance = self.get_balance(current)

            # LL
            if balance > 1 and value < current.left.value:
                return self.right_rotate(current)
            
            # RR
            if balance < -1 and value > current.right.value:
                return self.left_rotate(current)
            
            # LR
            if balance > 1 and value > current.left.value:
                current.left = self.left_rotate(current.left)
                return self.right_rotate(current)
            
            # RL
            if balance < -1 and value < current.right.value:
                current.right = self.right_rotate(current.right)
                return self.left_rotate(current)
            
            return current



        self.__root = _add(self.__root, value)
        self.__count += 1
            
    
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    
    def right_rotate(self, z):
        y = z.left
        t3 = y.right

        y.right = z
        z.left = t3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
    
    def left_rotate(self, z):
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2
        
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    
    def delete(self, value):
        if self.is_empty():
            raise IndexError("Tree is Empty")
        def _delete(current, value):
            if current is None:
                raise ValueError("Value not Found!")
            
            elif value < current.value:
                current.left = _delete(current.left, value)

            elif value > current.value:
                current.right = _delete(current.right, value)

            else:
                if not current.left and not current.right:
                    self.__count -= 1
                    return None
            
                elif current.right is None:
                    self.__count -= 1
                    return current.left

                elif current.left is None:
                    self.__count -= 1
                    return current.right

                else:
                    succesor = self.min(current.right)
                    current.value = succesor
                    current.right = _delete(current.right, succesor)

            current.height = 1 + max(self.get_height(current.left), self.get_height(current.right)) 
            
            balance = self.get_balance(current)
            
            # LL
            if balance > 1 and self.get_balance(current.left) >= 0:
                return self.right_rotate(current)
            
            # LR
            if balance > 1 and self.get_balance(current.left) < 0:
                current.left = self.left_rotate(current.left)
                return self.right_rotate(current)
            
            # RR
            if balance < -1 and self.get_balance(current.right) <= 0:
                return self.left_rotate(current)
            
            # RL
            if balance < -1 and self.get_balance(current.right) > 0:
                current.right = self.right_rotate(current.right)
                return self.left_rotate(current)
            
            return current

        self.__root = _delete(self.__root, value) 
        

    def in_order(self):
        def _in_order(root):
            if root:
                _in_order(root.left)
                print(root.value, end=" ")
                _in_order(root.right)
        _in_order(self.__root)

    
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

    def level_order(self):
        def _level_order(root):
            if root is None:
                return []
            
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

    def inorder_successor(self, value):
        if not self.is_found(value):
            raise ValueError("Value Not found")
        
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
        if not self.is_found(value):
            raise ValueError("Value Not found")
        
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
    
    def is_balanced(self):
        def _check(node):
            if not node:
                return True
            
            balance = self.get_balance(node)
            if balance > 1 or balance < -1:
                return False
            return _check(node.left) and _check(node.right)

        return _check(self.__root) 
    
    def is_empty(self):
        return self.__count == 0   

    def clear(self):
        self.__root = None
        self.__count = 0
    
    def depth(self, value=None):
        if self.__count == 0:
            return -1
        
        def _depth(root, depth):
            if not root:
                return -1
            
            if root.value == value:
                return depth
            
            left_depth = _depth(root.left, depth + 1)
            right_depth = _depth(root.right, depth + 1)

            if left_depth != -1:
                return left_depth

            if right_depth != -1:
                return right_depth
            
            return -1
        
        if value is None:
            return self.height(self.__root.value)
        
        return _depth(self.__root, 0)

            
    def get_leaves(self, tree=None):
        
        def _get_leaves(root):
            if not root:
                return []
            
            if not root.left and not root.right:
                return [root.value]
            
            return _get_leaves(root.left) + _get_leaves(root.right)

        if tree:
            return _get_leaves(tree.__root)
        
        return _get_leaves(self.__root)

    def leafSimilar(self, root1, root2):
        return self.get_leaves(root1) == self.get_leaves(root2)

b = AVL()



b.add(13)
b.add(11)
b.add(15)
b.add(12)
b.add(10)
b.add(6)

b.delete(6)
# b.delete(7)
print(b.level_order())

print(b.is_balanced())
