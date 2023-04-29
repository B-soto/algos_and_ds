class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
       
        sequences_seen = {}
        
        left = 0
        right = 9

        #get freq of all possible 10 strand dna 
        while right < len(s):
            sub_string = ''.join(s[left:right+1])
            
            
            if sub_string in sequences_seen:
                sequences_seen[sub_string] +=1
            else:
                sequences_seen[sub_string] = 1
            
            left +=1
            right +=1
                
        
        return [k for k,v in sequences_seen.items() if v > 1]
    
    