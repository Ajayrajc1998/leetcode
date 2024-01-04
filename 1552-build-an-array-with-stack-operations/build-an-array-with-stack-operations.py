class Solution(object):
    def __init__(self):
        self.stack=[]
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        result=[]
        checker=[i for i in range(1,n+1)]
        i=0
        count=0
        while True:
            if checker[i] in target:
                result.append('Push')
                count+=1
            else:
                result.append('Push')
                result.append("Pop")
            i+=1
            if count==len(target):
                return result 

        