class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        start=set()
        end=set()
        for i in paths:
            start.add(i[0])
            end.add(i[1])
        res=end.difference(start)
        res=list(res)
        return res[0]