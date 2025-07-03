# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def path_sum(self, root, target_sum):
        if not root:
            return 0
        
        from_here = self.count_nodes(root, target_sum)
        
        left_count = self.path_sum(root.left, target_sum)
        right_count = self.path_sum(root.right, target_sum)

        return from_here + left_count + right_count

    def count_nodes(self, node, target_sum):
        if not node:
            return 0
        
        count = 0
        if node.value == target_sum:
            count = 1
        remaining = target_sum - node.value
        count += self.count_nodes(node.left, remaining)
        count += self.count_nodes(node.right, remaining)
        
        return count
    


    def path_sum_h(self, root, target_sum):
        prefix_sums = {0:1}

        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.value

            paths_found = prefix_sums.get(curr_sum - target_sum, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1

            paths_found += dfs(node.left, curr_sum)
            paths_found += dfs(node.right, curr_sum)

            prefix_sums[curr_sum] -= 1

            return paths_found
        
        return dfs(root, 0)
