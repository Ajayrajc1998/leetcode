class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.split()
        num=[int(i) for i in s if i.isdigit()]
        for i in range(len(num)-1):
            if num[i]>=num[i+1]:
                return False 
        return True
