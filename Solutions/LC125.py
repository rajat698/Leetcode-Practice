class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        for i in s:
            
            if i not in 'qwertyuioplkjhgfdsazxcvbnm1234567890':
                s = s.replace(i, "")
        
        if not s:
            return True
        
        def palindrome(s):

            l, r = 0, len(s) - 1

            while l < r:

                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True
        
        return palindrome(s)
        