class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        factor=[i for i in range(1,n+1) if n%i==0]
        if k<=len(factor):
            return factor[k-1]
        else:
            return -1