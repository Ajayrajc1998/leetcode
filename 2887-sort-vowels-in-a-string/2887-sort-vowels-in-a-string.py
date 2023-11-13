class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiou')
        vw = sorted(c for c in s if c.lower() in vowels)

        j = 0
        result = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                result.append(vw[j])
                j += 1
            else:
                result.append(s[i])

        return "".join(result)