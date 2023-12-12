class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        for i in range(len(s)):
            substring=s[i:(i+3)]
            u=set()
            print(substring)
            for j in substring:
                u.add(j)
            if len(u)==3:
                print(u)
                count+=1
        return count