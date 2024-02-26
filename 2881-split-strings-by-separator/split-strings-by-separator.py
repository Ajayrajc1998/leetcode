class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        result=[]
        for word in words:
            l=word.split(separator)
            l=[i for i in l if i!=""]
            result.extend(l)
        
        return result