class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d={}

        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        res=[]
        for i in d:
            res.append([i,d[i]])
        
        res = sorted(res, key=lambda x: (-x[1], x[0]))
        result=''
        for i in range(len(res)):
            result+=res[i][0]*res[i][1]
        return result