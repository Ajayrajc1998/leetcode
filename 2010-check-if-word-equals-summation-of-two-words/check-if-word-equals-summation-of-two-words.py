class Solution(object):
    def alpha_number(self,word):
        n=len(word)
        alphabet='abcdefghijklmnopqrstuvwxyz'
        num=0
        for i in range(len(word)):
            num+=alphabet.index(word[i])*(10**(n-(i+1)))
        return num
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        first_num=self.alpha_number(firstWord)
        second_num=self.alpha_number(secondWord)
        target_num=self.alpha_number(targetWord)
        if first_num+second_num==target_num:
            return True
        else:
            return False
        