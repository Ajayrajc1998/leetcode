class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        sq=[]
        for i in rectangles:
            if i[0]>i[1]:
                sq.append(i[1])
            else:
                sq.append(i[0])
        mxsq=max(sq)
        return sq.count(mxsq)