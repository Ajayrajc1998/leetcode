class Solution(object):
    def stringHash(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i=0
        result=''
        while True:
            sub=s[i:i+k]
            num=0
            for j in sub:
                num+=ord(j)-97
            num=num%26
            result+=chr(97+num)
            i=i+k
            if i+k>len(s):
                break
        return result