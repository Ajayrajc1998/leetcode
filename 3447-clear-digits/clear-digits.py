class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        for i in s:
            if i.isnumeric():
                if res!=[]:
                    res.pop()
            else:
                res.append(i)
        
        return ''.join(res)