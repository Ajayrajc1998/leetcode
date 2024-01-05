class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        while True:
            nums=[(nums[i]+nums[i+1]) % 10 for i in range(len(nums)-1)]
            if len(nums)==1:
                return nums[0]