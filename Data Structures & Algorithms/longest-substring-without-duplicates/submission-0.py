class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        

        existing = set()
        ans = 0
        j = 0
        i = 0
        while i < len(s):
            while s[i] in existing:
                existing.remove(s[j])
                j+=1
            existing.add(s[i])
            i+=1
            ans = max(ans, i-j)
        
        return ans
            
            




        