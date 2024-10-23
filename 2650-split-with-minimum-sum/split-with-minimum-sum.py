class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        dig=[]

        while num>0:
            dig_num=num%10
            num//=10
            dig.append(dig_num)
        left=[]
        right=[]
        dig.sort()
        for i in range(len(dig)):
            if (i+1)%2==1:
                left.append(dig[i])
            else:
                right.append(dig[i])
        left_num=''
        for i in left:
            left_num+=str(i)
        right_num=''
        for j in right:
            right_num+=str(j)
        return int(left_num)+int(right_num)