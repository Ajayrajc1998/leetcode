class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count=0
        i=j=0
        while i<len(points)-1:
            if abs(points[i][0]-points[i+1][0])>abs(points[i][1]-points[i+1][1]):
                count+=abs(points[i][0]-points[i+1][0])
            else:
                count+=abs(points[i][1]-points[i+1][1])
            i+=1
        return count 
        