class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=[i for i in nums if i>0]
        n=[i for i in nums if i<0]
        i=0
        j=0
        res=[]
        while i<len(p) or j<len(n):
            res.append(p[i])
            res.append(n[j])
            i+=1
            j+=1
        return res
        