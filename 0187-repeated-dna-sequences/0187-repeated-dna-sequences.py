class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
       
        sequences_seen = set()
        
        left = 0
        right = 9
        
        return_arr = set()

        #get freq of all possible 10 strand dna 
        while right < len(s):
            sub_string = ''.join(s[left:right+1])
            
            
            if sub_string in sequences_seen:
                return_arr.add(sub_string)
            else:
                sequences_seen.add(sub_string)
            
            left +=1
            right +=1
                
        
        return list(return_arr)
    
    