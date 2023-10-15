class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        a=str(num)
        b=int(a[::-1])
        b=str(b)
        if a==b[::-1]:
            return True
        return False