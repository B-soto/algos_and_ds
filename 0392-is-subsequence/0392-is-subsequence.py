class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        s_index = 0
        
        for char in t:
            if char == s[s_index]:
                s_index += 1
                if s_index == len(s): return True
        return False
        
#         s = "abc", 
#                 ^
        
        
#         t = "ahbgdc"
#                   ^
            
        # create a pointer to watch letters needed in s
        #Start pointer at 0
        
        # Iterate over T
        # IF a ltter in T matches s pointer, then increase s pointer .If s Pointer is ever length of s, we got all letters return true
        #keep iterating T checking for s pointer char. if we make it to end of loop, return Flase. we didnt find all the lletters
        
        
        
            