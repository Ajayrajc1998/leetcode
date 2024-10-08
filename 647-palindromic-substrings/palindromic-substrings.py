class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        i=0
        s_len=1
        if len(s)==1:
            return 1


        while True:
            sub=s[i:i+s_len]
            if i+s_len>=len(s):
                s_len+=1
                i=0
            else:
                i+=1
            if sub==sub[::-1]:
                res+=1
            if s_len==len(s):
                break
        
        return res+1 if s==s[::-1] else res



