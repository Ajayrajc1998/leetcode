class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = set()
        nums.sort()
        
        left=0
        right=len(nums)-1
        while left<right:
            a=float(nums[left])
            b=float(nums[right])
            res.add((a+b)/2)
            left+=1
            right-=1
            

         
        return len(res)
