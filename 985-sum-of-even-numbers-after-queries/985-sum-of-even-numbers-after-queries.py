class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        return_arr = []
        current_even_count = sum([x for x in nums if x%2==0])
        print(current_even_count)
        
        for q in queries:
            val = q[0]
            i = q[1]
            
            if val%2 != 0 and nums[i]%2 != 0:
                # print(val)
                nums[i] += val
                # print(nums)
                current_even_count += nums[i]
                # print(current_even_count)
            
            elif val%2 == 0 and nums[i]%2 == 0:
                current_even_count += val
                nums[i] += val
            
            elif val%2 != 0 and nums[i]%2 == 0:
                current_even_count -= nums[i]
                nums[i] += val
                
            elif val%2 == 0 and nums[i]%2 != 0:
                nums[i] += val
                
            return_arr.append(current_even_count)
        
        return return_arr
                
        