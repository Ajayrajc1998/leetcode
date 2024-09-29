class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        res.append(s[0])
        j=0
        for i in range(1,len(s)):
            res.append(s[i])
            print(res)
            if s[i].lower()==res[j].lower():
                print('common')
                if s[i]!=res[j]:
                    print('yes')
                    res.pop()
                    res.pop()
                    j-=1
                else:
                    j+=1
            else:
                j+=1


        return ''.join(res) if len(s)>0 else ''