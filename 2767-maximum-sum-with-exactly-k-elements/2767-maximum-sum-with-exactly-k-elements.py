class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res=0
        nums.sort()
        while k!=0:
            a=nums.pop()
            res+=a
            nums.append(a+1)
            k-=1
        return res
