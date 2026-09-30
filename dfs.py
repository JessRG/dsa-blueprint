# All Paths for a Sum
# Given a binary tree and a number S, find all paths from root-to-leaf such that the sum of all
# the node values of each path equals S.

# Example 1:
#          1
#        /   \
#      7      9
#     / \    / \
#    4   5  2   7
# S: 12
# Output: [[1, 7, 4], [1, 9, 2]]
# Explanation: Here are the two paths with sum '12':1 -> 7 -> 4 and 1 -> 9 -> 2

# Example 2:
#         12
#        /  \
#       7    1
#       |   / \
#       4  10  5
# S: 23
# Output: [[12, 7, 4], [12, 1, 10]]
# Explanation: Here are the two paths with sum '23':12 -> 7 -> 4 and 12 -> 1 -> 10

# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findPaths(root, required_sum):
    allPaths = []
    # TODO: Write your code here
    path = []

    def find(node, target):
        if node is None:
            return

        remaining = target - node.val
        path.append(node.val)

        if remaining == 0 and node.left is None and node.right is None:
            allPaths.append(path[:])
        else:
            # check the left and right subtrees
            find(node.left, remaining)
            find(node.right, remaining)

        path.pop()
        return

    find(root, required_sum)
    return allPaths

# [12,7,1,4,null,10,5]
# 23
root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)

left = root.left
left.left = TreeNode(4)

right = root.right
right.left = TreeNode(10)
right.right = TreeNode(5)

print(findPaths(root, 23))