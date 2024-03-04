# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer=[]
        self.printInorder(root,answer)
        return answer

    
    def printInorder(self,node,answer):
        if node is None:
            return
        self.printInorder(node.left, answer)
        self.printInorder(node.right, answer)
        answer.append(node.val)