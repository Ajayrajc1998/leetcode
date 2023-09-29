class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count=0
        d={'type':0,'color':1,'name':2}
        for i in items:
            if i[d[ruleKey]]==ruleValue:
                count+=1
        return count
