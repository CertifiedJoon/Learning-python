def boyer_moore_search_bad_char(haystack, needle):
    bad_char = bad_char_heurestics(needle)
    m = len(haystack)
    n = len(needle)
    s = 0
    print(bad_char)
    while (s <= m - n):
        j = n - 1
        while j >= 0 and haystack[s + j] == needle[j]:
            j -= 1
        if j < 0:
            return s
        else:
            if bad_char[ord(haystack[s + j])] == -1:
                s += j + 1
            else:
                s += max(1, j - bad_char[ord(haystack[s + j])])
    return -1

def bad_char_heurestics(needle):
    NO_OF_CHAR = 128
    bad_char = [-1] * NO_OF_CHAR
    for i in range(len(needle)):
        bad_char[ord(needle[i])] = i
    return bad_char

if __name__ == "__main__":
    print(boyer_moore_search_bad_char("For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.", "For sequences"))
    
    