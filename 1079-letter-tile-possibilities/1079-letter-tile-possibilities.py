class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen_set = set()
        
        
        def traverse(letters, tiles_arr):
            if letters:
                seen_set.add(letters)
            for i in range(len(tiles_arr)):
                traverse(letters + tiles_arr[i], tiles_arr[:i] + tiles_arr[i+1:])
            
        
        traverse('', tiles)
        return len(seen_set)
        