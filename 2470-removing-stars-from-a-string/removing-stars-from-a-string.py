class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        for i in range(len(s)):
            if s[i]=='*' and res!=[]:
                res.pop()
            else:
                res.append(s[i])
        
        return ''.join(res) if res!=[] else ''