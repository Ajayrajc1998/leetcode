class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(reverse=True)
        for i in range(len(nums)):
            sub=nums[:i+1]
            if sum(sub)>sum(nums[i+1:]):
                return sub






        