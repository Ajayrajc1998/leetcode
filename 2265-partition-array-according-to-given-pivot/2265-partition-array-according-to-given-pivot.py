class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        a=sorted(nums)
        if a==nums:
            return nums
        if nums.count(pivot)>1:
            for i in range(a.index(pivot)+1,len(nums)):
                if nums[i]!=pivot:
                    right=i+1
                    break
        else:
            right=a.index(pivot)+1
        left=0
        for i in range(len(nums)):
            if nums[i]<pivot:
                a[left]=nums[i]
                left+=1
            elif nums[i]>pivot:
                a[right]=nums[i]
                right+=1
            else:
                pass
        return a
