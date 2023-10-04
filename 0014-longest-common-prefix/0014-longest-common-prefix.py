class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs[0]==[""]:
            return ""
        if len(strs)==1:
            return strs[0]
        res=''
        for i in range(1,len(strs[0])+1):
            s=strs[0][:i]
            count=1
            for j in range(1,len(strs)):
                if strs[j][:i]==s:
                    count+=1
            if count==len(strs):
                res=strs[j][:i]
        return res

