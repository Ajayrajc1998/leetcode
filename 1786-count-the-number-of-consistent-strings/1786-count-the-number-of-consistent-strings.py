class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count=0
        for i in range(len(words)):
            flag=True
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    flag=False
                    break
            if flag:
                count+=1
        return count