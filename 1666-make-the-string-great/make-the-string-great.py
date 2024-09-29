class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        res.append(s[0])
        j=0
        for i in range(1,len(s)):
            res.append(s[i])
            if s[i].lower()==res[j].lower():
                if s[i]!=res[j]:
                    res.pop()
                    res.pop()
                    j-=1
                else:
                    j+=1
            else:
                j+=1


        return ''.join(res) if len(s)>0 else ''