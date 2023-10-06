class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res=0
        alt=0
        for i in gain:
            alt+=i
            if alt>res:
                res=alt
        return res