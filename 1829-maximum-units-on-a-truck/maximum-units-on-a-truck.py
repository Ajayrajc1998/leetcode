class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        target=0
        result=0
        boxTypes=sorted_data = sorted(boxTypes, key=lambda x: x[1],reverse=True) 
        for i in range(len(boxTypes)):
            print(boxTypes[i])
            if boxTypes[i][0]+target<=truckSize:
                target+=boxTypes[i][0]
                result+=(boxTypes[i][0]*boxTypes[i][1])
            elif target==truckSize:
                break
            elif boxTypes[i][0]+target>truckSize:
                remain=(truckSize-target)
                result+=(remain*boxTypes[i][1])
                break
         
        return result
                