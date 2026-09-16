import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # handle edge cases (lengths 1 and 0)
        if len(s) == 0:
            return False
        elif len(s) == 1:
            return True
        
        # first we need to strip all punctuation, whitespace, and turn to lowercase
        cleanStr = re.sub(r'[\W_]+', '', s)
        cleanStr = cleanStr.lower()
        
        # now use 2 pointers to work from the outside in
        # make sure to check if the pointers are at the same point, this is where the loop will end
        # if the values at the pointers are not equal, break
        # else, update the pointer values and continue

        i = 0
        j = len(cleanStr) - 1

        while (i < j):
            if cleanStr[i] != cleanStr[j]:
                return False
            
            i += 1
            j -= 1

        return True


