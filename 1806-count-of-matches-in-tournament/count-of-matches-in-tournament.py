class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_matches=0
        team=n
        while team>1: 
            matches=team//2
            if matches*2!=team:
                team=matches+1
            else:
                team=matches
            total_matches+=matches
        return total_matches