class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_pointer = 0
        r_pointer = len(s) - 1

        while l_pointer < r_pointer:
            # we don't overtake pointers AND it's not alphanumeric
            # then, we gotta keep moving our pointers
            while l_pointer < r_pointer and not self.isAlphaNum(s[l_pointer]):
                l_pointer += 1
            while r_pointer > l_pointer and not self.isAlphaNum(s[r_pointer]):
                r_pointer -= 1

            # this checks if the character is even the same 
            if (s[l_pointer].lower() != s[r_pointer].lower()):
                return False
            l_pointer, r_pointer = l_pointer + 1, r_pointer - 1        
        return True

    #   Returns a boolean to determine if the 
    #   character that  we passed in was a  
    #   alpha numeric character or not 
    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or # Checks upper-case
                    ord('a') <= ord(c) <= ord('z') or # Checks lower-case
                    ord('0') <= ord(c) <= ord('9'))

