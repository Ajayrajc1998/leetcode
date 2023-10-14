class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        mat=[[0 for _ in range(n)] for _ in range(m)]
        for i in indices:
            for j in range(len(mat[i[0]])):
                mat[i[0]][j]+=1
            for k in range(len(mat)):
                mat[k][i[1]]+=1
        count=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]%2==1:
                    count+=1
        return count