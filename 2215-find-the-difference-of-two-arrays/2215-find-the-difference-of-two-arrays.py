
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        freq = {}

        for num in nums1:
            freq[num] = 1

       
        for num in nums2:
            if num in freq and freq[num] != 2:
                freq[num] = 3
            else:
                freq[num] = 2

     

        return [[k for k,v in freq.items() if v == 1], [k for k,v in freq.items() if v == 2]]