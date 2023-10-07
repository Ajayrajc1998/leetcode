class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        word=list(word)
        og=False
        for i in range(len(word)):
            if word[i]==ch:
                reverse=word[:i+1]
                og=i+1
                break
        if og!=False:
            reverse=reverse[::-1]
        else:
            return "".join(word)
        return "".join(reverse)+"".join(word[og:])