class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_trim=[]
        t_trim=[]
        for i in range(len(s)):
            if s[i]!='#':
                s_trim.append(s[i])
            if s[i]=='#' and len(s_trim)>=1:
                s_trim.pop()
        for i in range(len(t)):
            if t[i]!='#':
                t_trim.append(t[i])
            if t[i]=='#' and len(t_trim)>=1:
                t_trim.pop()
        
        if s_trim==t_trim:
            return True
        else:
            return False

        
