class Solution:
    
    def strStr(self, haystack: str, needle: str) -> int:
        def check_sub_string(index):
            # Check to see if haystack index to end is shorter than needle
            if len(needle) > len(haystack) -index:
                print("here")
                return False
            haystack_runner = index
            
            for needle_runner in range(len(needle)):
                    if haystack[haystack_runner] != needle[needle_runner]:
                        return False
                    else:
                        haystack_runner +=1  
            return True
            
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]: #have a new pointer for haystack and needle progress through each string to see if they match
                check = check_sub_string(i)
                if check:
                    return i
        
        return -1
        
        