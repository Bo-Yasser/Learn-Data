# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowest_common_ansector(self, root, one, two):
        ancestor = None
        def dfs(node):
            nonlocal ancestor
            if not node:
                return False
                
            result = node.val == one or node.val == two
            
            left = dfs(node.left)
            right = dfs(node.right)

            if result + left + right >= 2:
                ancestor = node.val
                 

            return result or left or right

        dfs(root)
        return ancestor
    
    def lowest_common_ansector(self, root, one, two):
            if not root or root.value == one or root.value == two:
                return root
            
            left = self.lowest_common_ansector(root.left, one, two)
            right = self.lowest_common_ansector(root.right, one, two)

            if left and right:
                return root
            
            return left or right
            

