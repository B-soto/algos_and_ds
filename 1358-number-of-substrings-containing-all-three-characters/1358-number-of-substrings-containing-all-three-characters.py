class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        '''
        letter_needed = {a:0,b:0,c:0}
        letters_needed = 0
        total_count = 10
        left, right = 0,0
        abcabc
              R
            L
        Hunting Phase,
        Iterate over the string 
        if we see an a, b, or c, we subtract it from letter_needed dict. If the number is <= 0, then we also subtract it orm letters needed. 
        
        Now we check if we still need any letters.

        If not, 
        
        now we go into catch up phase
        while letters_needed is 0,
        update total count with curr substring value, + reminader of string since every possibel substring after will be valid
        count = count + (len(s) - r)
        we move our left pointer up. If
        left pointer that we lost was an A,B,C then we +1 to its letter freq dict. 
        If the letter freq dict is ever > 0, then we update letters needed and break out of our loop



        '''
        letter_needed = {'a':1,'b':1,'c':1}
        letters_needed = 3
        total_count = 0
        l, r = 0, 0

        while r < len(s):
            char = s[r]
            if char in letter_needed:
                letter_needed[char] -= 1
            if letter_needed[char] == 0:
                letters_needed -= 1

            while letters_needed == 0:
                print(l,r,total_count)
                total_count += len(s)- r

                lchar = s[l]
                l +=1
                if lchar in letter_needed:
                    letter_needed[lchar] +=1
                if letter_needed[lchar] == 1:
                    letters_needed += 1
            r +=1
            
        return total_count


        


                

                    