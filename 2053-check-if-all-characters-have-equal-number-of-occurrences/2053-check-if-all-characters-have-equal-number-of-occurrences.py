class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letter={}

        for i in s:
            if i not in letter:
                letter[i]=1
            else:
                letter[i]+=1
        
        a=set(letter.values())
        if len(a)==1:
            return True
        else:
            return False
        