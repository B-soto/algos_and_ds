from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        note = Counter(ransomNote)
        mag = Counter(magazine)

        
        for k,v in note.items():
            if k not in mag or note[k] > mag[k]:
                return False
            
        return True
                
        