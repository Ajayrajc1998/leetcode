class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                result=result+(nums[i]-nums[i+1])+1
                nums[i+1]=nums[i+1]+(nums[i]-nums[i+1])+1
        return result