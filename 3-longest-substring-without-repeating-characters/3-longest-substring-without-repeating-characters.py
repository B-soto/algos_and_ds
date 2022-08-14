class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = []
        maxLength = 0
        for i in range(len(s)):
            while s[i] in chars:
                del chars[0]
            chars.append(s[i])
            maxLength = max(len(chars), maxLength)
            
        return maxLength