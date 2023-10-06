class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i][::-1]==words[j]:
                    count+=1
        return count
        