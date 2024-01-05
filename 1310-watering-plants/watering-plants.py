class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        i=0
        j=0
        step=0
        temp=capacity
        while i<len(plants):
            print(temp)
            if plants[i]<=temp:
                step+=1
                print('step',1)
                temp-=plants[i]
            else:
                temp=capacity
                step+=(i)+(i+1)
                temp-=plants[i]
            
            i+=1
        return step
                    