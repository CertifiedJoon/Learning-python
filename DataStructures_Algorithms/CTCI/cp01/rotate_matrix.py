import time
import unittest
from collections import defaultdict
from copy import deepcopy
def rotate_matrix_layer(matrix):
    """
    takes in 2d array matrix of N*N to rotate it
    90 degrees layer by layer
    """
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            top = matrix[layer][i]
            matrix[layer][i] = matrix[-i - 1][layer]
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            matrix[i][-layer - 1] = top
            
    return matrix

def rotate_matrix_pythonic_right(matrix): 
    """
    pythonic code for the above method
    The big
    """
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
    for i, j in zip(range(n), range(n-1, -1, -1)):
        for k in range(n):
            result[k][i] = matrix[j][k]
    return result

def rotate_matrix_pythonic_left(matrix):
    """
    pythonic code modified to shift left
    """
    n = len(matrix)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for k,j in zip(range(n), range(n-1, -1, -1)):
            result[k][i] = matrix[i][j]
    return result

class Test(unittest.TestCase):
    test_cases = [
        # ([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]],
        #  [[12,8,4,0],[13,9,5,1],[14,10,6,2],[15,11,7,3]])
        ([[12,8,4,0],[13,9,5,1],[14,10,6,2],[15,11,7,3]],
         [[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
    ]
    
    test_functions = [
        # rotate_matrix_layer,
        # rotate_matrix_pythonic_right
        rotate_matrix_pythonic_left
    ]
    
    def test_rotate_matrix(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)
        for _ in range(num_runs):
            for matrix, expected in self.test_cases:
                for rotate_matrix in self.test_functions:
                    start = time.process_time()
                    assert(
                        rotate_matrix(matrix) == expected
                    ), f"{rotate_matrix.__name__} failed at {matrix}"
                    function_runtimes[rotate_matrix.__name__] += (
                    (time.process_time() - start) * 1000)
        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<25s}: {runtime:.1f}ms")
            
if __name__ == "__main__":
    unittest.main()