'''
Valid Palindrome:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric 
characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Time Complexity: O(n)
Space Complexity: O(1)
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isAlphaNum(char):
            return (ord("A") <= ord(char) <= ord("Z") or
                    ord("a") <= ord(char) <= ord("z") or
                    ord("0") <= ord(char) <= ord("9"))
        
        left = 0
        right = len(s) -1
        s = s.lower()

        while left < right:
            if not isAlphaNum(s[left]):
                left += 1
                continue

            if not isAlphaNum(s[right]):
                right -= 1
                continue
            
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1

        return True