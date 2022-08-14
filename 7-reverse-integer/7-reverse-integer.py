class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 4294967295:
            return 0
        
        x = list(str(x))
        new_num = []
        neg = False
        
        if '-' in str(x):
            neg = True
            x = x[1:]
        new_x = ''.join(x[::-1])
#         check if trailing 0's
        while new_x[0] == 0:
            del new_x[0]
          
        
        if int(new_x) > 2147483647:
            return 0
        elif neg is True and int('-' + new_x) < -2147483648: 
            return 0
        if neg:
            return int('-' + new_x)
        return int(new_x)
            
            
        