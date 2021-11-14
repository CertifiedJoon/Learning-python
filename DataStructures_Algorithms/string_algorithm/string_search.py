import time
import unittest
from collections import defaultdict
import random

# RK_Search
def rabin_karp_search(haystack, needle):
    d = len(set(c for c in haystack))
    m = len(haystack)
    n = len(needle)
    
    hash_needle = rk_hash(needle,d)
    hash_haystack = rk_hash(haystack[0:n],d)
    
    for i in range(m - n + 1):
        if hash_needle == hash_haystack and needle == haystack[i:i+n]:
            return i
        
        if i + n < m:
            hash_haystack = d * (hash_haystack - pow(d, n-1) * ord(haystack[i])
            ) + (ord(haystack[i + n]))
        
    return -1

def rk_hash(s, n_chr_set):
    ret_hash = 0
    for c in s:
        ret_hash = ret_hash * n_chr_set + ord(c)
    return ret_hash

# KMP Search
def knuth_morris_pratt_search(haystack, needle):
    m = len(haystack)
    n = len(needle)
    lps = calc_lps(needle)
    i = j = 0
    
    while (i < m and j < n):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        if j == n:
            return i - n
        
        if i < m and haystack[i] != needle[j]:
            if j:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1
                
def calc_lps(needle):
    n = len(needle)
    ret = [0 for _ in range(n)]
    common_length = 0
    i = 1
    
    while (i < n):
        if needle[i] == needle[common_length]:
            common_length += 1
            ret[i] = common_length
            i += 1
        elif (common_length):
            common_length = ret[common_length - 1]
        else:
            i += 1
    
    return ret
    
# BM Search
def boyer_moore_search_bad_char(haystack, needle):
    bad_char = bad_char_heurestics(needle)
    m = len(haystack)
    n = len(needle)
    s = 0
    while (s <= m - n):
        j = n - 1
        while j >= 0 and haystack[s + j] == needle[j]:
            j -= 1
        if j == -1:
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
    
    
def boyer_moore_search_good_char(haystack, needle):
    s = 0
    m = len(haystack)
    n = len(needle)
    bpos = [0] * (n + 1)
    shift = [0] * (n + 1)
    
    process_good_char_heuristics(bpos, shift, needle, n)
    process_complete_shift(bpos, shift, n)
    
    while (s <= m - n):
        j = n - 1
        
        while j >= 0 and haystack[s + j] == needle[j]:
            j -= 1
        
        if j < 0:
            return s
        
        else:
            s += shift[j + 1]
    return -1
    
def process_good_char_heuristics(bpos, shift, needle, n):
    i = n 
    j = n + 1
    bpos[i] = j
    while i > 0:
        while j <= n and needle[i - 1] != needle[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i 
            else:
                j = bpos[j]
        i -= 1
        j -= 1
        bpos[i] = j 

def process_complete_shift(bpos, shift, m):
    j = bpos[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = bpos[j]
        
class Test(unittest.TestCase):
    test_cases_real_life = [
        ("For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.", "For sequences", 55),
        ("algorithm demonstration. This is the primary type of problem and solution that the text is concerned with. As such, solutions should not use standard library functions in cases that would make it unnecessary to implement the algorithm. The goal of these solutions should be to have an easy to understand solution that demonstrates understanding of the algori",
        "library functions in cases that would make it unnecessary to implement the algorithm", 150),
        ("If neither weights nor cum_weights are specified, selections are made with equal probability. If a weights sequence is supplied, it must be the same length as the population sequence. It is a TypeError to specify both weights and cum_weights.", "cum_weights.", 230),
        ("On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma, and beta distributions. For generating distributions of angles, the von Mises distribution is available.", "distributions of", 156),
        ("python demonstration. We also accept solutions that solve the problem in a more practical way, using whatever standard library functions are available. Please do not use any third party dependencies. These solutions should also be easy to understand and good examples of pythonic ways of doing things.", "I have no clue", -1),
        ("When the hash value of the pattern matches with the hash value of a window of the text but the window is not the actual pattern then it is called a spurious hit.Spurious hit increases the time complexity of the algorithm. In order to minimize spurious hit, we use modulus. It greatly reduces the spurious hit.", "helloworld", -1),
        ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut posuere nisi elementum justo rhoncus sollicitudin. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Suspendisse vitae nunc metus. Vestibulum mattis, lectus non accumsan fringilla, dolor augue viverra arcu, quis sagittis sapien massa id augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Fusce mattis ac sem non sagittis. Sed ac iaculis tortor, lobortis interdum dolor. Aliquam eget sodales tortor. In rutrum faucibus libero, a laoreet sapien cursus non. Integer vulputate lorem id risus fringilla feugiat. Pellentesque molestie dapibus pharetra. Nam vestibulum lorem at tempor gravida. Maecenas tortor sem, molestie non pretium sit amet, consequat in ipsum. In sed rutrum tortor. Duis consequat nisi non scelerisque finibus. Nam eu imperdiet mi. Donec leo nulla, eleifend et posuere id, accumsan consectetur erat. Nam viverra risus turpis, ultrices feugiat metus eleifend ac. Mauris ultrices, felis in pulvinar egestas, magna arcu convallis metus, nec cursus enim nisi eget lacus. Pellentesque quis diam in ligula faucibus tincidunt in at urna. Pellentesque sit amet leo et felis facilisis semper. Curabitur bibendum nulla id tellus lacinia accumsan. Ut nisi orci, laoreet ac vestibulum ut, ornare sed metus. Proin accumsan vestibulum nisi, in bibendum risus commodo sit amet. Aliquam pretium vestibulum dictum. Vivamus fermentum tellus eget massa faucibus, eu blandit urna commodo. Suspendisse varius urna leo, congue ultricies nibh cursus nec. Fusce sit amet augue malesuada, tristique augue non, ullamcorper augue. Aenean ut neque tristique, ullamcorper felis id, maximus lorem. Vivamus molestie auctor metus, ac ornare ligula vehicula vitae. Aenean suscipit semper lobortis. Pellentesque nisl velit, posuere sed lacus vitae, congue tincidunt justo. Nam non orci vel nunc consectetur bibendum quis sit amet nibh. Curabitur nec nibh bibendum, tempus turpis sit amet, hendrerit lorem. Vivamus fermentum posuere lacus ut sollicitudin. Integer varius luctus purus, ac ultricies neque semper vel. Nam convallis justo iaculis libero interdum, at efficitur mauris dictum. Vivamus a quam vitae metus euismod dapibus nec quis lectus. Aliquam sollicitudin sem at dui mattis, in elementum ligula vestibulum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut tempor mauris justo, at vulputate tortor dictum nec. Morbi molestie posuere turpis, ac lobortis lorem. Maecenas massa dolor, pharetra in tellus vitae, convallis dictum orci. Proin eu erat nisi. Ut placerat urna ac orci venenatis facilisis. Nullam in ante odio. Integer vel est eget odio dapibus aliquam et at lacus. Nullam libero ante, posuere et molestie et, sodales rutrum ex. Proin mollis turpis non massa posuere varius. Nullam bibendum lacus non purus auctor suscipit. Curabitur erat dolor, tempus sed erat a, gravida euismod neque. Sed est orci, rhoncus eu cursus eget, finibus vitae sapien. Maecenas feugiat augue vitae vulputate aliquam. In tempor, libero ac lobortis dictum, leo est lacinia sem, ac sagittis risus urna auctor nulla. In a iaculis nunc.","In a iaculis nunc", 3149)
    ]
    test_cases_random = [
        ("AAAAAAAAAAAAAAA","BBA", -1),
        ("AAAAAAAAAAAAAA", "AAAAAAAAB", -1),
        ("aaaaaabbbbba", "bbbbb", 6),
        ("ADDBDDADDBDDCDADDBDDCDDCDD", "ADDBDDCDD", 14),
        ("ABBABBABBABBABABBABAA", "ABBABAB", 9)
    ]
    
    for _ in range(10000):
        temp = random.choices(range(97, 123), k=random.randrange(10,20))
        random_str = "".join([chr(e) for e in temp])
        start = random.randrange(0, len(random_str) // 2)
        end = random.randrange(len(random_str)//2, len(random_str) + 1)
        test_cases_random.append((random_str, "asdf1dca", -1))
        
    #     test_cases_random.append((random_str, random_str[start:end], random_str.find(random_str[start:end])))
    
    test_functions = [
        rabin_karp_search,
        knuth_morris_pratt_search,
        boyer_moore_search_bad_char,
        boyer_moore_search_good_char
    ]
    
    def test_pattern_search(self):
        num_runs = 1
        function_runtimes = defaultdict(float)
        
        for _ in range(num_runs):
            for haystack, needle, expected in self.test_cases_random:
                for string_search in self.test_functions:
                    start = time.process_time()
                    assert(
                    string_search(haystack, needle) == expected
                    ), f"{string_search.__name__} failed at {haystack} looking for {needle}"
                    function_runtimes[string_search.__name__] += (
                    time.process_time() - start) * 1000
                    
        print(f"\n{num_runs} runs of random pattern")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<30s}: {runtime:.1f}ms")
        
    def test_real_life_search(self):
        num_runs = 100
        function_runtimes = defaultdict(float)
        
        for _ in range(num_runs):
            for haystack, needle, expected in self.test_cases_real_life:
                for string_search in self.test_functions:
                    start = time.process_time()
                    assert(
                    string_search(haystack, needle) == expected
                    ), f"{string_search.__name__} failed at \n{haystack} \nlooking for: \n{needle}"
                    function_runtimes[string_search.__name__] += (
                    time.process_time() - start) * 1000
                    
        print(f"\n{num_runs} runs of real life passage")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<30s}: {runtime:.1f}ms")
    
    
if __name__ == "__main__":
    """
    RabinKarp takes the most time in almost all types of test cases. Real life passage, repeated letters and random letters. Hash value application can be noted
    Runtime also expand faster than others when the text enlarges.
    KnuthMorrisPratt search takes the second most time in all types of test cases, although significantly less than RK
    Boyer_Moore_search implemented with bad character match shows strong performance in real-life passages. Also comparable performance with repeated pattern examples,
    when compared with good character heuristics. Boyer Moore Search with bad character should be the go to rule of thumb.
    Boyer Moore search implemented with good character heuristics shows strong performance in repeated similar patterns case.
    """
    unittest.main()