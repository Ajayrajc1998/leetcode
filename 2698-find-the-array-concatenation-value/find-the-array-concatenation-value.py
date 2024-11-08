class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        while len(nums)>1:
            left=nums.pop(0)
            right=nums.pop()
            c_num=str(left)+str(right)
            res+=int(c_num)
        if len(nums)==1:
            res+=nums[0]
        return res

        


