class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels=['a','e','i','o','u']
        a=s[:len(s)//2]
        b=s[len(s)//2:]
        a=a.lower()
        b=b.lower()
        print(a,b)
        count1=0
        count2=0
        for i in range(len(a)):
            if a[i] in vowels:
                count1+=1
            if b[i] in vowels:
                count2+=1
        if count1==count2:
            return True
        else:
            return False
        