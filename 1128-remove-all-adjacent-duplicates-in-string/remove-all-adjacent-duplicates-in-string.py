class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=[]
        for i in s:
           if a !=[]:
                if i==a[-1]:
                    a.pop()
                else:
                        a.append(i)
           else:
                a.append(i)
        return ''.join(a)