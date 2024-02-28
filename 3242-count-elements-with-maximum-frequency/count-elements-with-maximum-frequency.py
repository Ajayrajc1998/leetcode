class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count=0
        max_count_num=set()
        for i in nums:
            if nums.count(i)>max_count:
                max_count=nums.count(i)
        for i in nums:
            if nums.count(i)==max_count:
                max_count_num.add(i)
        return len(max_count_num)*max_count        