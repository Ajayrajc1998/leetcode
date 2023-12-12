class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        sets=set()
        for i in s:
            if i in sets:
                return i
            else:
                sets.add(i)
        

            

        