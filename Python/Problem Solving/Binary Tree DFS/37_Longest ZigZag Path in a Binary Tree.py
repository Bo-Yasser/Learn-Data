# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longest_zigzag(self, root):
        def dfs(node, isleft, depth):
            if not node:
                return depth

            if isleft:
                depth = max(
                    depth,
                    dfs(node.right, False, depth + 1),
                    dfs(node.left, True, 0)
                )


            else:
                depth = max(
                    depth,
                    dfs(node.left, True, depth + 1),
                    dfs(node.right, False, 0)
                )
            
            return depth
        
        return max(dfs(root.left, True, 0), dfs(root.right, False, 0))

    def longest_zigzag(self, root):
        
        longest_path=0
        def _longest_zigzag(node, curr_path, prev_direction):
            nonlocal longest_path
            if not node:
                return 0

            longest_path = max(curr_path, longest_path)
            if node.left:
                if prev_direction == "right":
                    _longest_zigzag(node.left, curr_path+1, "left")

                else:
                    _longest_zigzag(node.left, 1, "left")
            
            if node.right:
                if prev_direction == "left":
                    _longest_zigzag(node.right, curr_path+1, "right")

                else:
                    _longest_zigzag(node.right, 1, "right")
            
            return longest_path
        
        return _longest_zigzag(root, 0, None)