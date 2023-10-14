class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prod=0
        for i in range(len(nums)):
            if len(nums)%(i+1)==0 :
                prod+=nums[i]**2
        return prod