class Solution(object):
    def distinctDifferenceArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            prefix=set(nums[:i+1])
            sufix=set(nums[i+1:])
            res.append(len(prefix)-len(sufix))
        return res