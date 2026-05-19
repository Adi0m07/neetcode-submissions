class Solution:
    def isPalindrome(self, s: str) -> bool:
        empty = ""
        for ch in s:
            if ch.isalnum():
                empty += ch.lower()
        return empty == empty[::-1]        
