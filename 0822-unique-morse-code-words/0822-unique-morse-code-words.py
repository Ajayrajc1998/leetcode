class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        symbol=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d={}
        for i in range(26):
            d[chr(97+i)]=symbol[i]
        res=set()
        for i in range(len(words)):
            t=""
            for j in range(len(words[i])):
                t+=d[words[i][j]]
            res.add(t)
        return len(res)