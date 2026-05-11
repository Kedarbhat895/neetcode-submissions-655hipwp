class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        d = {}
        ans = 0
        maxFreq = 0
        j = 0
        i = 0


        while i < len(s):
            d[s[i]] = d.get(s[i], 0)+1
            maxFreq = max(maxFreq, d[s[i]])

            while (i-j+1) - maxFreq > k:
                d[s[j]]-=1
                j+=1
            
            ans = max(ans, i-j+1)
            i+=1
        return ans


            
        