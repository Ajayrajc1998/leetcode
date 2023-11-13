class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        counts=[]
        for i in range(len(boxes)):
            count=0
            for j in range(len(boxes)):
                if i!=j:
                    if boxes[j]=="1":
                        count+=abs(j-i)
            counts.append(count)
        return counts
