class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        a=97-ord(coordinates[0])
        b=int(coordinates[1])
        if a%2==0 and b%2==0:
            return True
        elif a%2==1 and b%2==1:
            return True
        else:
            return False