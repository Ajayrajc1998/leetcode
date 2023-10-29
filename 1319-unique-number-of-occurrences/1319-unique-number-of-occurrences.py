class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        if len(list(d.keys()))!=len(set(d.values())):
            return False
        return True
        