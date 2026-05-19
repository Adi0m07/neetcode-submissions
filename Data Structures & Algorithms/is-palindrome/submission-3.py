class Solution:
    def isPalindrome(self, s: str) -> bool:
        def vc(ch):
            if 'a' <= ch <= 'z':
                return True
            if '0' <= ch <= '9':
                return True
            return False
             
        def p(x):
            l  , r = 0 , len(x)-1
            while l < r:
                while l<r and not vc(x[l].lower()):
                    l +=1
                while l<r and not vc(x[r].lower()):
                    r -=1
                if x[l].lower() != x[r].lower():
                    return False
                l +=1 
                r -=1
            return True
        return p(s)
