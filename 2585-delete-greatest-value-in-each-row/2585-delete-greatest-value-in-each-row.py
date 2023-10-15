class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        i=0
        res=0
        while grid!=[[] for _ in range(len(grid))]:
           gp=[]
           while i<len(grid):
               gp.append(max(grid[i]))
               grid[i].remove(max(grid[i]))
               i+=1
           res+=max(gp)
           i=0
        return res      