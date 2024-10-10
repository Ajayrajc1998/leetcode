class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        res=[]
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                res.append([arr[i],arr[j],float(arr[i])/float(arr[j])])
        res=sorted(res,key=lambda x:x[-1])
        return [res[k-1][0],res[k-1][1]]