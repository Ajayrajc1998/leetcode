class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)<3:
            return -1
        count=0
        min_element=nums[0]
        max_element=nums[-1]
        for i in nums:
            if i!=min_element:
                return i
    