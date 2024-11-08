class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original)!=(m*n):
            return []
        
        i=0
        j=0
        ans=[]
        while j<m:
            sub=[]
            k=0
            while k<n:
                sub.append(original[i])
                i+=1
                k+=1
            ans.append(sub)
            j+=1
        return ans