class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        j=n
        d1={}
        d2={}
        while i<=n:
            d1[i]=sum(range(1,i+1))  
            i+=1
        while j>0:
            d2[j]=sum(range(j,n+1))
            j-=1
        print(d1,'d111111')
        print(d2,'d2222222')
        for i in range(1,n+1):
            if d1[i]==d2[i]:
                return i
        return -1
        