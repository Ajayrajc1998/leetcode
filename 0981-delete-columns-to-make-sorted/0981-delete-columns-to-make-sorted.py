class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count=0
        colstr=[]
        for i in range(len(strs[0])):
            s=""
            for j in range(len(strs)):
                s+=strs[j][i]
            colstr.append(s)
        for i in colstr:
            if list(i)!=sorted(i):
                count+=1
            
        return count
