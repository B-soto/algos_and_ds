class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        return_list = []
        count = 0

        curr_str = ""
        for p in s:
            if p == "(":
                if count > 0:
                    curr_str +="("
                count +=1
                
            elif p == ")" and count > 1:
                count -=1
                curr_str += ")"
            else:
                count -=1
                return_list.append(curr_str)
                curr_str = ""

        return "".join(return_list)