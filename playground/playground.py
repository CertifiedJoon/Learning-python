def lpsCalc(needle, n):
    i = 1
    le = 0
    lps = [0 for i in range(n)]
    while (i < n):
        if (needle[le] = needle[i]):
            le += 1
            lps[i] = le
            i += 1
        else:
            if (le):
                le = lps[le]
            else:
                i += 1
    return lps

def find(needle, haystack):
    n = len(needle)
    m = len(haystack)
    i = j = 0
    while(i < m and j < n):
        if (haystack[i] == needle[j]):
            i += 1
            j += 1
        if j == n:
            return i - n
        if (i < m and haystack[i] != needle[j]):
            if j:
                j = lps[j-1]
            else:
                j = 0
    return -1
            