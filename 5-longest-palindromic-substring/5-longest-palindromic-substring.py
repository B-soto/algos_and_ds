class Solution(object):
    def helper(self, string, l, r):
        while l >= 0 and r < len(string) and string[l] == string[r]:
            l += -1
            r += 1
        return(string[l+1:r])    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for i in range(len(s)):
            len1 = self.helper(s, i, i)
            if len(len1) > len(result):
                print('len1', len1, i)
                result = len1
                
            len2 = self.helper(s, i, i+1)
            if len(len2) > len(result):
                print('len2', len2, i)
                result = len2
        return result