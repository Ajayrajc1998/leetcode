class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        l_text=text.split(" ")
        l_text=[i for i in l_text if i!='']
        s_count=text.count(' ')
        if len(l_text)>1:
            space=s_count//(len(l_text)-1)
            res=''
            for i in range(len(l_text)):
                res+=l_text[i]
                if i!=len(l_text)-1:
                    res+=' '*space

            if len(res)!=len(text):
                res+=' '*(len(text)-len(res))

            return res
        else:
            res=l_text[0]+' '*s_count
            return res
        