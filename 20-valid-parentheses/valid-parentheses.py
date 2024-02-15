class Solution(object):
    def isValid(self, s):
        brackets={')':'(','}':'{',']':'['}

        stack=[]
        for i in s:
            if i in brackets.values():
                stack.append(i)
            elif i in brackets.keys():
                if not stack or stack.pop()!=brackets[i]:
                    return False

        return not stack 