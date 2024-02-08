class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first_occurence(nums,target):
            left,right=0,len(nums)-1
            first_occurence=-1
            while left<=right:
                mid=left+(right-left)//2

                if nums[mid]==target:
                    first_occurence=mid
                    right=mid-1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return first_occurence
        
        def last_occurence(nums,target):
            left,right=0,len(nums)-1
            last_occurence=-1
            while left<=right:
                mid=left+(right-left)//2

                if nums[mid]==target:
                    last_occurence=mid
                    left=mid+1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return last_occurence
        first=first_occurence(nums,target)
        last=last_occurence(nums,target)
        return [first,last]