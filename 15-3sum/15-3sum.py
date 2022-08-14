import itertools
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer_pairs = []
        nums = sorted(nums) # n log n
        used_nums = set()
        used_pairs = set()
        
        #n * n-1 --> n^2
        for i in range(len(nums)):
            if nums[i] not in used_nums:
                target = 0-nums[i]
                new_arr = nums[i+1:]
                seen_set = set()
                for j in range(len(new_arr)):
                    j_compliment = target - new_arr[j]
                    if j_compliment in seen_set:
                        used_nums.add(nums[i])
                        
                        potential_match = [j_compliment, nums[i], new_arr[j]]
                        potential_match_set = (j_compliment, nums[i], new_arr[j])
                        if potential_match_set not in used_pairs:
                            used_pairs.add(potential_match_set)
                            answer_pairs.append(potential_match)                           
                    seen_set.add(new_arr[j])
        # print(answer_pairs)
        return answer_pairs
        # n log n + n^2 ==> n^2
        
        