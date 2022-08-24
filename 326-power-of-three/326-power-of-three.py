class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        boolean = False
        if n ==1:
            return True
        if n < 3:
            return False
        
        while n > 3:
            print(n)
            if n % 3 != 0:
                return False
            else:
                # print(f'here {}')x
                n = n / 3
        print(n)
        if n != 3:
            return False
        else:
            return True
                
        