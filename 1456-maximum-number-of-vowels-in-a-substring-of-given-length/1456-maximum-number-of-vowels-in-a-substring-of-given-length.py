class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = {'a','e','i','o','u'}
        
        max_count = 0
        curr_count = 0
        l = 0
        
        for i in range(k):
            letter = s[i]
            if letter in v:
                curr_count +=1
            max_count = max(max_count, curr_count)
            
        for i in range(k,len(s)):
            letter = s[i]
            left = s[l]
            l += 1
            
            if letter in v:
                curr_count +=1
                
            if left in v:
                curr_count -= 1
            max_count = max(max_count, curr_count)
        
        return(max_count)
            
        
            