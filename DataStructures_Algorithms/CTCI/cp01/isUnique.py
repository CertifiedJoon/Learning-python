import time
import unittest
from collections import defaultdict

def isUniqueBruteForce(s):
    """
    O(n^2) runtime and O(1) space
    """
    if not isinstance(s, str):
        raise TypeError("String Required")
    
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

def isUniqueSet(s):
    """
    O(n) runtime but O(n) space
    """
    return len(s) == len(set((c for c in s)))

def isUniqueBitwise(s):
    """ 
    The big implication of isUniqueBitwise is that bit-field 
    can be used as a boolean array with indexing 2^id
    
    O(n) runtime with O(1) space
    """
    if len(s) > 128:
        return False
    check = 0
    for c in s:
        shiftBy = ord(c)
        if (check & 1 << shiftBy) > 0:
            return False
        check |= 1 << shiftBy
    return True


class Test(unittest.TestCase):
    testCases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    
    testFunctions = [
        isUniqueBruteForce,
        isUniqueSet,
        isUniqueBitwise
    ]
    
    def testIsUnique(self):
        numRuns = 1000
        functionRuntimes = defaultdict(float)
        
        for _ in range(numRuns):
            for text, expected in self.testCases:
                for isUnique in self.testFunctions:
                    start = time.process_time()
                    assert (
                        isUnique(text) == expected
                    ), f"{isUnique.__name__} failed for value: {text}"
                    functionRuntimes[isUnique.__name__] += (
                        time.process_time() - start
                    ) * 1000
                    
        print(f"\n{numRuns} runs")
        for functionName, runtime in functionRuntimes.items():
            print(f"{functionName}: {runtime:.1f}ms")
            
if __name__ == "__main__":
    unittest.main()
                    
            