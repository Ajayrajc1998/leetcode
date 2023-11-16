class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=[]
        i=1
        j=0
        sub=s[0]
        while i<len(s):
            if s[i] not in sub:
                sub+=s[i]
                i+=1
            else:
                res.append(sub)
                sub=s[i]
                i+=1
        return len(res)+1