
import sys
sys.path.append("h:/Programing/Python/DataStructure")




from Queue import linked_queue as lq

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.value, end=" ")
            self.in_order(root.right)

    
    def pre_order(self, root):
        if root:
            print(root.value, end=" ")
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.value, end=" ")

    def level_order(self, root):
        if root is None:
            return
        
        queue = lq.LinkedQueue()
        queue.enqueue(root)
        
        while not queue.is_empty():
            current = queue.dequeue()
            print(current.value)

            if current.left:
                queue.enqueue(current.left)

            if current.right:
                queue.enqueue(current.right)

    def maxDepth(self, root):
        if not root:
            return -1
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

    
    def get_leaves(self, root):
        if not root:
            return []
        
        if not root.left and not root.right:
            return [root.value]
        
        return self.get_leaves(root.left) + self.get_leaves(root.right)

    def leafSimilar(self, root1, root2):
        return self.get_leaves(root1) == self.get_leaves(root2)

    # same thing and same efficiency but other way     
    # def leafSimilar(self, root1, root2):
    #     def get_leaves(root, tree):
    #         if not root:
    #             return
            
    #         if not root.left and not root.right:
    #             tree.append(root.value)
    #             return
    #         get_leaves(root.left, tree)
    #         get_leaves(root.right, tree)

    #     tree_one = []
    #     tree_two = []
    #     get_leaves(root1, tree_one)
    #     get_leaves(root2, tree_two)

    #     return tree_one == tree_two
        
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
    
    def count_node_repeat(self, node, target):
        if not node:
            return 0
        
        count = 1 if node.value == target else 0

        count += self.count_node_repeat(node.left, target)
        count += self.count_node_repeat(node.right, target)

        return count

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
    

    def longest_zigzag(self, root):
        def dfs(node, isleft, depth):
            if not node:
                return depth

            if isleft:
                depth = max(depth,dfs(node.right, False, depth + 1), dfs(node.left, True, 0))


            else:
                depth = max(
                    depth,
                    dfs(node.left, True, depth + 1),
                    dfs(node.right, False, 0)
                )
            
            return depth
        
        return max(dfs(root.left, True, 0), dfs(root.right, False, 0))
    

    
tree = BinaryTree(20)
tree.root.left = Node(15)
tree.root.left.right = Node(15)
tree.root.left.right.left = Node(3)
# tree.root.left.right.right = Node(3)

# tree.root.right = Node(18)
# tree.root.right.right = Node(12)
# tree.root.right.left = Node(1)
# tree.root.right.left.right = Node(10)


# tree.root.right.left = Node("F")
# tree2 = BinaryTree("A")
# tree2.root.left = Node("B")
# tree2.root.right = Node("C")
# tree2.root.left.left = Node("D")


# print(f"\n{tree.maxDepth(tree.root)}")

# tree.level_order(tree.root)

# print(tree.leafSimilar(tree.root, tree2.root))

# print(tree.goodNodes(tree.root))


# print(tree.count_node(tree.root, 4))


print(tree.longest_zigzag(tree.root))

