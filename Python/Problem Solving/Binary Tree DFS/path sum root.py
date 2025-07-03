# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path_sum_root(self, root, target_sum, two_paths=False):
        def _path_sum_root(root, curr_sum):
            if not root:
                return False
            curr_sum += root.value
            if not root.left and not root.right:
                return curr_sum == target_sum
            
            return _path_sum_root(root.left, curr_sum) or _path_sum_root(root.right, curr_sum)
        
        if not root:
            return False
        
        if two_paths:
            left =_path_sum_root(root.left, root.value) 
            right = _path_sum_root(root.right, root.value)
            return left and right 
        else:
            return _path_sum_root(root, 0)

    def path_sum_root(self, root, target_sum, two_paths=False):
        if not root:
            return False
        if not root.left and not root.right:
            return root.value == target_sum
        remaining = target_sum - root.value
        
        if two_paths:
            return self.path_sum_root(root.left, remaining) and self.path_sum_root(root.right, remaining)
        else:
            return self.path_sum_root(root.left, remaining) or self.path_sum_root(root.right, remaining)
    
