class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        text=text.split(" ")
        count=0
        for i in text:
            flag=True
            for j in brokenLetters:
                if j in i:
                    flag=False 
                    break
            if flag:
                count+=1
        return count