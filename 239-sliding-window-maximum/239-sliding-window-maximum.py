from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        
        rtn_arr = []
        d = deque()
        
        for i, n in enumerate(nums):
            # print(i)
            while len(d) > 0 and n > nums[d[-1]]:
                d.pop()
            d.append(i)
            
            if d[0] == i-k:
                # print('removing', d[0], 'from', d, 'index', i)
                d.popleft()
            
            if i >= k-1:
                # print('adding')
                rtn_arr.append(nums[d[0]])
        return(rtn_arr)
        
        
        