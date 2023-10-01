class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        a=edges[0][0]
        b=edges[0][1]
        if a not in edges[1]:
            return b
        else:
            return a
