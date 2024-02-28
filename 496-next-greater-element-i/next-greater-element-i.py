class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in nums1:
            flag=True
            for j in range(nums2.index(i)+1,len(nums2)):
                if nums2[j]>i:
                    flag=False
                    result.append(nums2[j])
                    break
            if flag:
                result.append(-1)
        return result