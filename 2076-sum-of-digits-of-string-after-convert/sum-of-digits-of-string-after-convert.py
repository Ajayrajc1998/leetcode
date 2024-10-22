class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def count_digit(n):
            dig_sum=0
            while n>0:
                dig_sum+=n%10
                n//=10
            return dig_sum
        num=''
        for i in s:
            num+=str((ord(i)-97)+1)
        for i in range(k):
            num=count_digit(int(num))
        return num

