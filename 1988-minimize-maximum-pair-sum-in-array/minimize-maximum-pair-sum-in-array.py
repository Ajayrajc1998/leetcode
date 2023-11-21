class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res=[]
        i=0
        while i<len(nums)//2:
            res.append(nums[i]+nums[len(nums)-1-i])
            i+=1
        return max(res)