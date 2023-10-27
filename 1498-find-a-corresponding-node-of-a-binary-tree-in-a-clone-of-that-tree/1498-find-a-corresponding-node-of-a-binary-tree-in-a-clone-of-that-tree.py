# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        if cloned is None:
            return None
        if cloned.val==target.val:
            return cloned
        left_result=self.getTargetCopy(original, cloned.left, target)
        if left_result:
            return left_result
        right_result=self.getTargetCopy(original,cloned.right,target)
        if right_result:
            return right_result
        return None