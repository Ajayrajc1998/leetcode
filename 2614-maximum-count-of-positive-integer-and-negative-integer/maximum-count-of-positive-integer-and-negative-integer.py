class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p_count=0
        n_count=0
        for i in nums:
            if i<0:
                n_count+=1
            else:
                if i!=0:
                    p_count+=1
        
        return p_count if p_count>n_count else n_count