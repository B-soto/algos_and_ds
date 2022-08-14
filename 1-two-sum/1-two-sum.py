class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for count, num in enumerate(nums):
            
            value = target - num 
            
            if value in visited.values():
                print("Found value")
                for k,v in visited.items():
                    if v == value:
                        return [k, count]
            visited[count] = num