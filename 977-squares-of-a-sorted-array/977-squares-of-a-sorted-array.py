class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negative_stack = []
        positive_nums = []
        rtn_arr = []
        for n in nums:
            if n < 0:
                negative_stack.append(n)
            else:
                positive_nums.append(n)
        
        negative_index = len(negative_stack) -1
        positive_index = 0
        
        # [-4,-1] [0,3,10]
        
        while positive_index <= len(positive_nums)-1 and negative_index >= 0:
            # print(positive_index, len(positive_nums)-1, negative_index)
            if positive_nums[positive_index] <= abs(negative_stack[negative_index]):
                rtn_arr.append(positive_nums[positive_index] * positive_nums[positive_index])
                positive_index +=1
            else:
                rtn_arr.append(negative_stack[negative_index] * negative_stack[negative_index])
                negative_index -= 1
                
        while positive_index <= len(positive_nums)-1:
            rtn_arr.append(positive_nums[positive_index] * positive_nums[positive_index])
            positive_index +=1
            
        while negative_index > -1:
            rtn_arr.append(negative_stack[negative_index] * negative_stack[negative_index])
            negative_index -= 1
        # print(rtn_arr,negative_stack, positive_nums)
        return rtn_arr
                