class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # O(n)
        # O(n2)
        print(len(s))
        sequences_seen = {}
        
        left = 0
        right = 9

        #get freq of all possible 10 strand dna 
        while right < len(s):
            sub_string = ''.join(s[left:right+1])
            # print(sub_string)

            
            if sub_string in sequences_seen:
                sequences_seen[sub_string] +=1
            else:
                sequences_seen[sub_string] = 1
            
            left +=1
            right +=1
                
        # print([k for k,v in sequences_seen.items() if v > 1])
        return [k for k,v in sequences_seen.items() if v > 1]
    
    