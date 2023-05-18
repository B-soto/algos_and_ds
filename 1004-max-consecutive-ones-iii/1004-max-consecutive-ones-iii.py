class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        longest_sub_string
        flips_left = k
        
        Hunting Phase
        Iterate over nums until we reach a 0. If we have flips left, we count it and keep moving
        check if flips_left 
        
        
        
        
        '''
        # [1,1,1,0,0,0,1,1,1,1,0]
        #        r
        # l
        longest = 0
        flips_left = k
        l,r = 0,0
        curr = 0
        
        while r < len(nums):
            if nums[r] == 1:
                curr = (r+1)-l
                print(r,l,curr)
                longest = max(longest, curr)
                r +=1
                continue
                
            if nums[r] == 0 and flips_left > 0:
                flips_left -=1
                curr = (r+1)-l
                print(r,l, flips_left, curr)
                longest = max(longest, curr)
                r +=1
            else:
                while flips_left == 0:
                    if nums[l] == 1:
                        l += 1
                        continue
                    else:
                        flips_left +=1
                        l +=1
                flips_left -=1
                curr = (r+1)-l
                print(r,l, flips_left, curr)
                longest = max(longest, curr)
                r +=1
        return(longest)
                
                
            
                
                