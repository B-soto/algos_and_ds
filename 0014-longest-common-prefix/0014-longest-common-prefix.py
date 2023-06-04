class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        prefix = strs[0]
        pi = 0
        
        for s in strs[1:]:
            if len(prefix) == 0:
                return ''
            for char in s:
                if char == prefix[pi]:
                    pi += 1
                else:
                    break
                if pi >= len(prefix):
                    break
                
            # if pi == 0:
            #     return ''
            
            prefix = prefix[0:pi]
            print(prefix, pi)
            pi = 0
        return prefix
                
            
        