class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res=[0 for i in range(len(s))]
        i=0
        while i<len(res):
            res[indices[i]]=s[i]
            i+=1
        return "".join(res)
