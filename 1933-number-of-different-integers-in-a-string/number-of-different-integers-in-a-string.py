class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        dig=set()
        dig_flag=False
        num=''
        for i in range(len(word)):
            if word[i].isdigit() and not dig_flag:
                dig_flag=True
            if word[i].isdigit() and dig_flag:
                num+=word[i]
            if not word[i].isdigit() and dig_flag:
                dig.add(int(num))
                dig_flag=False
                num=''
        if not word.isalpha() and dig_flag:
            dig.add(int(num))
        return len(dig)
                