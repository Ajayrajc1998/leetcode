class Solution(object):
    def twoSum(self, nums, target):
        res=[]
        for i in range(len(nums)):
            num=nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]+num==target:
                    res.append(i)
                    res.append(j)
                    return res
