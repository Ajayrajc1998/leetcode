class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        res=[[heights[i],names[i]] for i in range(len(names))]
        res.sort(reverse=True)
        return [ i[1] for i in res]