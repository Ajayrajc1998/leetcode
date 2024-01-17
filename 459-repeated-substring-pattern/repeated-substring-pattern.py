class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=1
        j=0
        while i<len(s):
            sub=s[:i]
            if len(s)==(s.count(sub)*len(sub)):
                return True
            i+=1
        return False