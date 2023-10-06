class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        res=0
        for i in range(len(mat)):
            res+=mat[i][i]
            if i!=len(mat)-1-i:
                res+=mat[i][len(mat)-1-i]
        return res