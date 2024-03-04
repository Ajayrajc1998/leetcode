class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if ('a' not in s) or ('b' not in s):
            return True
        a_index=[]
        b_index=[]
        for i in range(len(s)):
            if s[i]=='a':
                a_index.append(i)
            elif s[i]=='b':
                b_index.append(i)
        print('aIndex',a_index)
        print('bIndex',b_index)
        if a_index[-1]>b_index[0]:
            return False
        else:
            return True
            

