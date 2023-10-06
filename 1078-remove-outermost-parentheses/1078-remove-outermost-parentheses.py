class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=j=0
        # par=[]
        # while i<len(s)-1:
        #     if s[i]==')' and s[i+1]==')':
        #         par.append(s[j:i+2])
        #         i+=2
        #         j=i
        #     else:
        #         i+=1
        # print(par)
        # for i in range(len(par)):
        #     par[i]=par[i][1:len(par[i])-1]
        # print('after',par)
        # return "".join(par)
        par=[]
        d={'(':0,")":0}
        while i<len(s):
            if s[i]=="(":
                d["("]+=1
            else:
                d[")"]+=1
            i+=1
            if d["("]==d[")"]:
                par.append(s[j:i])
                d={'(':0,")":0}
                j=i
        print(par)
        for i in range(len(par)):
            par[i]=par[i][1:len(par[i])-1]
        print('after',par)
        return "".join(par)