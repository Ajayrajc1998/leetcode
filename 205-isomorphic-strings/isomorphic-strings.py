class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d={}

        for i in range(len(s)):
            if s[i] not in d:
                if t[i] not in d.values():
                    d[s[i]]=t[i]
                else:
                    return False
            else:
                if d[s[i]]!=t[i]:
                    return False
        return True
