class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        d={}
        i=0
        j=0
        while i<len(nums1) and j <len(nums2):
            if nums1[i][0] not in d:
                d[nums1[i][0]]=nums1[i][1]
            else:
                d[nums1[i][0]]+=nums1[i][1] 
            if nums2[j][0] not in d:
                d[nums2[j][0]]=nums2[j][1]
            else:
                d[nums2[j][0]]+=nums2[j][1]
            i+=1
            j+=1
        while i<len(nums1):
            if nums1[i][0] not in d:
                d[nums1[i][0]]=nums1[i][1]
            else:
                d[nums1[i][0]]+=nums1[i][1] 
            i+=1
        while j<len(nums2):
            if nums2[j][0] not in d:
                d[nums2[j][0]]=nums2[j][1]
            else:
                d[nums2[j][0]]+=nums2[j][1]
            j+=1
        result=[[i,d[i]] for i in d]
        result.sort()
        return result
            
