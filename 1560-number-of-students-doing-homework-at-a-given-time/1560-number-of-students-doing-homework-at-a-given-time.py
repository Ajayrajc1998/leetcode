class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        count=0
        for i in range(len(startTime)):
            if queryTime in range(startTime[i],endTime[i]+1):
                count+=1
        return count