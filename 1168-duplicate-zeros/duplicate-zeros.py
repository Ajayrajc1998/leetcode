class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        i=0
        while i<len(arr):
            if arr[i]==0:
                arr.insert(i,0)
                arr.pop()
                i=i+2
            else:
                i+=1
        
        return arr