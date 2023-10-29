class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        s=set()
        s.update(nums1)
        s.update(nums2)
        s.update(nums3)
        result=[]
        for i in s:
            count=0
            if i in nums1:
                count+=1
            if i in nums2:
                count+=1
            if i in nums3:
                count+=1
            if count>1:
                result.append(i)
        return result