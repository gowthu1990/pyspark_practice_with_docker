class Solution:  
    def largeOddNum(self, s: str) -> str:
        if len(s) == 0:
            return ""
        
        if s.endswith(("1","3","5","7","9")):
            return s
        else:
            return self.largeOddNum(s[:len(s)-1])
        


s = Solution()

print(s.largeOddNum("22222"))