class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
   
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            
            #base case
            if i >= len(s):
                return True
            
            
            #recursive case
            answer_set = set()
            val = False
            for word in wordDict:

                word_length = len(word)
                if s[i:word_length+i] == word and dfs(i+word_length):
                    # cache[i] = True
                    return True
            
            cache[i] = False
            return False
            
            
        
        return dfs(0)
            
        
        
        
        
#                                                 i=0
#                                         /.               \.   
#                                     leet  i = 0            code X
#                                 /          \
#                             leet i=4 X     code i =4
#                         /.   \.              /\
                                            # i=8
                                        
                            
                
#         , wordDict = ["leet","code"]
        

#                                               "leetcode" 0
#                                          /.                  \. 
#                                 "l eetcode" 1 X                       "leetcode" 1
#                                 /.    \.                                /.        \.  
#                                                                    "le,etcode" X     "leetcode" 2
#                                                                     /.    \.         /.    \.  
#                                                                         "lee tcode" 3 X     "leetcode" 3
#                                                                                                 / \
#                                                                                     "leet code" 4  "leetcode" 4


#                                             "applepenapple", 0               wordDict = ["apple","pen"]
#                                             /.             \
#                                  "a pplepenapple"1 X    "applepenapple"1
#                                     /.  \                   /\
#                                                     .....
#                                                                 "applepenapple" 5
#                                                                     / \
#                                                     "apple penapple" 6
#                                                         /               \
#                                         "apple pen apple" 7 X         "apple penapple" 7
#         # Input: 
#         #     s = "____andog", wordDict = ["cats","dog","sand","and","cat"]
#         # {a:0 p:0 l:0 e:0 n:0}
        
        