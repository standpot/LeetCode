class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        else:
            x1 = int(str(x)[::-1])  # [::-1] flips the string <- ->
            if(x == x1):
                return True
            else:
                return False