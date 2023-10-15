class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        num=int(num)
        while num%10==0:
            num=num/10
        return str(num)
        