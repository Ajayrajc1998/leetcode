class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        target=0

        for i in arr:
            if arr.count(i)==1:
                target+=1
                if target==k:
                    return i
        return ""