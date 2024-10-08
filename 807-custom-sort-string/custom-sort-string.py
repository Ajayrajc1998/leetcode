class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        s=list(s)
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                try:
                    if order.index(s[i])>order.index(s[j]):
                        s[i],s[j]=s[j],s[i]
                except:
                    pass
        
        return ''.join(s)