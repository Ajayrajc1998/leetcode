class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        sub=[]
        for i in range(len(nums)):
            sub.append(nums[i])
            if (i+1)%3==0:
                res.append(sub)
                sub=[]
        for i in range(len(res)):
            for j in range(len(res[i])):
                if j==0:
                    if res[i][1]-res[i][0]>k:
                        return []
                    elif res[i][2]-res[i][0]>k:
                        return []
                elif j==1:
                    if res[i][0]-res[i][1]>k:
                        return []
                    elif res[i][2]-res[i][1]>k:
                        return []
                else:
                    if res[i][1]-res[i][2]>k:
                        return []
                    elif res[i][2]-res[i][2]>k:
                        return []

        return res
                

        