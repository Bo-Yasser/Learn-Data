# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root):
        count = 0
        def _goodNodes(node, max_value):
            nonlocal count
            if not node:
                return

            if node.val >= max_value:
                count += 1

            new_max = max(node.val, max_value)
            _goodNodes(node.left, new_max)
            _goodNodes(node.right, new_max)

        _goodNodes(root, float("-inf"))
        return count
        

    def goodNodes(self, root):
        def _goodNodes(root, max_value=float("-inf")):
            if not root:
                return 0

            count = 1 if root.value >= max_value else 0
            max_value = max(root.value, max_value)
            
            count += _goodNodes(root.left, max_value)
            count += _goodNodes(root.right, max_value)

            return count

        return _goodNodes(root)
    

