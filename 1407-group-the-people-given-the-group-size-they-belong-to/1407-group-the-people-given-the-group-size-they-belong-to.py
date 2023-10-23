class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        d={}

        for i in range(len(groupSizes)):
            if groupSizes[i] not in d:
                a=[i]
                d[groupSizes[i]]=a
            else:
                d[groupSizes[i]].append(i)
        result=[]
        print(d)
        for i in d.keys():
            if len(d[i])==i:
                result.append(d[i])
            else:
                a=len(d[i])//i
                k=0
                for j in range(a):
                    result.append(d[i][k:k+i])
                    k=k+i
        result.sort()
        return result