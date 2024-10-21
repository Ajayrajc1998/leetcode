class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res=[]

        # for i in queries:
        #     max_len=0
        #     for j in range(len(nums)):
        #         if sum(nums[:j+1])<=i:
        #             if len(nums[:j+1])>max_len:
        #                 max_len=len(nums[:j+1])
        #     res.append(max_len)

        # return res if res!=[] else [0,]

        prefix_sum=[0]*len(nums)
        prefix_sum[0]=nums[0]

        for i in range(1,len(nums)):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        
        for q in queries:
            left,right=0,len(nums)-1
            max_len=0

            while left<=right:
                mid=(left+right)//2
                if prefix_sum[mid]<=q:
                    max_len=mid+1
                    left=mid+1
                else:
                    right=mid-1
            
            res.append(max_len)
        
        return res

