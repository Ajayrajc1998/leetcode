class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s=list(str(num))
        s=[int(i) for i in s]
        print(s)
        count=0
        for i in s:
            if num%i==0:
                count+=1
        return count

        