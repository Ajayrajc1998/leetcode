class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """

        d={str(i):set() for i in range(0,10)}
        i=0
        j=2
        while j<len(rings)+2:
            a=rings[i:j]
            print(a)
            d[a[1]].add(a[0])
            i=j
            j+=2
        count=0
        for i in d.values():
            if len(i)==3:
                count+=1
        print(d)
        return count