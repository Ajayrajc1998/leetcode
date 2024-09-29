class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums==sorted(nums):
            return True
        else:
            rotate=0
            while rotate<len(nums):
                val=nums.pop()
                nums.insert(0,val)
                if nums==sorted(nums):
                    return True
                rotate+=1
        
        return False
