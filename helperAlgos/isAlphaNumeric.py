'''
Time Complexity: O(1)

Space Complexity: O(1)
'''

def isAlphaNumeric(char):
    return (ord("A") <= ord(char) <= ord("Z") or
            ord("a") <= ord(char) <= ord("z") or
            ord("0") <= ord(char) <= ord("9"))
