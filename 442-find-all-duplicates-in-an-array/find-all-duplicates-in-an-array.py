class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        res=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                res.append(i)
        return res