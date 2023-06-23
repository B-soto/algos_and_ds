class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        s1_mismatch = {}
        changes = 0
        s2_mismatch = {}
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                s1_mismatch[s1[i]] = s2[i]
                s2_mismatch[s2[i]] = s1[i]
                changes += 1
                
        #check if either dict is longer than 2 items 
        if changes <= 2 and len(s1_mismatch) <= 2 and len(s2_mismatch) <= 2 and s2_mismatch == s1_mismatch:
            return True
        else:
            return False