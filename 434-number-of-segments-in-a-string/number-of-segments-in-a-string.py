class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        s = s.rstrip()
        if s=="":
            return 0
        count=0
        s=s.split(" ")
        s=[i for i in s if i!=""]
        print(s)
        # for i in s:
        #     if i==" ":
        #         count+=1
        return len(s)
