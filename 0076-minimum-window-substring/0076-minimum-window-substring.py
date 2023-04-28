from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # t_dict = {
        #     a: 0
        #     b: 0
        #     c:0
        # }
        # needed_lettter = 0
        
        needed_letters = len(t)
        t_dict = Counter(t)
        
        
        
        
#         "ADOBECODEBANC", t = "ABC"
#               l
#                    r 
            
        l = 0
        r = 0
        target_index = [0,float('inf')]
            
        while r < len(s):
            letter = s[r]
            
            #Hunting Phase
            if needed_letters > 0:
                if letter in t_dict:
                    if t_dict[letter] > 0:
                        t_dict[letter] -=1
                        needed_letters -= 1
                    else:
                        t_dict[letter] -=1
                        
            
            
            #catchup phase
            while needed_letters == 0:
                #update target_index_list
                if r-l < target_index[1] - target_index[0]:
                    target_index[0] = l
                    target_index[1] = r
                
                #Update l
                l_letter = s[l]
                if l_letter in t_dict:
                    if t_dict[l_letter] == 0:
                        needed_letters += 1
                    t_dict[l_letter] +=1
                    
                l += 1
                
            r += 1
            
    
        return s[target_index[0]:target_index[1]+1] if target_index[1] != float('inf') else "" 
            