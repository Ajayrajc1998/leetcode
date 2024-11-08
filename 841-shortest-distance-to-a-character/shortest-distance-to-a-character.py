class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        e_index=[]
        for i in range(len(s)):
            if s[i]==c:
                e_index.append(i)
        
        ans=[]
        for i in range(len(s)):
            if s[i]==c:
                ans.append(0)
            else:
                min_dist=len(s)+1
                for j in e_index:
                    if abs(i-j)<min_dist:
                        min_dist=abs(i-j)
                ans.append(min_dist)
        
        return ans

        

