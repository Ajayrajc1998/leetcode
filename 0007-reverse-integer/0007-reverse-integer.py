class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x=str(x)
        x=x[::-1]
        neg=False
        if '-' in x:
            neg=True    
        if neg:
            x=x[:-1]
            if (int(x) > 2**31 - 1) or (int(x) < -2**31):
                    return 0
            return -int(x)
        if (int(x) > 2**31 - 1) or (int(x) < -2**31):
                    return 0
        return int(x)
            