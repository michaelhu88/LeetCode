class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        if p.val != q.val:
            return False
        
        left_subtree = self.isSameTree(p.left, q.left)
        right_subtree = self.isSameTree(p.right, q.right)

        if not left_subtree or not right_subtree:
            return False
        return True