from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # note = {a:2} mag = {a:2 b:1}
        note = dict(Counter(ransomNote))
        mag = dict(Counter(magazine))
        print(note, mag)
        
        for k,v in note.items():
            if k not in mag or note[k] > mag[k]:
                return False
            
        return True
                
        