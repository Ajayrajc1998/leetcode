class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.split("|")
        count=0
        for i in range(0,len(s),2):
            count+=s[i].count("*")
        return count