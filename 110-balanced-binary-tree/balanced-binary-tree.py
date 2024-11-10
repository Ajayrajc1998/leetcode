# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def maxDepth(self,root):
        if root is None:
            return 0
        
        l_depth=self.maxDepth(root.left) if root.left else 0
        r_depth=self.maxDepth(root.right) if root.right else 0

        return max(l_depth,r_depth)+1

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True

        l_depth=self.maxDepth(root.left) if root.left else 0
        r_depth=self.maxDepth(root.right) if root.right else 0

        if(abs(l_depth-r_depth)<=1):
            left_balance=self.isBalanced(root.left) if root.left else True
            right_balance=self.isBalanced(root.right) if root.right else True
            if left_balance and right_balance:
                return True
        return False