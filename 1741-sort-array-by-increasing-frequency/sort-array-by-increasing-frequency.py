class Solution(object):
    def frequencySort(self, nums):
        n_count={}
        for i in nums:
            if i not in n_count:
                n_count[i]=nums.count(i)
        f_count=[]
        for i in n_count:
            f_count.append([i,n_count[i]])
        f_count=sorted(f_count,key=lambda x:(x[1],-x[0]))
        result=[]
        for i in f_count:
            for j in range(i[1]):
                result.append(i[0])
        return result

        
    