class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        n=len(s)//2
        for i in range(n,-1,-1):
            if s[i]!=s[len(s)-1-i]:
                if ord(s[i])>ord(s[len(s)-1-i]):
                    s[i]=s[len(s)-1-i]
                else:
                    s[len(s)-1-i]=s[i]
        return "".join(s)