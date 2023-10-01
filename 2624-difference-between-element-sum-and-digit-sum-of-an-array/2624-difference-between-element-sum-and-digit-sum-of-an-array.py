class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=""
        for i in nums:
            s+=str(i)
        print(s)
        digit_sum=0
        for i in s:
            digit_sum+=int(i)
        return abs(sum(nums)-digit_sum)