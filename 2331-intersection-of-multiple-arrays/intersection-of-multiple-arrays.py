class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        count={}
        for i in nums:
            for j in i:
                if j not in count:
                    count[j]=1
                else:
                    count[j]+=1
        
        result=[]
        for key in count:
            if count[key]==len(nums):
                result.append(key)
        result.sort()
        return result