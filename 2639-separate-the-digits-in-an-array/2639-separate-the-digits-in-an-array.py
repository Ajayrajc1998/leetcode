class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            res.extend(list(str(nums[i])))
        res=[int(i) for i in res]
        return res
