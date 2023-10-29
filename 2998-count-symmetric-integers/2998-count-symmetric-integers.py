class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        res=0
        for i in range(low if low>10 else 11,high+1):
            if len(str(i))%2==0:
                a=str(i)
                left=[int(i) for i in a[:len(a)//2] ]
                right=[int(i) for i in a[len(a)//2:]]
                if sum(left)==sum(right):
                    res+=1
                    
        return res