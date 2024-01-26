class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        current_string = ""
        char_index_map = {}

        i = 0
        for j in range(len(s)):
            if s[j] in char_index_map and char_index_map[s[j]] >= i:
                i = char_index_map[s[j]] + 1

            current_string = s[i:j + 1]

            if len(current_string) > max_length:
                max_length = len(current_string)

            char_index_map[s[j]] = j

        return max_length