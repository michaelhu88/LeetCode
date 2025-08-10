# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxi = [-math.inf]

        if not root:
            return 0

        def dfs(node, depth):
            if not node:
                return
            maxi[0] = max(depth, maxi[0])
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            return

        dfs(root, 1)
        return maxi[0]
