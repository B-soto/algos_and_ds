class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]
        
        prefix = strs[0]
        pi = 0
        
        
        for i in range(1, len(strs)):
            word = strs[i]
            if word == "" or prefix == "":
                return ""
            
            # print(word)
            for wi in range(len(word)):
                # print(word[wi],pi)
                if word[wi] == prefix[pi]:
                    pi +=1
                else:
                    break
                    
                if pi >= len(prefix):
                    break
            if pi == 0:
                return ''
            prefix = prefix[0:pi]
            # print(prefix)
            pi = 0
        return prefix
                
            
        