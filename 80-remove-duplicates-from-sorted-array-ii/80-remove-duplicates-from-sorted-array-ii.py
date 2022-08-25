class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return nums
        
        last_digit_seen = nums[0]
        digit_freq = 1
        
        
        for i in range(1, len(nums)):
            if nums[i] == last_digit_seen:
                if digit_freq < 2:
                    digit_freq += 1
                else:
                    nums[i] = '_'
            else:
                last_digit_seen = nums[i]
                digit_freq = 1
        
        for i in range(len(nums)):
            if nums[i] == '_':
                j = i
                while (j < len(nums)):
                    if type(nums[j]) == int:
                        #print('swap', nums[i], nums[j])
                        nums[i] = nums[j]
                        nums[j] = '_'
                        break
                    else:
                        j += 1
        count = [1 for n in nums if type(n) == int]
        return sum(count)
        
        
        