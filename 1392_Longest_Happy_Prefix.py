# Using LPS Method

class Solution:
    def longestPrefix(self, s: str):
        n = len(s)
        lps = [0]*n
        ln = 0
        i = 1

        while i<n:
            if s[i]==s[ln]:
                ln += 1
                lps[i] = ln
                i += 1
            elif:
                ln = lps[ln-1]
            else:
                i += 1
        
        return s[:lps[-1]]