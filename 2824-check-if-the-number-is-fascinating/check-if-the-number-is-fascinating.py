class Solution(object):
    def isFascinating(self, n):
        tot=""
        total_num=[]
        for i in range(3,0,-1):
            dig_2=n%10**(i)
            dig=dig_2//10**(i-1)
            if dig==0:
                return False
            total_num.append(dig)
        n_2=2*n
        for i in range(3,0,-1):
            dig_2=n_2%10**(i)
            dig=dig_2//10**(i-1)
            if dig==0:
                return False
            total_num.append(dig)
        n_3=3*n
        for i in range(3,0,-1):
            dig_2=n_3%10**(i)
            dig=dig_2//10**(i-1)
            if dig==0:
                return False
            total_num.append(dig)
        f_num=[i for i in range(1,10)]
        if f_num==sorted(total_num):
            return True
        else:
            return False