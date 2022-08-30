class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_ss = 0
        seen_set = set()
        sliding_window = []

        for char in s:
            while char in seen_set:
                seen_set.remove(sliding_window[0])
                del sliding_window[0]


            sliding_window.append(char)
            seen_set.add(char)
            max_ss = max(max_ss, len(sliding_window))
      
  
        return max_ss
#         chars = []
#         maxLength = 0
#         for i in range(len(s)):
#             while s[i] in chars:
#                 del chars[0]
#             chars.append(s[i])
#             maxLength = max(len(chars), maxLength)
            
#         return maxLength