class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s=s.split(":")
        a=ord(s[0][0])
        b=ord(s[1][0])
        c=(b-a)+1
        r=int(s[1][1])-int(s[0][1])+1
        print(s,'s')
        result=[]
        print(r,'r')
        print(c,'c')
        for i in range(int(s[0][1]),int(s[0][1])+int(r)):
            for j in range(1,int(c+1)):
                print('Yes')
                result.append(chr(a+(j-1))+str(i))
        result.sort()
        return result
