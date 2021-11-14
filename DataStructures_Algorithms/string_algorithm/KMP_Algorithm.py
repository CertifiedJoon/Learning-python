class Solution(object):
    def lpsCalc(self, needle,n):
        lps = [0 for i in range(n)]
        len = 0
        i = 1
        while(i < n):
            if (needle[i] == needle[len]):
                len += 1
                lps[i] = len
                i += 1
            elif (len):
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1
        return lps
    
    def kmp(self, haystack, needle):
        m = len(haystack)
        n = len(needle)
        i = 0
        j = 0
        lps = Solution().lpsCalc(needle,n)
        if not n:
            return ""
        while(i < m):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            if (j == n):
                return i - j
            if (i < m and haystack[i] != needle[j]):
                if (j):
                    j = lps[j-1]
                else:
                    i+=1
        return -1

sl = Solution()
sl.kmp("aaaaa", "bba")
