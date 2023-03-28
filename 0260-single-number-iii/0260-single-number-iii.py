class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        seen_set = {}
        for n in nums:
            if n in seen_set:
                seen_set[n] += 1
            else:
                seen_set[n] = 1
        
        return [k for k,v in seen_set.items() if v ==1]
        