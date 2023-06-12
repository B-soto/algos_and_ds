class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # s = "xyzzaz" [xyz,yzz,zza,zaz] [True,False,False,False ] == > 1 ==. 3n o(n)
        # set = (xyz)
        #iterate over s
        
        # as we iterate we count up to 3, and create a set, If the set is len(3) after building our string, then we update ocunt else we move on
        
#         count = 0
#         for i in range(len(s)-2):
#             seen_set = set()
#             for x in range(3):
#                 seen_set.add(s[i+x])
                
#             if len(seen_set) == 3:
#                 count +=1
#         return count

        seen = {}
        unique = 0
        count = 0
        
        l,r = 0,0
        
        while r < len(s):
            
            char = s[r]
            if char in seen:
                seen[char] +=1
            else:
                seen[char] = 1
                unique += 1

                
            if r > 2:
                #update l, remove from dict. If freq of char < 1, decrememnt uniqe
                lchar = s[l]
                l +=1
                seen[lchar] -= 1
                
                if seen[lchar] < 1:
                    del seen[lchar]
                    unique -= 1
                    
            if unique > 2:
                count += 1
                
            r+=1
        return count
                
                
            
                
                
            
            
        