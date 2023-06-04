class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        
        
        s = s[::-1]
        s = s.strip()
        
        if len(s) == 1:
            return 1
        
        rp = 0
        for lp in range(len(s)):
            if s[lp] == ' ':
                lp -= 1
                break
        print(lp,rp)
        return((lp-rp)+1)
                