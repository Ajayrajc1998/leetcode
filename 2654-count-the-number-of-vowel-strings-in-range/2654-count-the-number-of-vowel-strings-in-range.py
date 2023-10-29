class Solution(object):
    def vowelStrings(self, words, left, right):
        """
        :type words: List[str]
        :type left: int
        :type right: int
        :rtype: int
        """
        vowel=['a','e','i','o','u']
        count=0
        for  i in range(left,right+1):
            if words[i][0] in vowel and words[i][-1] in vowel:
                count+=1
        return count