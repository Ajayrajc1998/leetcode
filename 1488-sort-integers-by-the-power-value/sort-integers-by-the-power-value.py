class Solution(object):

    def pow(self,num,count=0):
        if num==1:
            return count
        elif num%2==0:
            return self.pow(num/2,count+1)
        else:
            return self.pow((3*num)+1,count+1)

    def getKth(self, lo, hi, k):
        """
        :type lo: int
        :type hi: int
        :type k: int
        :rtype: int
        """
        res=[]
        for i in range(lo,hi+1):
            num=self.pow(i)
            res.append([i,num])
        res=sorted(res,key=lambda x:x[-1])
        return res[k-1][0]