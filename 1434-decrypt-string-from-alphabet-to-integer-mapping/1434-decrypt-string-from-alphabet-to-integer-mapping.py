class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        res=""
        while i<len(s):
            if i+2<len(s) and s[i+2]=="#":
                res+=chr(96+int(s[i:i+2]))
                i=i+3
            else:
                res+=chr(96+int(s[i]))
                i+=1
            print(res)

        return res