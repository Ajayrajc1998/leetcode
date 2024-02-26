class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        d1={items1[i][0]:items1[i][1] for i in range(len(items1))}
        d2={items2[i][0]:items2[i][1] for i in range(len(items2))}
        result=[]
        for key in d1:
            if key in d2:
                result.append([key,d1[key]+d2[key]])
            else:
                result.append([key,d1[key]])
        for key in d2:
            if key not in d1:
                result.append([key,d2[key]])
        result.sort()
        return result