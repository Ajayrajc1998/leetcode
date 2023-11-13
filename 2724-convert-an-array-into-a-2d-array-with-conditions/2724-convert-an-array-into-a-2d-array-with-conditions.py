class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # result=[]
        # sub=[]
        # i=0
        # while True:
        #     if nums[i] not in sub:
        #         sub.append(nums[i])
        #         nums.pop(i)
        #     else:
        #         i+=1
            
        #     if i==len(nums)-1 or len(nums)==0 :
        #         result.append(sub)
        #         print("result",result)
        #         print('nums',nums)
        #         sub=[]
        #         i=0
        #     if len(nums)==0:
        #         break
            
        # return result

        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        result=[]
        while set(d.values())!=set([0]):
            sub=[]
            for i in d.keys():
                if d[i]!=0:
                    sub.append(i)
                    d[i]-=1
            print('sub',sub)
            result.append(sub)
        print(result)
        return result