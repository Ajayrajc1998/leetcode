class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        result=[]
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[j]-nums[i]==diff and nums[k]-nums[j]==diff:
                        if [i,j,k] not in result:
                            result.append([i,j,k])
        return len(result)
        