class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        number_dict = { '2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5': ['j', 'k', 'l'],
                       '6': ['m','n','o'], '7': ['p','q','r', 's'], '8': ['t','u','v'], '9': ['w','x','y','z']
                      } 
        rtn_list = []
        
        
        def dfs(curr_str, index):
            nonlocal number_dict
            #base Case
            if index == len(digits):
                rtn_list.append(curr_str)
                return

            
            #recursive case
            temp_string = curr_str
            for letter in number_dict[digits[index]]:
                curr_str += letter
                dfs(curr_str, index+1)
                curr_str = temp_string
                
            
        dfs("",0)
        
        return rtn_list
        