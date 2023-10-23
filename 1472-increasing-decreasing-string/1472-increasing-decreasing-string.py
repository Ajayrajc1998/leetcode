class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=list(set(s))
        i=j=0
        result=[]
        rev=False
        l.sort()
        while len(result)<len(s):
            if result.count(l[i])<s.count(l[i]):
                result.append(l[i])
            if i==len(l)-1 and  (rev==False):
                rev=True
                i+=1
            if i==0 and rev:
                rev=False
                i-=1
            if rev:
                i-=1
            else:
                i+=1
        return "".join(result)

        