# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    # first way
    def leafSimilar(self, root1, root2):
        def get_leaves(root, tree):
            if not root:
                return
            
            if not root.left and not root.right:
                tree.append(root.val)
                return
            get_leaves(root.left, tree)
            get_leaves(root.right, tree)

        tree_one = []
        tree_two = []
        get_leaves(root1, tree_one)
        get_leaves(root2, tree_two)

        return tree_one == tree_two
    
    # same thing and same efficiency but other way  
    # def get_leaves(self, root):
    #     if not root:
    #         return []
        
    #     if not root.left and not root.right:
    #         return [root.val]
        
    #     return self.get_leaves(root.left) + self.get_leaves(root.right)

    # def leafSimilar(self, root1, root2):
    #     return self.get_leaves(root1) == self.get_leaves(root2)