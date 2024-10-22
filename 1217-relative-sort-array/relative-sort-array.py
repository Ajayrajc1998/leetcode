class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        d={arr2[i]:i for i in range(len(arr2))}
        print(d)
        last=[]
        arr_1=[]
        for i in arr1:
            if i in d:
                arr_1.append(i)
            else:
                last.append(i)
        
        arr_1=sorted(arr_1,key=lambda x:d[x])
        last.sort()
        arr_1.extend(last)
        return arr_1