class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Big(o)n
        #Aux space o(s + t)
        s_freq, t_freq = {}, {} #o(1)
        
        if len(s) != len(t): #(o(s) + o(t)
            return False
        
        for i in range(len(s)): #o(s)
            if s[i] not in s_freq:
                s_freq[s[i]] = 1
            else:
                s_freq[s[i]] += 1
                
            if t[i] not in t_freq:
                t_freq[t[i]] = 1
            else:
                t_freq[t[i]] += 1
                
        return s_freq == t_freq
                
            
        