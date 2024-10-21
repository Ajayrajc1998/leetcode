class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        sq={i**2:i for i in range(1,n+1)}
        res=0
        for i in range(1,n+1):
            for j in range(i,n+1):
                if (j**2-i**2) in sq:
                    res+=1
        
        return res

