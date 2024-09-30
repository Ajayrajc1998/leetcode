class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_f=-1
        max_s=-2
        for i in s:
            if i.isdigit():
                if int(i)>max_f:
                    max_s=max_f
                    max_f=int(i)
                if int(i)>max_s and int(i)<max_f:
                    max_s=int(i)
        print(max_f,'first')
        print(max_s,'second')
        return max_s if max_s>-1 else -1