class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        """

        return string or list

        curr_string
        iterate over string s
        when we see a (, throw it in our stack
        while stack, 
            we should addd to current string whenever we see a ). pop the top of stack and append the pair to curr 
        once stack is done, we add curr string to return_list and reset curr_string



        (()())(())(()(()))
                         
        stack = {
            
            
            (
        }
        count = 1
        curr_string = ()()
        return = []
        """
        return_list = []
        count = 0

        curr_str = ""
        for p in s:
            if p == "(" and count == 0:
                count +=1
            elif p == "(" and count > 0:
                count +=1
                curr_str +="("
            elif p == ")" and count > 1:
                count -=1
                curr_str += ")"
            elif p == ")" and count == 1:
                count -=1
                return_list.append(curr_str)
                curr_str = ""

        return "".join(return_list)