class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        
        max_tri=0
        res=num[0]
        count=1
        final_res=''
        for i in range(1,len(num)):
            if num[i]!=res[0]:
                count=1
                res=num[i]
            else:
                count+=1
                res+=num[i]
            
            if count==3:
                if int(res)>=max_tri:
                    max_tri=int(res)
                    final_res=res
        return  final_res