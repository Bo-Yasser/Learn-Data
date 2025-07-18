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
        return f"{list(self.level_order())}"

    def __contains__(self, value):
        return self.is_found(value)
    
    def __iter__(self):
        def _in_order(root):
            if root:
                yield from _in_order(root.left)
                yield root.value
                yield from _in_order(root.right)
        
        return _in_order(self.__root)


    def add(self, value):
        
        def _add(current, value):
            if value < current.value:
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

            return current

        self.__root = _delete(self.__root, value) 

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

# اختبار BST
bst = BST()
bst2 = BST()


# إضافة عناصر
bst.add(50)
bst.add(30)
bst.add(70)
bst.add(20)
bst.add(10)

bst2.add(50)
bst2.add(30)
bst2.add(70)
bst2.add(20)
bst2.add(10)
# bst.add(60)
# bst.add(80)

# الطباعة باستخدام طرق الترافيرسال
# print("In-Order Traversal:")
# bst.in_order()  # يجب أن يطبع 20 30 40 50 60 70 80
# print("\nPre-Order Traversal:")
# bst.pre_order()  # يجب أن يطبع 50 30 20 40 70 60 80
# print("\nPost-Order Traversal:")
# bst.post_order()  # يجب أن يطبع 20 40 30 60 80 70 50
# print("\nLevel-Order Traversal:")
# print(bst.level_order())  # يجب أن يطبع [50, 30, 70, 20, 40, 60, 80]

# # اختبار البحث
# print("\nSearch for 40:", bst.search(40))  # يجب أن يعيد العقدة التي تحتوي على 40
# print("Search for 100:", bst.search(100))  # يجب أن يعيد None أو يرفع استثناء

# # اختبار الحذف
# bst.delete(40)  # حذف العقدة 40
# print("\nIn-Order Traversal after deletion of 40:")
# bst.in_order()  # يجب أن يطبع 20 30 50 60 70 80

# # اختبار الاستبدال بالـ successor
# print("\nInorder Successor of 30:", bst.inorder_successor(30))  # يجب أن يعيد 50

# # اختبار الحذف بعد التعديل
# bst.delete(50)  # حذف الجذر
# print("\nIn-Order Traversal after deletion of root 50:")
# bst.in_order()  # يجب أن يطبع 20 30 60 70 80



print(bst.level_order())
# print(bst.get_leaves())
print(bst.leafSimilar(bst, bst2))