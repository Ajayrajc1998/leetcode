class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        a=list(str(num))
        for i in range(len(a)):
            if a[i]!='9':
                a[i]='9'
                break
        a="".join(a)
        return int(a)