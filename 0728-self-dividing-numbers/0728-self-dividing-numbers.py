class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        for i in range(left,right+1):
            count=0
            for j in str(i):
                if int(j)!=0 and i%int(j)==0 :
                    count+=1
            if count==len(str(i)):
                res.append(i)
        return res