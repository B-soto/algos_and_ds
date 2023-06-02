class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        letter_freq = {}
        
        for word in strs:
            letters = ''.join(sorted(word))
            
            if letters in letter_freq:
                letter_freq[letters].append(word)
            else:
                letter_freq[letters] = [word]
                
        rtn_arr = []
        for k,v in letter_freq.items():
            rtn_arr.append(v)
            
        return rtn_arr
            
        
#         letter_freq = {{e:1,a:1,t:1}: [eat ,tea, ate]
#                        {t:1 a:1 n:1}: [tan,nat]
#                       {}}
        
        
        
        # Create a letter_freq_dict with arrays as values and dict as key
        
        # Iterate over each word in strs
        #createa freq counter for each word 
        # See if that freq is in the letter_freq dict. 
            #if it is, append it to the value
            #if not, create that dict with the value being an array with word as 0 index
            
            
    
        # Iterate over letter_freq and throw all values into a larger array.
        #return that array
        