class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(prices)):
            flag=False
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    res.append(prices[i]-prices[j])
                    flag=True
                    break
            if flag==False:
                res.append(prices[i])
                
        return res