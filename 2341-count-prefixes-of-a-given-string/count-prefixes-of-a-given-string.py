class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        count=0
        for i in words:
            if i[0]==s[0]:
                if i==s[:len(i)]:
                    count+=1

        return count
        