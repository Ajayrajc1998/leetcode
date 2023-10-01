class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split(" ")
        result=[0 for _ in range(len(s))]
        for i in s:
            intex=int(i[-1])
            result[intex-1]=i[:-1]
        return " ".join(result)
        