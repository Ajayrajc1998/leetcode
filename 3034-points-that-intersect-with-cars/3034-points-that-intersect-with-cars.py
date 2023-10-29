class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        result=[]
        for i in nums:
            result.extend(list(range(i[0],i[1]+1)))
        return len(set(result))