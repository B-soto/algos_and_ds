from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_freq = Counter(s)
        rtn_str = []
        
        for char in order:
            if char in s_freq:
                for _ in range(s_freq[char]):
                    rtn_str.append(char)
                del s_freq[char]
                
        for item, freq in s_freq.items():
            for _ in range(freq):
                rtn_str.append(item)
        print(''.join(rtn_str))
        return ''.join(rtn_str)
        
        